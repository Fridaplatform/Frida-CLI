import re


def add_styletags_to_string(string: str, style: str) -> str:
    """Returns a modified string with style tags added."""
    return f"[{style}]{string}[/]"


def add_styletags_from_regex(string: str) -> str:
    """Returns a modified string with style tags
    added based on predefined regex patterns."""
    regex_patterns = [
        (r"!([\w-]+)", r"[command]!\1[/]"),
        (r"-([\w-]+)", r"[option]-\1[/]"),
        (r"<([^<>]+)>", r"[operation]<\1>[/]"),
    ]

    # Iterate over the patterns and apply the corresponding formatting
    for pattern, replacement in regex_patterns:
        string = re.sub(pattern, replacement, string)

    return string


def print_padding(padding: int = 1):
    if padding > 0:
        print("\n" * (padding - 1))
