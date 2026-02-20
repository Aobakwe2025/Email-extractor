# 🤖 Task 3 — Task Automation with Python Scripts
### SoftGrowTech Python Internship | Email Extractor

---

## 📖 About This Project

This script automates a real-world repetitive task: **extracting email addresses from
a text file**. Instead of manually scanning through a document looking for emails,
you simply run this script and it will:

1. Read any `.txt` file you point it to
2. Scan every line using a **regular expression (regex)**
3. Collect all valid email addresses found
4. Remove duplicates (case-insensitive — `Alice@Gmail.com` and `alice@gmail.com` count as one)
5. Sort them alphabetically
6. Save a clean, formatted report to `extracted_emails.txt`
7. Print a summary directly to the console

This is a genuine automation task — the same kind of script used in real data
processing pipelines, CRM data cleaning, and scraping contact lists.

---

## 📁 Project Structure

```
task3_email_extractor/
│
├── email_extractor.py      ← Main automation script
├── input.txt               ← Sample input file (edit or replace with your own)
├── extracted_emails.txt    ← Output file (auto-created when you run the script)
└── README.md               ← This file
```

**You only need to run one file:** `email_extractor.py`

The output file `extracted_emails.txt` is automatically generated — you don't need
to create it manually.

---

## ⚙️ Requirements

| Requirement | Version |
|-------------|---------|
| Python      | 3.6+    |
| Libraries   | `re`, `os`, `sys`, `datetime` (all built-in — no pip install needed) |

No third-party packages are required. Everything used is part of Python's
standard library.

---

## 🚀 How to Run

### Step 1 — Verify Python is installed
```bash
python --version
# or
python3 --version
```
Expected output: `Python 3.x.x`

---

### Step 2 — Place your input file in the project folder

Make sure a file called **`input.txt`** exists in the **same folder** as `email_extractor.py`.

A ready-to-use sample `input.txt` is already included. You can:
- Use it as-is to test the script
- Replace it with your own `.txt` file (just name it `input.txt`)
- Or edit the `INPUT_FILE` variable at the top of `email_extractor.py` to point to
  any file path you like

---

### Step 3 — Navigate to the project folder
```bash
cd path/to/task3_email_extractor
```
Windows example:
```
cd C:\Users\YourName\Desktop\task3_email_extractor
```
Mac/Linux example:
```
cd ~/Desktop/task3_email_extractor
```

---

### Step 4 — Run the script
```bash
python email_extractor.py
# or
python3 email_extractor.py
```

---

## 📺 Sample Console Output

```
=============================================
   📂  Email Extractor — Task Automation
=============================================

  ✅  Read input file : 'input.txt'  (1,432 characters)
  🔍  Scanning complete — 13 unique email(s) found.

─────────────────────────────────────────────
  📧  Emails found : 13
─────────────────────────────────────────────
    1.  alice.johnson@gmail.com
    2.  bob.patel99@yahoo.com
    3.  carla_mendes@outlook.com
    4.  d.kim+intern@hotmail.com
    5.  eva.nkosi@university.ac.za
    ...
─────────────────────────────────────────────

  ✅  Results saved to : 'extracted_emails.txt'

  ✔   Done! Open 'extracted_emails.txt' to see the full results.
```

---

## 📄 Sample Output File (`extracted_emails.txt`)

```
=======================================================
  EXTRACTED EMAIL ADDRESSES
  Generated : 2025-06-15 14:32:07
  Total     : 13 unique email(s) found
=======================================================

    1.  alice.johnson@gmail.com
    2.  bob.patel99@yahoo.com
    3.  carla_mendes@outlook.com
    ...

=======================================================
```

---

## 🔑 Key Concepts Demonstrated

| Concept | Where Used |
|---------|-----------|
| `re` module | Regex pattern to match email addresses |
| `os.path.exists()` | Checking if the input file exists before reading |
| `sys.exit()` | Graceful error exit if file is missing |
| `open()` + `read()` / `write()` | File reading and writing |
| `set` | Removing duplicate emails |
| `sorted()` | Alphabetical ordering of results |
| String `.lower()` | Case-insensitive deduplication |
| `datetime` | Timestamping the output report |
| Functions | Each step isolated into its own clean function |

---

## 🧠 How the Regex Works

```python
r"[a-zA-Z0-9_.+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z]{2,7}"
```

| Part | Matches |
|------|---------|
| `[a-zA-Z0-9_.+\-]+` | Local part — letters, digits, dots, underscores, `+`, `-` |
| `@` | The literal `@` symbol |
| `[a-zA-Z0-9\-]+` | Domain name — letters, digits, hyphens |
| `\.` | A literal dot |
| `[a-zA-Z]{2,7}` | Top-level domain — 2 to 7 letters (`.com`, `.co.za`, `.museum`) |

Malformed addresses like `@missinglocal.com` or `missingdomain@` are correctly
**ignored** because they don't match the full pattern.

---

## 🛠 Customisation

**Use a different input file:**
Edit the top of `email_extractor.py`:
```python
INPUT_FILE  = "my_contacts.txt"   # ← change this
OUTPUT_FILE = "results.txt"        # ← and/or this
```

**Use an absolute path:**
```python
INPUT_FILE  = r"C:\Users\YourName\Documents\contacts.txt"
OUTPUT_FILE = r"C:\Users\YourName\Documents\emails_found.txt"
```

---

## 👤 Author

Developed as part of the **SoftGrowTech Python Programming Internship — Task 3**.
