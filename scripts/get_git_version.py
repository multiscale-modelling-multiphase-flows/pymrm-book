import os
import sys
sys.path.insert(0, os.path.abspath("../pymrm"))

def get_git_version(submodule_path):
    try:
        # Navigate to the submodule directory
        git_dir = os.path.join(submodule_path, ".git")
        # Get the latest tag or commit hash
        version = subprocess.check_output(
            ["git", "--git-dir", git_dir, "describe", "--tags"],
            universal_newlines=True,
        ).strip()
        return version
    except Exception as e:
        return f"unknown ({e})"

