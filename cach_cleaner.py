import shutil
from pathlib import Path

def remove_pycache(root_path: Path):
    removed_count = 0

    for path in root_path.rglob("__pycache__"):
        if path.is_dir():
            shutil.rmtree(path)
            removed_count += 1
            print(f"Removed: {path}")

    print(f"\nDone. Removed {removed_count} '__pycache__' directories.")

if __name__ == "__main__":
    root_directory = Path.cwd()
    print(f"Scanning: {root_directory}\n")
    remove_pycache(root_directory)
