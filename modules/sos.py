import smtplib

def send_sos_alert():
    # Example for sending an email SOS alert (this should be replaced with actual implementation)
    sender_email = "youremail@gmail.com"
    receiver_email = "trustedcontact@gmail.com"
    password = "yourpassword"
    
    message = """\
    Subject: SOS Alert

    I'm in danger! Please help. Here's my location: https://maps.google.com/?q=lat,lon"""
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("SOS alert sent!")
    except Exception as e:
        print(f"Failed to send SOS: {e}")
