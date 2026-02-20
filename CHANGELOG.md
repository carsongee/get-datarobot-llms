# Changelog

## Version 0.1.0 (2026-02-20)

### New Features

#### Python Package & DataRobot Plugin Support
- Created installable Python package structure with `dr-get-llms` entrypoint
- Full DataRobot CLI plugin support with `--dr-plugin-manifest`
- Plugin manifest includes `authentication: true` flag
- Package can be installed via `uv tool install .` (recommended) or `pip install .`
- Works as both `dr get-llms` (via DataRobot CLI) and `dr-get-llms` (standalone)

#### Enhanced Field Display
- Added command-line arguments to toggle display of all available model fields
- `model` and `llm_id` are always displayed as core fields
- 22 optional fields can be independently toggled with `--show-*` flags:
  - name, description, provider, creator
  - context_size, max_completion_tokens
  - capabilities, supported_languages
  - input_types, output_types, parameters
  - documentation_link, reference_links
  - date_added, license
  - is_preview, is_metered, is_deprecated, is_active
  - retirement_date, suggested_replacement
  - available_regions
- `--show-all` convenience flag to display all fields at once

#### Smart Filtering
- `--filter-active` (default: enabled) - Show only active models
- `--no-filter-active` - Show all models regardless of active status
- `--show-deprecated` - Include deprecated models (default: hidden)

#### Enhanced Table Display
- Dynamic column width calculation based on content
- Automatic truncation of complex fields (lists, dicts) at 50 characters
- Proper header formatting with field names
- Filter status displayed in output footer

### Technical Improvements
- Uses `argparse` for robust command-line argument parsing
- Organized help output with filter and field groups
- Maintains backward compatibility with original `llms.py` script
- Both scripts share same functionality
- No changes to original `llms.py` behavior when run without arguments

### Documentation
- Updated README.md with installation and usage examples
- Created PLUGIN_TESTING.md for verification and testing guide
- Added comprehensive command-line option documentation
- Included practical usage examples

## Migration from Original Script

The original `llms.py` script continues to work exactly as before when run without arguments:
```bash
uv run llms.py
# or
uv run https://bit.ly/4b213e8
```

For enhanced functionality, use the command-line arguments:
```bash
python llms.py --show-provider --show-context-size
```

Or install the package for DataRobot CLI integration:
```bash
uv tool install .
dr get-llms --show-all
```
