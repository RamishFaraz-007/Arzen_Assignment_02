# Arzen Internship Assignment 02

## Author

**Name:** Ramish Faraz

**Program:** BS Computer Engineering

**Assignment:** Internship Assignment 02

---

# Project Overview

This repository contains the solutions for Internship Assignment 02. The assignment focuses on cybersecurity concepts, Python programming, security log processing, and software testing. The project demonstrates the practical application of automation techniques commonly used in Security Operations Centers (SOC) to improve efficiency and reduce manual effort.

---

# Repository Contents

- Task 1 – Comparison of Manual Security Work, Simple Scripts, and SOAR
- Task 2 – Python Security Log Parser
- Task 3 – Unit Testing for the Security Log Parser

---

# Task 1 – Security Automation Comparison

## Objective

To compare different approaches used for performing cybersecurity tasks and incident response.

### Topics Covered

- Manual Security Operations
- Script-Based Automation
- Security Orchestration, Automation and Response (SOAR)

### Key Learning Outcomes

- Understanding the limitations of manual security operations.
- Learning how automation improves efficiency.
- Understanding the role of SOAR platforms in enterprise cybersecurity.
- Comparing speed, scalability, accuracy, and cost of different approaches.

---

# Task 2 – Python Security Log Parser

## Objective

Develop a Python application that reads raw security log files, validates each log entry, extracts useful information, and exports the processed data into a CSV file.

## Features

- Reads security log files.
- Parses log entries.
- Validates timestamp format.
- Detects malformed log entries.
- Skips invalid records.
- Generates a structured CSV report.
- Displays a processing summary.
- Supports Dry Run mode.

## Technologies Used

- Python 3
- argparse
- csv
- datetime
- os

## Files

- log_parser.py
- sample_logs.txt
- output_parsed.csv

### Run

```bash
python log_parser.py sample_logs.txt
```

---

# Task 3 – Unit Testing

## Objective

Develop automated tests to verify the functionality of the Security Log Parser created in Task 2.

## Test Cases

- Verify parser file exists.
- Verify sample log file exists.
- Verify successful parser execution.
- Verify CSV output generation.
- Verify processing completion message.

## Technologies Used

- Python 3
- unittest
- subprocess
- os

### Run

```bash
python test_parser.py
```

---

# Skills Demonstrated

- Cybersecurity Fundamentals
- Security Automation
- Python Programming
- File Handling
- Command Line Applications
- Exception Handling
- CSV Processing
- Software Testing
- Unit Testing
- Automation Concepts
- Documentation

---

# Expected Output

## Task 2

```
Processing Complete
---------------------------
Total Lines : 10
Parsed      : 10
Skipped     : 0
Output File : output_parsed.csv
```

## Task 3

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.2s

OK
```

---

# Conclusion

This assignment demonstrates the implementation of basic cybersecurity automation using Python. It covers the comparison of manual security operations with automated solutions, the development of a security log parser, and the use of automated unit testing to verify software functionality. Together, these tasks showcase fundamental skills in Python programming, security operations, automation, and software quality assurance.
