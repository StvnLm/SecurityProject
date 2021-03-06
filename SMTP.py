from email.headerregistry import Address
from email.message import EmailMessage
import smtplib

# GMAIL credentials
email_address = "Testmail@gmail.com"
email_password = "PLPLplpl2"

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
  HTML TEST MESSAGE
</p>
"""

if __name__ == '__main__':

    account_List = [["Steven Lam1", "ca.stevenlam", "gmail.com"], ["Steven Lam2", "stevenlam5796", "gmail.com"], ["Steven Lam3", "SheridanCollegeContests", "gmail.com"]]
    for n in range(len(account_List)):
        # Recipient
        recipient = (Address(display_name=account_List[n][0], username=account_List[n][1], domain=account_List[n][2]))
        msg = create_email_message(from_add=email_address, to_add=recipient, subject="TEST SUBJECT!",
                                   plaintext_msg="plaintext_test", html_msg=HTML_MESSAGE)

        with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
                smtp_server.ehlo()
                smtp_server.starttls()
                smtp_server.login(email_address, email_password)
                smtp_server.send_message(msg)
                print("SENT")
