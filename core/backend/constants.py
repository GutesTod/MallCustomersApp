from pathlib import Path

def get_project_root_dir():
    return Path(__file__).absolute().parent.parent.parent