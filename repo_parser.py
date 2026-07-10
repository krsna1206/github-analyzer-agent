import os
import shutil
import subprocess
import tempfile



def build_repository_context(repo_url):
    TEMP_DIR = tempfile.mkdtemp(prefix="repo_")

    # Remove old repository if it exists
    # if os.path.exists(TEMP_DIR):
    #     shutil.rmtree(TEMP_DIR)

    # Clone repository
    result = subprocess.run(
        ["git", "clone", "--depth", "1", repo_url, TEMP_DIR],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)
    context = {
        "repo": os.path.basename(repo_url),
        "owner": repo_url.split("/")[-2],
        "language": "Unknown",
        "readme": "",
        "tree": [],
        "dependencies": {},
        "source_files": {}
    }

    source_count = 0

    for root, dirs, files in os.walk(TEMP_DIR):

        # Ignore unnecessary folders
        dirs[:] = [
            d for d in dirs
            if d not in {
                ".git",
                ".github",
                "venv",
                ".venv",
                "__pycache__",
                "node_modules"
            }
        ]

        for file in files:

            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, TEMP_DIR)

            context["tree"].append(rel_path)

            # README
            if file.lower() == "readme.md":
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    context["readme"] = f.read()[:3000]

            # Dependencies
            elif file in ["requirements.txt", "package.json"]:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    context["dependencies"][rel_path] = f.read()[:1500]

            # Python files
            elif file.endswith(".py") and source_count < 3:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    context["source_files"][rel_path] = f.read()[:2000]
                source_count += 1

    return context