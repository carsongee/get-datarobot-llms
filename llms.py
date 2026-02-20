#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "datarobot",
#   "tabulate",
# ]
# ///

import argparse
import sys

import datarobot


def list_models(args):
    """List all available LLM Gateway models."""
    catalog = datarobot.genai.LLMGatewayCatalog()
    all_models = catalog.list_as_dict()

    # Apply filters
    models = []
    for model in all_models:
        if args.filter_active and not model.get("is_active", True):
            continue
        if not args.show_deprecated and model.get("is_deprecated", False):
            continue
        models.append(model)

    if not models:
        print("No models found")
        raise SystemExit(0)

    # Determine which fields to display
    fields = ["llm_id", "model"]  # Always included
    
    optional_fields = [
        ("name", args.show_name),
        ("description", args.show_description),
        ("provider", args.show_provider),
        ("creator", args.show_creator),
        ("context_size", args.show_context_size),
        ("max_completion_tokens", args.show_max_completion_tokens),
        ("capabilities", args.show_capabilities),
        ("supported_languages", args.show_supported_languages),
        ("input_types", args.show_input_types),
        ("output_types", args.show_output_types),
        ("parameters", args.show_parameters),
        ("documentation_link", args.show_documentation_link),
        ("reference_links", args.show_reference_links),
        ("date_added", args.show_date_added),
        ("license", args.show_license),
        ("is_preview", args.show_is_preview),
        ("is_metered", args.show_is_metered),
        ("retirement_date", args.show_retirement_date),
        ("suggested_replacement", args.show_suggested_replacement),
        ("is_deprecated", args.show_is_deprecated),
        ("is_active", args.show_is_active),
        ("available_regions", args.show_available_regions),
    ]
    
    for field, enabled in optional_fields:
        if enabled:
            fields.append(field)

    # Print header
    print("\nDataRobot Available Models")
    print("=" * 80)
    print()

    # Calculate column widths
    col_widths = {}
    for field in fields:
        header_len = len(field.replace("_", " ").title())
        max_val_len = max(
            len(str(m.get(field, ""))) if not isinstance(m.get(field), (list, dict)) else 50
            for m in models
        )
        col_widths[field] = max(header_len, min(max_val_len, 50))

    # Print table header
    headers = [field.replace("_", " ").title() for field in fields]
    header_line = "  ".join(f"{h:<{col_widths[f]}}" for h, f in zip(headers, fields))
    print(header_line)
    print("  ".join("-" * col_widths[f] for f in fields))

    # Print rows
    for model in sorted(models, key=lambda x: x.get("model", "")):
        row_parts = []
        for field in fields:
            value = model.get(field, "")
            if isinstance(value, (list, dict)):
                value = str(value)[:47] + "..." if len(str(value)) > 50 else str(value)
            else:
                value = str(value)
            row_parts.append(f"{value:<{col_widths[field]}}")
        print("  ".join(row_parts))

    print()
    print(f"Total: {len(models)} models")
    if args.filter_active:
        print("(Filtered to active models only)")
    if not args.show_deprecated:
        print("(Hiding deprecated models)")
    print()


def create_parser():
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        description="List available DataRobot LLM Gateway models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    # Filters
    filter_group = parser.add_argument_group("filters")
    filter_group.add_argument(
        "--filter-active",
        action="store_true",
        default=True,
        help="Show only active models (default: True)",
    )
    filter_group.add_argument(
        "--no-filter-active",
        action="store_false",
        dest="filter_active",
        help="Show all models regardless of active status",
    )
    filter_group.add_argument(
        "--show-deprecated",
        action="store_true",
        default=False,
        help="Include deprecated models",
    )
    
    # Optional fields
    fields_group = parser.add_argument_group("optional fields")
    fields_group.add_argument("--show-name", action="store_true", help="Show name field")
    fields_group.add_argument("--show-description", action="store_true", help="Show description field")
    fields_group.add_argument("--show-provider", action="store_true", help="Show provider field")
    fields_group.add_argument("--show-creator", action="store_true", help="Show creator field")
    fields_group.add_argument("--show-context-size", action="store_true", help="Show context_size field")
    fields_group.add_argument("--show-max-completion-tokens", action="store_true", help="Show max_completion_tokens field")
    fields_group.add_argument("--show-capabilities", action="store_true", help="Show capabilities field")
    fields_group.add_argument("--show-supported-languages", action="store_true", help="Show supported_languages field")
    fields_group.add_argument("--show-input-types", action="store_true", help="Show input_types field")
    fields_group.add_argument("--show-output-types", action="store_true", help="Show output_types field")
    fields_group.add_argument("--show-parameters", action="store_true", help="Show parameters field")
    fields_group.add_argument("--show-documentation-link", action="store_true", help="Show documentation_link field")
    fields_group.add_argument("--show-reference-links", action="store_true", help="Show reference_links field")
    fields_group.add_argument("--show-date-added", action="store_true", help="Show date_added field")
    fields_group.add_argument("--show-license", action="store_true", help="Show license field")
    fields_group.add_argument("--show-is-preview", action="store_true", help="Show is_preview field")
    fields_group.add_argument("--show-is-metered", action="store_true", help="Show is_metered field")
    fields_group.add_argument("--show-retirement-date", action="store_true", help="Show retirement_date field")
    fields_group.add_argument("--show-suggested-replacement", action="store_true", help="Show suggested_replacement field")
    fields_group.add_argument("--show-is-deprecated", action="store_true", help="Show is_deprecated field")
    fields_group.add_argument("--show-is-active", action="store_true", help="Show is_active field")
    fields_group.add_argument("--show-available-regions", action="store_true", help="Show available_regions field")
    
    # Convenience flag to show all fields
    parser.add_argument(
        "--show-all",
        action="store_true",
        help="Show all available fields",
    )
    
    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle --show-all flag
    if args.show_all:
        for arg in vars(args):
            if arg.startswith("show_") and arg != "show_all":
                setattr(args, arg, True)
    
    list_models(args)
