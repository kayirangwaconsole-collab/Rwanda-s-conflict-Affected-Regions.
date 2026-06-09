#!/usr/bin/env python3
"""
Simple CSV filter: keep only rows where the country is Rwanda.

Usage examples:
  python3 filter_rwanda.py data/input.csv
  python3 filter_rwanda.py data/input.csv -o rwanda_only.csv
  python3 filter_rwanda.py data/input.csv -c country

If you pass -c/--column, the script checks that column for an exact match (case-insensitive).
If you don't pass -c, the script keeps any row where any cell contains the word "Rwanda" (case-insensitive).
"""

import csv
import argparse


def main():
    parser = argparse.ArgumentParser(description="Keep only rows where Rwanda appears")
    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument("-o", "--output", default="rwanda_only.csv", help="Output CSV file path")
    parser.add_argument("-c", "--column", help="Column name to check for 'Rwanda' (optional)")
    args = parser.parse_args()

    # Read the CSV as dictionaries (header -> value)
    with open(args.input, newline="", encoding="utf-8") as inf:
        reader = csv.DictReader(inf)
        fieldnames = reader.fieldnames
        if not fieldnames:
            print("Input CSV has no header row. Please add a header or use a CSV with headers.")
            return

        kept = []
        check_col = args.column
        for row in reader:
            if check_col and check_col in row:
                val = (row.get(check_col) or "").strip().lower()
                if val == "rwanda":
                    kept.append(row)
            else:
                # If no column specified or column not found, check any cell for substring 'rwanda'
                found = False
                for v in row.values():
                    if v and "rwanda" in v.lower():
                        found = True
                        break
                if found:
                    kept.append(row)

    # Write filtered rows to output with same columns
    with open(args.output, "w", newline="", encoding="utf-8") as outf:
        writer = csv.DictWriter(outf, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kept)

    print(f"Saved {len(kept)} rows to '{args.output}'")


if __name__ == "__main__":
    main()
