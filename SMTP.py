from email.headerregistry import Address
from email.message import EmailMessage
import smtplib

# GMAIL credentials
email_address = "mikelovesoreos@gmail.com"
email_password = "telecomS144"

# Recipient
recipient = (Address(display_name="Steven Lam", username="ca.stevenlam", domain="gmail.com"))

def create_email_message(from_add, to_add, subject, plaintext_msg, html_msg=None):
    msg = EmailMessage()
    msg["From"] = from_add
    msg["To"] = to_add
    msg["Subject"] = subject
    msg.set_content(plaintext_msg)
    if html_msg is not None:
        msg.add_alternative(html_msg, subtype="html")
    return msg

HTML_MESSAGE = """\
<p>
  HTML Version!
</p>

<p>
  Link to <a href="reddit.com">REDDIT</a>!
</p>
"""

if __name__ == '__main__':
    msg = create_email_message(from_add=email_address, to_add=recipient, subject="Hello world",
                               plaintext_msg="plaintext_test", html_msg=HTML_MESSAGE)

    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(email_address, email_password)
            smtp_server.send_message(msg)
            print("SENT")
