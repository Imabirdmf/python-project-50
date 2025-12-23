import json

import yaml


def file_parser(file_path: str) -> dict:
    with open(file_path, "r") as f:
        if file_path.endswith(".yaml") or file_path.endswith(".yml"):
            return yaml.safe_load(f)
        elif file_path.endswith(".json"):
            return json.load(f)
        raise FileNotFoundError(f"File {file_path} is not a valid YAML file.")
