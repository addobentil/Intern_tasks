import csv
import requests
from requests.exceptions import RequestException

csv_file_path = "Task 2 - Intern.csv"

try:
    with open(csv_file_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)

        # Check if 'urls' column exists
        if 'urls' not in reader.fieldnames:
            print("Error: Column 'urls' not found in CSV")
            exit()

        for row in reader:
            clean_url = row.get('urls', '').strip()
            if not clean_url:
                continue  # Skip empty rows

            try:
                response = requests.head(clean_url, allow_redirects=True, timeout=10)
                print(f"({response.status_code}) {clean_url}")

            except RequestException as e:
                # Print descriptive error messages instead of codes
                if isinstance(e, requests.exceptions.Timeout):
                    print(f"Timeout error: {clean_url}")
                elif isinstance(e, requests.exceptions.TooManyRedirects):
                    print(f"Too many redirects: {clean_url}")
                elif isinstance(e, requests.exceptions.SSLError):
                    print(f"SSL error: {clean_url}")
                elif isinstance(e, requests.exceptions.ConnectionError):
                    print(f"Connection error: {clean_url}")
                else:
                    print(f"Unknown error: {clean_url}")
            print()  # Adds an empty line after each URL's result

except FileNotFoundError:
    print("Error: File 'Task 2 - Intern.csv' not found")
    exit()