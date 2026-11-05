#!/usr/bin/env python3
"""Build a deterministic resource index using Python 3.10+ and Git."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SPECIFICATION = "https://rocos-sia.feishu.cn/wiki/Wj2IwOm8BiYslfkxImicRpArn6g"
PACKAGES = {
    "robots": ("robot", "robot.yaml"),
    "devices": ("device", "device.yaml"),
    "tools": ("tool", "tool.yaml"),
}


def resource_for(path):
    """Return (type, package path, entrypoint) from the repository layout."""
    parts = path.parts
    if len(parts) >= 4 and parts[1] in PACKAGES:
        kind, entry = PACKAGES[parts[1]]
        base = PurePosixPath(*parts[:3])
        return kind, base.as_posix(), (base / entry).as_posix()
    if len(parts) >= 3 and parts[1] == "scripts":
        return "script_collection", "config/scripts", None
    if len(parts) == 2 and path.suffix.lower() in {".yaml", ".yml"}:
        return "config_template", path.as_posix(), path.as_posix()
    return None


def file_type(path):
    parts = path.parts
    suffix = path.suffix.lower()
    name = path.name.lower()
    if name.startswith(("license", "copying")):
        return "license"
    if name in {"source.md", "third_party_notices.md"}:
        return "source_notice"
    if suffix in {".md", ".rst", ".pdf", ".docx"}:
        return "documentation"
    if "identification" in parts:
        return "calibration_data"
    if "maintenance" in parts:
        return "maintenance_record"
    if suffix == ".urdf":
        return "urdf"
    if suffix in {".stl", ".obj", ".dae", ".ply", ".off", ".glb", ".gltf"}:
        return "mesh"
    if suffix == ".xml":
        return "mjcf" if "mjcf" in parts else "ethercat_eni" if name.startswith("eni") else "xml"
    if suffix in {".yaml", ".yml"}:
        return {
            "robot.yaml": "robot_config",
            "device.yaml": "device_config",
            "tool.yaml": "tool_config",
            "hardware.yaml": "hardware_config",
            "frames.yaml": "frame_records",
            "mujoco.yaml": "simulation_config",
            "master.yaml": "master_config",
            "ecm.yaml": "master_config",
            "igh.yaml": "master_config",
        }.get(name, "configuration")
    if suffix in {".py", ".sh", ".bash", ".lua"}:
        return "script"
    return "data"


def build_manifest(root):
    # Include new, unignored resources locally, including before the first commit.
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root, check=True, stdout=subprocess.PIPE,
    )
    paths = sorted(set(result.stdout.decode("utf-8").rstrip("\0").split("\0")) - {""})
    files = []
    resources = {}
    for relative in paths:
        path = PurePosixPath(relative)
        if path.parts[0] not in {"config", "docs"} and not (
            len(path.parts) == 1 and (
                path.suffix.lower() == ".md"
                or path.name.lower().startswith(("license", "copying"))
            )
        ):
            continue
        if path.name == ".gitkeep":
            continue
        local = root / relative
        if local.is_symlink() or any(parent.is_symlink() for parent in local.parents if parent != root):
            raise ValueError(f"Resource symlinks are not supported: {relative}")
        if not local.is_file():  # Ignore files deleted from the working tree.
            continue
        digest = hashlib.sha256()
        size = 0
        with local.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
                size += len(chunk)
        item = {
            "path": relative,
            "type": file_type(path),
            "format": path.suffix.lower().lstrip(".") or "text",
            "size_bytes": size,
            "sha256": digest.hexdigest(),
            "resource": None,
        }
        package = resource_for(path) if path.parts[0] == "config" else None
        if package:
            kind, base, entrypoint = package
            item["resource"] = base
            if base not in resources:
                resources[base] = {
                    "id": base,
                    "type": kind,
                    "name": PurePosixPath(base).stem if kind == "config_template" else PurePosixPath(base).name,
                    "path": base,
                    "entrypoint": entrypoint,
                    "readme": None,
                    "file_count": 0,
                }
            resources[base]["file_count"] += 1
        files.append(item)

    indexed = {item["path"] for item in files}
    for resource in resources.values():
        if resource["entrypoint"] not in indexed:
            resource["entrypoint"] = None
        readme = f'{resource["path"]}/README.md'
        if readme in indexed:
            resource["readme"] = readme
    return {
        "schema_version": 1,
        "specification": SPECIFICATION,
        "summary": {
            "resource_count": len(resources),
            "file_count": len(files),
            "total_size_bytes": sum(item["size_bytes"] for item in files),
            "resource_types": dict(sorted(Counter(item["type"] for item in resources.values()).items())),
            "file_types": dict(sorted(Counter(item["type"] for item in files).items())),
        },
        "resources": sorted(resources.values(), key=lambda item: item["path"]),
        "files": files,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if manifest.json needs regeneration")
    args = parser.parse_args()
    content = (json.dumps(build_manifest(ROOT), ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    target = ROOT / "manifest.json"
    if args.check:
        if not target.exists() or target.read_bytes() != content:
            parser.exit(1, "manifest.json is out of date; run python3 scripts/generate_manifest.py\n")
        print("manifest.json is up to date")
    else:
        target.write_bytes(content)
        print("Generated manifest.json")


if __name__ == "__main__":
    main()
