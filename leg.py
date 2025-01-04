import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fungsi untuk mendapatkan output dari perintah tmate -F
def get_tmate_output():
    try:
        # Jalankan perintah `tmate -F` dan dapatkan outputnya
        result = subprocess.run(['tmate', '-F'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Fungsi untuk mengirim email
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Konfigurasi email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Hubungkan ke server SMTP dan kirim email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    # Dapatkan output dari `tmate -F`
    tmate_output = get_tmate_output()

    # Konfigurasi email
    sender_email = "tialivingston2020@unlock.web.id"  # Ganti dengan email Anda
    sender_password = "jizbnrheflslcgib"      # Ganti dengan password/email app key Anda
    recipient_email = "icadnewton@gmail.com"  # Ganti dengan email tujuan
    subject = "Tmate Output"
    body = f"Hasil output dari tmate -F:\n\n{tmate_output}"

    # Kirim email
    send_email(sender_email, sender_password, recipient_email, subject, body)
