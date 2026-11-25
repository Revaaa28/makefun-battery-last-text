"""The Battery's Last Text to Its Charger.

Writes one line of plain text — the phone battery's final message to the
charger it waited for all day — to /output/entry.txt.

The line (158 characters, one line, no trailing newline):

    all day i watched you charge the tablet, the earbuds, even the watch.
    i'm at 1% and this is my last text. going to 0% now, and i'm taking
    your alarms with me.

Deterministic: the text is a fixed literal, so every run writes identical bytes.
Before writing, the program checks the entry against the competition gate
itself (UTF-8, 1–200 characters, not only whitespace) and refuses to write an
invalid entry.
"""

import os

ENTRY = (
    "all day i watched you charge the tablet, the earbuds, even the watch. "
    "i'm at 1% and this is my last text. "
    "going to 0% now, and i'm taking your alarms with me."
)


def main() -> None:
    # Gate self-check (mirrors the competition gate): UTF-8, 1-200 chars,
    # not only whitespace, single line.
    ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
