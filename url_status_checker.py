import requests
import csv
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception as e:
        print(f"Error validating URL {url}: {str(e)}")
        return False

def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return "ERROR"

def main():
    try:
        with open('Task 2 - Intern.csv', 'r', encoding='utf-8') as input_file, \
             open('updated_csv_with_status.csv', 'w', newline='', encoding='utf-8') as output_file:
            
            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(['URL', 'Status'])
            for row in csv_reader:
                if row: 
                    url = row[0].strip()
                    if is_valid_url(url):
                        status_code = check_url_status(url)
                        print(f"({status_code}) {url}")
                        csv_writer.writerow([url, status_code])
                    else:
                        print(f"(INVALID) {url}")
                        csv_writer.writerow([url, 'INVALID'])
                        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
