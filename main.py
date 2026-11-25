import os
import sys

AWAY = "I'm away until Monday;"
URGENT = "for anything urgent, please panic quietly and try again then."
LINE = AWAY + " " + URGENT

def entry_line():
    return LINE

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        sys.exit("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
