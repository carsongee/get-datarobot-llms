# Plugin Testing Guide

## Installation Verification

After installing the package with `uv tool install .` or `uv pip install -e .` for development, verify the installation:

1. **Check the command is accessible:**
   ```bash
   which dr-get-llms
   ```
   Should output the path to the executable.

2. **Verify executable permissions:**
   ```bash
   ls -l $(which dr-get-llms)
   ```
   Should show `-rwxr-xr-x` (executable).

3. **Test the plugin manifest:**
   ```bash
   dr-get-llms --dr-plugin-manifest
   ```
   Should output:
   ```json
   {
     "name": "get-llms",
     "version": "0.1.0",
     "description": "Lists all available models in the LLM gateway",
     "authentication": true
   }
   ```

## Using with DataRobot CLI

Once installed, the plugin should be automatically discovered by the DataRobot CLI:

1. **List available plugins:**
   ```bash
   dr plugin list
   ```
   Should include `get-llms`.

2. **Use via DataRobot CLI:**
   ```bash
   dr get-llms
   ```

3. **Or use directly:**
   ```bash
   dr-get-llms
   ```

## Command-Line Options

The command supports various options to customize output:

### Basic usage (default shows only active models):
```bash
dr get-llms
```

### Show all fields:
```bash
dr get-llms --show-all
```

### Show specific fields:
```bash
dr get-llms --show-provider --show-context-size
```

### Include inactive models:
```bash
dr get-llms --no-filter-active
```

### Show deprecated models with replacement info:
```bash
dr get-llms --show-deprecated --show-suggested-replacement
```

### Combine multiple options:
```bash
dr get-llms --show-all --no-filter-active --show-deprecated
```

Run `dr get-llms --help` or `dr-get-llms --help` to see all available options.

## Troubleshooting

If `dr get-llms` doesn't work:

1. Check plugin is discovered:
   ```bash
   dr plugin list
   ```

2. Verify the executable is on PATH:
   ```bash
   which dr-get-llms
   ```

3. Test the manifest manually:
   ```bash
   dr-get-llms --dr-plugin-manifest
   ```

4. Check plugin discovery timeout isn't disabled:
   ```bash
   dr --help | grep plugin-discovery-timeout
   ```

## Requirements

- DataRobot credentials must be configured
- The DataRobot CLI must be installed for `dr get-llms` syntax
- The `dr-get-llms` command works standalone without the DataRobot CLI
