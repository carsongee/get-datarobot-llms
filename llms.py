#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "datarobot",
#   "tabulate",
# ]
# ///

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
