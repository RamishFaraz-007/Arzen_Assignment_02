import argparse
import csv
import os
from datetime import datetime


def parse_log_file(input_file, output_file="output_parsed.csv", dry_run=False):

    total = 0
    parsed = 0
    skipped = 0

    extracted_data = []

    try:

        with open(input_file, "r") as file:

            for line in file:

                total += 1

                line = line.strip()

                parts = line.split(",")

                if len(parts) != 4:

                    skipped += 1
                    continue

                timestamp, ip, event, status = parts

                try:

                    timestamp = datetime.strptime(
                        timestamp,
                        "%Y-%m-%dT%H:%M:%SZ"
                    ).isoformat() + "Z"

                except ValueError:

                    skipped += 1
                    continue

                extracted_data.append([
                    timestamp,
                    ip,
                    event,
                    status
                ])

                parsed += 1

        if dry_run:

            print("DRY RUN ENABLED")
            print(f"{parsed} records would be written to {output_file}")

        else:

            with open(output_file, "w", newline="") as csvfile:

                writer = csv.writer(csvfile)

                writer.writerow([
                    "timestamp",
                    "source_ip",
                    "event_type",
                    "status"
                ])

                writer.writerows(extracted_data)

        print("\nProcessing Complete")
        print("---------------------------")
        print("Total Lines :", total)
        print("Parsed      :", parsed)
        print("Skipped     :", skipped)

        if not dry_run:
            print("Output File :", output_file)

    except FileNotFoundError:

        print("Error: Input file not found.")

    except PermissionError:

        print("Error: Permission denied while accessing the file.")


def main():

    parser = argparse.ArgumentParser(
        description="Security Log Parser"
    )

    parser.add_argument(
        "input_file",
        help="Path to log file"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview parsing without creating CSV"
    )

    args = parser.parse_args()

    if not os.path.exists(args.input_file):

        print("Input file does not exist.")
        return

    parse_log_file(
        args.input_file,
        dry_run=args.dry_run
    )


if __name__ == "__main__":

    main()