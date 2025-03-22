import csv
import requests
from requests.exceptions import RequestException

csv_file_path = "Task 2 - Intern.csv"

try:
    with open(csv_file_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)

        # check if 'urls' column exists
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
                # errors and their codes
                error_code = "000"
                if isinstance(e, requests.exceptions.Timeout):
                    error_code = "408"  # Request timeout
                elif isinstance(e, requests.exceptions.TooManyRedirects):
                    error_code = "310"  # Too many redirects
                elif isinstance(e, requests.exceptions.SSLError):
                    error_code = "495"  # SSL error
                elif isinstance(e, requests.exceptions.ConnectionError):
                    error_code = "499"  # Connection error
                    
                print(f"({error_code}) {clean_url}")

except FileNotFoundError:
    print("Error: File 'Task 2 - Intern.csv' not found")
    exit()
