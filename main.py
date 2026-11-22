"""Write the relaxing entry text to entry.txt.

The program writes one fixed text: a person lying on the grass at
dusk, held by the ground. It is deterministic, uses only the
standard library, and needs no network.
"""

import os


def main():
    text = "At dusk she lies back in the grass and the ground takes her whole weight. The grass is cool against her back, the crickets begin, and the sky above her deepens one slow shade at a time. The ground does not move; it holds."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
