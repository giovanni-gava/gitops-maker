import typer
from gitops_template.services.validator import validate_structure

validate_app = typer.Typer()

@validate_app.command("structure")
def validate(
    path: str = typer.Argument(..., help="Caminho do projeto"),
    output_json: bool = typer.Option(False, "--json", help="Saída em JSON para CI/CD"),
    show_tree: bool = typer.Option(False, "--tree", help="Exibe árvore de arquivos com Rich"),
):
    """
    Valida se a estrutura do projeto GitOps está correta.
    """
    result = validate_structure(path, output_json=output_json, show_tree=show_tree)

    if not output_json:
        for err in result["errors"]:
            typer.secho(f"❌ {err}", fg=typer.colors.RED)

        for warn in result["warnings"]:
            typer.secho(f"⚠️ {warn}", fg=typer.colors.YELLOW)

        if result["valid"]:
            typer.secho("✅ Estrutura válida!", fg=typer.colors.GREEN)
        else:
            typer.secho("❌ Estrutura com problemas.", fg=typer.colors.RED)

    raise typer.Exit(code=0 if result["valid"] else 1)

