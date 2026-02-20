"""CLI entrypoint for dr-get-llms plugin."""

import json
import sys


def print_manifest():
    """Print the plugin manifest for DataRobot CLI discovery."""
    manifest = {
        "name": "get-llms",
        "version": "0.1.0",
        "description": "Lists all available models in the LLM gateway",
        "authentication": True
    }
    print(json.dumps(manifest, indent=2))


def list_models():
    """List all available LLM Gateway models."""
    import datarobot

    catalog = datarobot.genai.LLMGatewayCatalog()
    models = [
        {"llm_id": x["llm_id"], "model": x["model"]}
        for x in catalog.list_as_dict()
    ]

    if not models:
        print("No models found")
        raise SystemExit(0)

    # Print header
    print("\nDataRobot Available Models")
    print("=" * 80)
    print()

    # Calculate column widths
    max_id_len = max(len(m["llm_id"]) for m in models)
    max_model_len = max(len(m["model"]) for m in models)

    # Print table header
    print(f"{'LLM ID':<{max_id_len}}  {'Model':<{max_model_len}}")
    print(f"{'-' * max_id_len}  {'-' * max_model_len}")

    # Print rows
    for model in sorted(models, key=lambda x: x["model"]):
        print(f"{model['llm_id']:<{max_id_len}}  {model['model']:<{max_model_len}}")

    print()
    print(f"Total: {len(models)} models")
    print()


def main():
    """Main entrypoint for the dr-get-llms command."""
    if len(sys.argv) > 1 and sys.argv[1] == "--dr-plugin-manifest":
        print_manifest()
    else:
        list_models()


if __name__ == "__main__":
    main()
