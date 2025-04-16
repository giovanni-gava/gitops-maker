import os
from cookiecutter.main import cookiecutter

def generate_scaffold(name: str, stack: str, environments: list, ci_provider: str, output_dir: str, preview: bool = False):
    template_path = os.path.join(os.path.dirname(__file__), "..", "templates", stack)

    context = {
        "project_name": name,
        "envs": environments,
        "ci": ci_provider,
    }

    if preview:
        print("👀 Preview mode. Would generate with context:")
        print(context)
        print(f"Template path: {template_path}")
        return

    cookiecutter(
        template=template_path,
        no_input=True,
        extra_context=context,
        output_dir=output_dir
    )
