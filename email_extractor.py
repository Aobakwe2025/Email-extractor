"""
╔══════════════════════════════════════════════════════════════╗
║         TASK AUTOMATION — Email Extractor Script             ║
║              SoftGrowTech Internship — Task 3                ║
╚══════════════════════════════════════════════════════════════╝

Automatically scans a .txt file, extracts all valid email
addresses using a regular expression, removes duplicates,
sorts them alphabetically, and saves the results to a new file.

Key Concepts: os, re, file handling
"""

import re
import os
import sys
from datetime import datetime


# ─────────────────────────────────────────────
#  CONFIGURATION  (edit these paths if needed)
# ─────────────────────────────────────────────

INPUT_FILE  = "input.txt"          # Source file to scan for emails
OUTPUT_FILE = "extracted_emails.txt"  # Where results are saved


# ─────────────────────────────────────────────
#  REGEX PATTERN
# ─────────────────────────────────────────────

# This pattern covers the vast majority of real-world email addresses:
#   • local part: letters, digits, dots, underscores, plus signs, hyphens
#   • @ symbol
#   • domain: letters, digits, dots, hyphens
#   • TLD: 2–7 letters (e.g. .com, .co.za, .museum)
EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9_.+\-]+@[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*\.[a-zA-Z]{2,7}"
)


# ─────────────────────────────────────────────
#  CORE FUNCTIONS
# ─────────────────────────────────────────────

def read_input_file(filepath):
    """
    Read and return the full text content of a file.
    Exits with a helpful message if the file does not exist.
    """
    if not os.path.exists(filepath):
        print(f"\n  ❌  ERROR: Input file not found → '{filepath}'")
        print("  Please make sure 'input.txt' exists in the same folder as this script.\n")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"  ✅  Read input file : '{filepath}'  ({len(content):,} characters)")
    return content


def extract_emails(text):
    """
    Find all email addresses in the given text using regex.
    Returns a sorted list of unique (case-insensitive) emails.
    """
    found = EMAIL_PATTERN.findall(text)

    # Normalise to lowercase and remove duplicates using a set
    unique_emails = sorted(set(email.lower() for email in found))
    return unique_emails


def save_emails(emails, filepath):
    """
    Write the list of emails to the output file.
    Includes a header with timestamp and count.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 55 + "\n")
        f.write("  EXTRACTED EMAIL ADDRESSES\n")
        f.write(f"  Generated : {timestamp}\n")
        f.write(f"  Total     : {len(emails)} unique email(s) found\n")
        f.write("=" * 55 + "\n\n")

        if emails:
            for i, email in enumerate(emails, start=1):
                f.write(f"  {i:>3}.  {email}\n")
        else:
            f.write("  No email addresses were found in the input file.\n")

        f.write("\n" + "=" * 55 + "\n")

    print(f"  ✅  Results saved to : '{filepath}'")


def print_summary(emails):
    """Print a summary of results to the console."""
    print("\n" + "─" * 45)
    print(f"  📧  Emails found : {len(emails)}")
    print("─" * 45)

    if emails:
        for i, email in enumerate(emails, start=1):
            print(f"  {i:>3}.  {email}")
    else:
        print("  No emails were found in the input file.")

    print("─" * 45 + "\n")


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

def main():
    print("\n" + "=" * 45)
    print("   📂  Email Extractor — Task Automation")
    print("=" * 45 + "\n")

    # Step 1: Read the source file
    text = read_input_file(INPUT_FILE)

    # Step 2: Extract emails using regex
    emails = extract_emails(text)
    print(f"  🔍  Scanning complete — {len(emails)} unique email(s) found.\n")

    # Step 3: Print summary to the console
    print_summary(emails)

    # Step 4: Save results to the output file
    save_emails(emails, OUTPUT_FILE)

    print(f"\n  ✔   Done! Open '{OUTPUT_FILE}' to see the full results.\n")


if __name__ == "__main__":
    main()
