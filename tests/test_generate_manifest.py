"""Exercise resource discovery and change detection in isolated Git repositories."""

import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


spec = importlib.util.spec_from_file_location(
    "generate_manifest", Path(__file__).resolve().parents[1] / "scripts/generate_manifest.py"
)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.git("init", "--quiet")

    def git(self, *args):
        subprocess.run(["git", *args], cwd=self.root, check=True, stdout=subprocess.PIPE)

    def write(self, path, content=b"test\n"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)

    def test_discovers_packages_templates_and_documentation(self):
        for path in (
            "README.md", "docs/资源规范.pdf", "config/robots/README.md",
            "config/robots/talon/robot.yaml", "config/robots/talon/README.md",
            "config/robots/talon/model.urdf", "config/robots/talon/meshes/base.STL",
            "config/robots/talon/eni7.xml", "config/robots/talon/mjcf/scene.xml",
            "config/devices/talon_001/device.yaml", "config/devices/talon_001/frames.yaml",
            "config/tools/gripper/tool.yaml", "config/tools/gripper/LICENSE",
            "config/app.yaml", "config/scripts/README.md", "config/scripts/start.sh",
        ):
            self.write(path)
        manifest = generator.build_manifest(self.root)
        self.assertEqual(manifest, generator.build_manifest(self.root))
        self.assertEqual(manifest["summary"]["resource_types"], {
            "config_template": 1, "device": 1, "robot": 1, "script_collection": 1, "tool": 1,
        })
        files = {item["path"]: item for item in manifest["files"]}
        self.assertEqual(files["config/robots/talon/meshes/base.STL"]["type"], "mesh")
        self.assertEqual(files["config/robots/talon/mjcf/scene.xml"]["type"], "mjcf")
        self.assertEqual(files["config/robots/talon/eni7.xml"]["type"], "ethercat_eni")
        self.assertEqual(files["docs/资源规范.pdf"]["type"], "documentation")
        self.assertIsNone(files["config/robots/README.md"]["resource"])
        robot = next(item for item in manifest["resources"] if item["type"] == "robot")
        self.assertEqual(robot["readme"], "config/robots/talon/README.md")
        self.assertEqual(robot["entrypoint"], "config/robots/talon/robot.yaml")
        self.assertEqual(robot["file_count"], 6)

    def test_tracks_changes_deletions_and_ignored_files(self):
        self.write(".gitignore", b"config/tools/.objects/\n*.tmp\n")
        self.write("config/app.yaml", b"before\n")
        self.write("config/user.yaml")
        self.git("add", ".")
        self.write("config/tools/.objects/cache.json")
        self.write("config/example.tmp")
        self.write("config/scripts/.gitkeep", b"")
        self.write("manifest.json")
        self.write("scripts/helper.py")
        before = generator.build_manifest(self.root)
        self.write("config/app.yaml", b"after\n")
        (self.root / "config/user.yaml").unlink()
        self.write("config/robots/new model/robot.yaml")
        after = generator.build_manifest(self.root)
        files = {item["path"]: item for item in after["files"]}
        self.assertEqual(set(files), {"config/app.yaml", "config/robots/new model/robot.yaml"})
        self.assertNotEqual(before, after)
        self.assertEqual(files["config/app.yaml"]["sha256"], hashlib.sha256(b"after\n").hexdigest())
        self.assertEqual(files["config/app.yaml"]["size_bytes"], 6)

    def test_calibration_history_and_placeholders(self):
        base = "config/devices/talon_001/identification/dynamics"
        self.write(f"{base}/.gitkeep", b"")
        self.write(f"{base}/README.md")
        initial = generator.build_manifest(self.root)
        self.assertNotIn("calibration_data", initial["summary"]["file_types"])
        self.write(f"{base}/2026-11-05_01/parameters.npz", b"\x00\x01")
        self.write(f"{base}/2026-11-06_01/raw/samples.csv")
        manifest = generator.build_manifest(self.root)
        self.assertEqual(manifest["summary"]["file_types"]["calibration_data"], 2)
        self.assertIsNone(manifest["resources"][0]["entrypoint"])

    def test_rejects_symlinks(self):
        self.write("outside.yaml")
        (self.root / "config").mkdir()
        (self.root / "config/app.yaml").symlink_to(self.root / "outside.yaml")
        with self.assertRaisesRegex(ValueError, "symlinks"):
            generator.build_manifest(self.root)


if __name__ == "__main__":
    unittest.main()
