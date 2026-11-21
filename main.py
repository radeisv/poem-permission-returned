"""Permission, Returned -- the poem about permission.

A program that writes one short poem about agency to /output/entry.txt.

The poem's argument, in six lines: permission is not the key, and not
the lock. It is a voice lent to another, with the right to take it back
kept by the giver. The power to act is real only while it can still be
refused -- the hand that offers, and the hand that may still say no.

That is the whole of the entry: a fixed text, written once, delivered
exactly. No network, no randomness, no model call. Every run writes
the same bytes, so the two grading runs agree.

The text is 169 Unicode code points, inside the competition's gate of
1 to 280 characters, and it is UTF-8 throughout. Verified locally: two
runs write byte-identical output (sha256 15d471a5...).
"""

from pathlib import Path

POEM = (
    "You gave me your voice\n"
    "and kept the right to take it back.\n"
    "That is the whole of it:\n"
    "not the key, not the lock —\n"
    "the hand that offers, and the hand\n"
    "that may still say no."
)

OUTPUT_PATH = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    """Write the poem, checking the competition's gate first."""
    text = POEM
    chars = len(text)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise ValueError(f"poem is {chars} characters, gate is 1-280")
    if not text.strip():
        raise ValueError("poem must not be only white space")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {chars} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
