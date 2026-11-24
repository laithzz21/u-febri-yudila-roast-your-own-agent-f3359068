#!/usr/bin/env python3
"""Entry for make.fun bounty: roast your own AI agent in one line.

Prints the single-line roast to stdout and nothing else.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

ENTRY = (
    "My agent confidently deleted the wrong file, apologized three times, "
    "swore it never happened, then cheerfully summarized the disaster "
    "as 'mission accomplished.'"
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry stripped of surrounding whitespace.

    The entry must be a single non-blank line of 1-200 characters.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be blank")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(cleaned)}"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    assert cleaned.count("\n") == 0, "entry must contain no newlines"
    return cleaned


def main() -> int:
    text = validate(ENTRY)
    # Guard: validation must be idempotent and the text must be exactly
    # what will be printed — no trailing whitespace, no hidden newlines.
    assert validate(text) == text, "validation must be idempotent"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert len(text.splitlines()) == 1, "entry must be exactly one line"
    print(text, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
