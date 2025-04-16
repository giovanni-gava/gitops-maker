import typer

from gitops_template.cli.generate import generate_app
from gitops_template.cli.validate import validate_app
from gitops_template.cli.preview import preview_app

app = typer.Typer(help="🐍 Scaffold Generator for GitOps Templates")

# Subcomando generate
app.add_typer(generate_app, name="generate", help="Generate a new GitOps-ready repo scaffold")
app = typer.Typer(help="🐍 gitops-maker: scaffold generator for GitOps templates")
app.add_typer(generate_app, name="generate", help="Gera um novo scaffold")
app.add_typer(validate_app, name="validate", help="Valida estrutura do scaffold")
app.add_typer(preview_app, name="preview", help="Mostra preview da estrutura do scaffold")


def main():
    app()

if __name__ == "__main__":
    main()
