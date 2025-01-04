import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

# Fungsi untuk menjalankan perintah nohup tmate -F di subprocess (background)
def run_tmate_command():
    try:
        print("Running nohup tmate -F command in background...")
        # Jalankan tmate -F dalam subprocess di background dan pastikan output diarahkan ke file nohup.out
        with open('nohup.out', 'w') as nohup_file:
            process = subprocess.Popen(['nohup', 'tmate', '-F'], stdout=nohup_file, stderr=subprocess.PIPE, text=True)
        print("tmate command is running in the background.")
        return process
    except Exception as e:
        print(f"Exception occurred while running tmate command: {str(e)}")
        return None

# Fungsi untuk mendapatkan output dari file nohup.out
def get_nohup_output():
    try:
        print("Reading nohup.out file...")
        # Tunggu beberapa detik agar tmate menulis ke nohup.out
        time.sleep(10)  # Sesuaikan waktu tunggu jika perlu
        if not os.path.exists('nohup.out'):
            raise FileNotFoundError("nohup.out file not found.")
        with open('nohup.out', 'r') as file:
            output = file.read()
        print("Output from nohup.out retrieved successfully.")
        return output
    except Exception as e:
        print(f"Exception occurred while reading nohup.out: {str(e)}")
        return f"Exception occurred: {str(e)}"

# Fungsi untuk mengirim email
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        print("Preparing email...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        print("Connecting to SMTP server...")
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Jalankan perintah tmate -F di background
    print("Starting tmate command...")
    process = run_tmate_command()

    # Tunggu beberapa detik untuk memastikan output dapat ditulis ke nohup.out
    print("Waiting for tmate output...")
    time.sleep(15)  # Tunggu lebih lama untuk memberi waktu agar tmate menulis ke nohup.out

    # Dapatkan output dari file nohup.out
    print("Getting nohup.out output...")
    nohup_output = get_nohup_output()

    # Konfigurasi email
    sender_email = "wesleyarmstrong2020@unlock.web.id"  # Ganti dengan email Anda
    sender_password = "afgjkizfczkcblno"  # Ganti dengan password/email app key Anda
    recipient_email = "icadnewton@gmail.com"  # Ganti dengan email tujuan
    subject = "Nohup Output"
    body = f"koneksi ssh anda paduka redhat account kailahulsey5498+fzxms@outlook.com:\n\n{nohup_output}"

    # Kirim email dengan hasil output nohup.out
    print("Sending email...")
    send_email(sender_email, sender_password, recipient_email, subject, body)

    # Pastikan proses tmate selesai jika diperlukan
    process.wait()
