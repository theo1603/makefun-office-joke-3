"""One-line office joke: the calendar that declines its owner.

Writes one original one-line joke about office life to /output/entry.txt.
The joke is a single line, well under 200 characters.
Python 3.13 standard library only; no network, no randomness.
"""

import os

JOKE = (
    "My calendar is so full I tried to book a meeting with myself, "
    "and I declined it \u2014 I was already in a meeting with myself."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
