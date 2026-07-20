# Task 3 - Unit Testing for Security Log Parser

## Overview

This project demonstrates unit testing for the Security Log Parser developed in Task 2. The objective is to verify that the parser behaves correctly under different conditions by automatically executing predefined test cases.

Unit testing improves software reliability by detecting errors before deployment and ensuring that future code modifications do not break existing functionality.

---

## Features

The test suite verifies:

- Presence of the parser script.
- Presence of the sample log file.
- Successful execution of the parser.
- Automatic generation of the CSV output file.
- Correct completion message after processing.

---

## Technologies Used

- Python 3
- unittest
- subprocess
- os

---

## Project Files

Task_03/
│
├── test_parser.py
└── README.md

---

## Running the Tests

Execute the following command:

```bash
python test_parser.py
```

---

## Expected Output

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.2s

OK
```

---

## Test Cases

| Test Case | Description |
|-----------|-------------|
| Test 1 | Verify sample log file exists |
| Test 2 | Verify parser script exists |
| Test 3 | Execute the parser successfully |
| Test 4 | Verify CSV output is generated |
| Test 5 | Verify processing summary is displayed |

---

## Learning Outcomes

This project demonstrates:

- Automated Software Testing
- Unit Testing using Python
- Software Quality Assurance
- Process Verification
- Automated Validation of Program Output