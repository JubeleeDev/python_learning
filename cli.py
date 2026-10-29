import argparse
import sys
from pathlib import Path

from stats.report import get_report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="CLI Word Counter",
        description="Count number of lines and words")

    parser.add_argument("filename")
    parser.add_argument("-o", "--output-file")

    args = parser.parse_args()
    path = Path(args.filename)

    if path.is_dir():
        print("chosen filename path is directory", file=sys.stderr)
        sys.exit(1)
    
    if not path.is_file():
        print("file by chosen filename path is not found", file=sys.stderr)
        sys.exit(1)

    report = get_report(args.filename)

    if args.output_file is not None:
        output_path = Path(args.output_file)

        if output_path.is_dir():
            print("chosen output path is directory", file=sys.stderr)
            sys.exit(1)

        try:
            with open(args.output_file, "w", encoding="utf-8") as f:
                print(report, file=f)
        except PermissionError:
            print(f"permission error to file {args.output_file}", file=sys.stderr)
            sys.exit(1)
        except FileNotFoundError:
            print(f"parent directory of path ({args.output_file}) is not found", file=sys.stderr)
            sys.exit(1)
        except OSError as e:
            print(f"system error while writing file: {e.strerror}", file=sys.stderr)
            sys.exit(1)

        print("file with report was successfully written")


    else:
        print(report)

        