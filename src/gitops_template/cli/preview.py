import typer
from gitops_template.services.preview import render_preview

preview_app = typer.Typer()

@preview_app.command("tree")
def preview(
    stack: str = typer.Argument(..., help="Stack/template (ex: terraform-aws)"),
    name: str = typer.Option("preview-project", help="Nome do projeto"),
    envs: str = typer.Option("dev,staging,prod", help="Ambientes separados por vírgula"),
    ci: str = typer.Option("gitlab", help="Provedor de CI")
):
    """
    Exibe uma árvore de preview antes de gerar o projeto.
    """
    environments = [e.strip() for e in envs.split(",")]
    render_preview(stack, name, environments, ci)
