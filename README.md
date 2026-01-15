# DataRobot LLM Models List

A simple UV-runnable script to list all available DataRobot LLM Gateway models in a clean, easy-to-copy table format.

## Usage

### Run Remotely (No Clone Needed)

You can run the script directly from GitHub without cloning:

```bash
uv run https://raw.githubusercontent.com/carsongee/get-datarobot-llms/main/llms.py
```

### Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/get-datarobot-llms.git
cd get-datarobot-llms
carsongee
# Run the script
./llms.py
# or
uv run llms.py
```

## Requirements

- [UV](https://docs.astral.sh/uv/) package manager
- DataRobot credentials configured (API token)

The script will automatically install the required dependencies (`datarobot` and `tabulate`) when run.

## Output

The script displays models in a formatted table:

```
DataRobot Available Models
================================================================================

LLM ID                                    Model
----------------------------------------  ----------------------------------------
azure-openai-gpt-4o                       azure-openai/gpt-4o
google-gemini-1.5-pro                     google/gemini-1.5-pro
...

Total: XX models
```

## License

See [LICENSE](LICENSE) file for details.
