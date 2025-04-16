import os
from rich.tree import Tree
from rich import print

def render_preview(stack: str, name: str, envs: list, ci: str):
    tree = Tree(f"[bold blue]{name}/[/]")
    tree.add("📄 README.md")
    tree.add("📄 atlantis.yaml")
    tree.add("📄 .gitlab-ci.yml")

    tree.add("📁 modules/")
    envs_branch = tree.add("📁 envs/")
    for env in envs:
        env_branch = envs_branch.add(f"📁 {env}/")
        env_branch.add("📄 main.tf")

    tree.add("📄 .validate.yml")
    print(f"[bold green]📦 Preview do projeto GitOps '{name}' com stack '{stack}':[/]\n")
    print(tree)
