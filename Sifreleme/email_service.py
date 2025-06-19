import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

def send_email(encrypted_text):
    sender_email = "sender@gmail.com"  # Buraya kendi e-posta adresinizi yazın
    receiver_email = "receiver@gmail.com"  # Alıcının e-posta adresini yazın
    password = "password"  # Buraya kendi e-posta şifrenizi girin

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "Şifrelenmiş Mesaj"
        msg.attach(MIMEText(f"Şifreli Mesaj: {encrypted_text}", "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        messagebox.showinfo("Başarılı", "Şifreli mesaj başarıyla gönderildi!")
    except Exception as e:
        messagebox.showerror("Hata", f"E-posta gönderilirken bir hata oluştu: {e}")
        print(f"E-posta gönderilirken hata: {e}")
