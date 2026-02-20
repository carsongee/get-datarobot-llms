# DataRobot LLM Models List

List all available DataRobot LLM Gateway models in a clean, easy-to-copy table format.

## Usage

### As a DataRobot CLI Plugin

Install the package to use as a DataRobot CLI plugin:

```bash
uv tool install git+https://github.com/carsongee/get-datarobot-llms.git
```

Or using pip:

```bash
pip install git+https://github.com/carsongee/get-datarobot-llms.git
```

Then use via the DataRobot CLI:

```bash
dr get-llms
```

Or run directly:

```bash
dr-get-llms
```

### As a Standalone Script

```bash
uv run https://bit.ly/4b213e8
```

Or using the full URL:

```bash
uv run https://raw.githubusercontent.com/carsongee/get-datarobot-llms/main/llms.py
```

## Command-Line Options

Both the plugin and standalone script support the following options:

### Filters
- `--filter-active` - Show only active models (default: enabled)
- `--no-filter-active` - Show all models regardless of active status
- `--show-deprecated` - Include deprecated models (default: hidden)

### Optional Fields
By default, only `llm_id` and `model` are shown. Add any of these flags to display additional fields:

- `--show-name` - Display model name
- `--show-description` - Display model description
- `--show-provider` - Display provider
- `--show-creator` - Display creator
- `--show-context-size` - Display context size
- `--show-max-completion-tokens` - Display max completion tokens
- `--show-capabilities` - Display capabilities
- `--show-supported-languages` - Display supported languages
- `--show-input-types` - Display input types
- `--show-output-types` - Display output types
- `--show-parameters` - Display parameters
- `--show-documentation-link` - Display documentation link
- `--show-reference-links` - Display reference links
- `--show-date-added` - Display date added
- `--show-license` - Display license
- `--show-is-preview` - Display preview status
- `--show-is-metered` - Display metered status
- `--show-retirement-date` - Display retirement date
- `--show-suggested-replacement` - Display suggested replacement
- `--show-is-deprecated` - Display deprecated status
- `--show-is-active` - Display active status
- `--show-available-regions` - Display available regions
- `--show-all` - Display all available fields

### Examples

Show basic model list (active models only):
```bash
dr get-llms
```

Show all fields for all models (including inactive):
```bash
dr get-llms --show-all --no-filter-active
```

Show models with provider and context size:
```bash
dr get-llms --show-provider --show-context-size
```

Show deprecated models with suggested replacements:
```bash
dr get-llms --show-deprecated --show-suggested-replacement
```

## Requirements

Requires DataRobot credentials configured. Dependencies are automatically installed.

## Development

Install in editable mode for development:

```bash
uv pip install -e .
```

Or using pip:

```bash
pip install -e .
```
