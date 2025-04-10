# T386128--url-status-checker-Submission

A Python script that checks and reports HTTP status codes for URLs listed in a CSV file. This project was created as part of the Outreachy contribution period (Round 30) for the task "Addressing the new Lusophone technological wishlist proposals" (T386128).

## Project Overview

This script reads URLs from a CSV file, checks their HTTP status codes, and outputs the results both to the console and to a new CSV file. It handles various edge cases including invalid URLs and connection errors.

### Features

- Reads URLs from a CSV file
- Validates URL format before making requests
- Handles network errors gracefully
- Outputs results in a user-friendly format: (STATUS_CODE) URL
- Creates a new CSV file with status codes for further analysis
- Supports UTF-8 encoding for international URLs

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/neha222222/T386128--url-status-checker-Submission.git
cd T386128--url-status-checker-Submission
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

1. Place your input CSV file (containing URLs) in the project directory.
2. Run the script:
```bash
python url_status_checker.py
```

The script will:
- Read URLs from `Task 2 - Intern.csv`
- Print status codes to the console
- Generate `updated_csv_with_status.csv` with the results

### Input Format
The input CSV file should have URLs in the first column. The header row will be ignored.

### Output Format
Console output:
I have noticed these most frequent responses.
(200) https://example.com
(404) https://example.com/not-found
(ERROR) https://invalid-url

### What i learnt from while completing this task 
1. Working with URLs isn't as simple as it seems! 🌐
I discovered that URLs can be tricky - some might be invalid, others might time out, and some might redirect you somewhere else. It was fun figuring out how to handle all these different cases in my code.

2. CSV Files are pretty handy 📊
Before this, I mostly worked with simple text files. Learning to work with CSV files was neat - they're like spreadsheets in code! I learned how to read from them and create new ones with the results.

3. Error Handling is super important ⚠️
The biggest "aha!" moment was realizing that a lot can go wrong when dealing with web requests. Bad URLs, slow servers, no internet - my code needed to handle all of these gracefully. It taught me that good code isn't just about making things work, it's about handling things when they don't!
