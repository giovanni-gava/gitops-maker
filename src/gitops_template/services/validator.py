import os
import json
import yaml
from rich.tree import Tree
from rich import print


def load_validation_config(path: str) -> dict:
    config_file = os.path.join(path, ".validate.yml")
    if os.path.isfile(config_file):
        with open(config_file) as f:
            return yaml.safe_load(f)
    # fallback se não existir .validate.yml
    return {
        "required_files": ["README.md", "atlantis.yaml", ".gitlab-ci.yml"],
        "required_dirs": ["modules", "envs"],
        "check_tf_in_envs": True
    }


def validate_structure(path: str, output_json: bool = False, show_tree: bool = False) -> dict:
    config = load_validation_config(path)

    required_files = config.get("required_files", [])
    required_dirs = config.get("required_dirs", [])
    check_tf = config.get("check_tf_in_envs", True)

    result = {
        "checked_path": path,
        "valid": True,
        "errors": [],
        "warnings": [],
    }

    tree = Tree(f"[bold blue]{path}[/]") if show_tree else None

    # Validação de arquivos obrigatórios
    for file in required_files:
        file_path = os.path.join(path, file)
        if not os.path.isfile(file_path):
            result["errors"].append(f"Missing file: {file}")
            result["valid"] = False
        elif tree:
            tree.add(f"📄 {file}")

    # Validação de diretórios obrigatórios
    for d in required_dirs:
        dir_path = os.path.join(path, d)
        if not os.path.isdir(dir_path):
            result["errors"].append(f"Missing dir: {d}")
            result["valid"] = False
        elif tree:
            tree.add(f"📁 {d}")

    # Validação de arquivos .tf por ambiente
    envs_dir = os.path.join(path, "envs")
    if check_tf and os.path.isdir(envs_dir):
        for env in os.listdir(envs_dir):
            env_path = os.path.join(envs_dir, env)
            if os.path.isdir(env_path):
                tf_files = [f for f in os.listdir(env_path) if f.endswith(".tf")]
                if not tf_files:
                    result["warnings"].append(f"Env '{env}' has no .tf files")
                if tree:
                    branch = tree.add(f"📁 envs/{env}/")
                    for f in os.listdir(env_path):
                        branch.add(f"📄 {f}")

    # Exibir resultados
    if output_json:
        print(json.dumps(result, indent=2))
    elif show_tree and tree:
        print(tree)

    return result
