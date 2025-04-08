#!/usr/bin/env python3
import subprocess
import re

def get_latest_tag():
    try:
        output = subprocess.check_output(["git", "tag"], stderr=subprocess.STDOUT)
        tags = output.decode().strip().splitlines()
        semver_tags = [tag for tag in tags if re.match(r"v\d+\.\d+\.\d+", tag)]
        if not semver_tags:
            return "v0.0.0"
        semver_tags.sort(key=lambda s: list(map(int, s.lstrip("v").split("."))))
        return semver_tags[-1]
    except subprocess.CalledProcessError:
        return "v0.0.0"

def bump_patch(version):
    major, minor, patch = map(int, version.lstrip("v").split("."))
    patch += 1
    return f"v{major}.{minor}.{patch}"

if __name__ == "__main__":
    latest = get_latest_tag()
    new_version = bump_patch(latest)
    print(new_version)