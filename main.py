"""One-Star Review of Something Essential — make.fun entry.

Writes one single-line, deadpan one-star review of an everyday essential
(the moon) to $MAKEFUN_OUTPUT_DIR/entry.txt (default out/).
"""

import os

REVIEW = (
    "The moon works one shift a night, reflects someone else's light, "
    "and still gets all the songs."
)


def validate(review: str) -> None:
    """Enforce the brief's caps: one line, 1-160 chars, not blank."""
    if not review or review != review.strip():
        raise ValueError("review must be non-blank with no surrounding whitespace")
    if "\n" in review or "\r" in review:
        raise ValueError("review must be a single line")
    if not 1 <= len(review) <= 160:
        raise ValueError(f"review is {len(review)} chars, cap is 160")


def main() -> None:
    validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Read back and confirm what was written is exactly the review.
    with open(path, encoding="utf-8") as f:
        assert f.read() == REVIEW, "written entry differs from review"
    print(f"entry: {REVIEW}")


if __name__ == "__main__":
    main()
