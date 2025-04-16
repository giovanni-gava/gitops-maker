# src/py_gitops_template/cli/generate.py

import typer
from gitops_template.services.generator import generate_scaffold

generate_app = typer.Typer()

@generate_app.command("new")
def generate(
    name: str = typer.Option(..., prompt=True, help="Project name"),
    stack: str = typer.Option(..., prompt=True, help="Stack template (e.g., terraform-aws, helm-kustomize)"),
    envs: str = typer.Option("dev,staging,prod", help="Comma-separated list of environments"),
    ci: str = typer.Option("gitlab", help="CI provider (gitlab, github, jenkins, etc.)"),
    output: str = typer.Option(".", help="Output directory"),
    preview: bool = typer.Option(False, help="Preview only (don’t write files yet)"),
):
    """
    Generate GitOps-ready project structure
    """
    environments = [env.strip() for env in envs.split(",")]
    typer.echo(f"🔧 Generating project '{name}' with stack '{stack}' in {output}")

    generate_scaffold(
        name=name,
        stack=stack,
        environments=environments,
        ci_provider=ci,
        output_dir=output,
        preview=preview
    )
