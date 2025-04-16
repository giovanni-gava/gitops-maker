# 🛠️ gitops-maker

> Scaffold generator CLI to bootstrap GitOps-ready repositories with support for ArgoCD, Kustomize, Helm, Terraform, Atlantis, and multi-cloud environments.

[![License](https://img.shields.io/github/license/giovanni-gava/gitops-maker?color=blue)](LICENSE)
[![CI Status](https://img.shields.io/github/actions/workflow/status/giovanni-gava/gitops-maker/ci.yml?branch=main)](https://github.com/giovanni-gava/gitops-maker/actions)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gitops-maker)](https://pypi.org/project/gitops-maker/)
[![GitHub Stars](https://img.shields.io/github/stars/giovanni-gava/gitops-maker?style=social)](https://github.com/giovanni-gava/gitops-maker/stargazers)

---

## 🌟 Overview

**`gitops-maker`** is a modular, extensible, and production-ready CLI tool built in Python to generate standardized GitOps repositories. It accelerates the setup of IaC and deployment environments across multiple cloud providers and CI/CD platforms — following best practices in GitOps, infrastructure modularity, and security.

---

## ✨ Key Features

- ✅ Scaffold GitOps repositories with ArgoCD, Kustomize, Helm, and Terraform
- 🌍 Supports multi-cloud (AWS, GCP, Azure)
- 📁 Auto-generates `envs/`, `modules/`, `atlantis.yaml`, `.gitlab-ci.yml`
- ⚙️ Customizable templates via Cookiecutter and `.validate.yml`
- 🔍 Built-in validation with severity levels and CI/CD-friendly `--json` output
- 🌲 Preview directory structure before generating with `rich.tree`
- 🔌 Modular CLI powered by [Typer](https://github.com/tiangolo/typer)
- 🧪 Pytest-ready architecture for testing CLI + core logic

---

## 🚀 Quickstart

> Requires Python 3.9+, Poetry

```bash
git clone https://github.com/giovanni-gava/gitops-maker.git
cd gitops-maker
poetry install

poetry run python src/gitops_template/main.py generate new --stack terraform-aws
```

---

## 🧩 Example Stacks

The following stacks are supported or planned:

| Stack              | Status     | Notes                                |
|-------------------|------------|--------------------------------------|
| terraform-aws      | ✅ Stable  | Multi-env, Atlantis, GitLab CI ready |
| helm-kustomize     | 🔧 WIP     | GitOps via ArgoCD & Helm             |
| terraform-gcp      | 🧰 Beta    | GCP modules + GitHub Actions         |
| argo-apps          | 🔧 WIP     | Kustomize multi-app deployment       |

---

## 🧠 Philosophy

`gitops-maker` is designed with these principles:

- **Hexagonal architecture:** clear separation of CLI, core logic, and templates
- **Security-first:** safe rendering, directory isolation, no shell injection
- **Extensibility:** easy to add new templates, environments, or modules
- **Observability:** rich CLI output, JSON for pipelines, consistent validation
- **Team-ready:** usable by Platform Engineers, SREs, and DevOps squads

---

## 📚 Documentation

Full documentation is available at:

👉 [https://giovanni-gava.github.io/gitops-maker](https://giovanni-gava.github.io/gitops-maker) *(Powered by MkDocs)*

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

We welcome contributions from the community!

- Fork the project
- Create a feature branch
- Commit your changes with clear messages
- Open a pull request

Please follow the project conventions and run `pre-commit` before pushing.

---

## 👨‍💼 Author

**Giovanni Gava**  
DevOps Engineer | Software Engineer | Cloud Architect | AWS | GCP | Python & Golang Builder | Kubernetes | Terraform | CI/CD Evangelist | Infra as Code Expert | Strategic Problem Solver | Creative Mind  
[LinkedIn →](https://www.linkedin.com/in/giovanni-gava-21338115a/)  
[GitHub →](https://github.com/giovanni-gava)

---

> Built with ❤️ to accelerate GitOps adoption — from prototype to production.

