print("HELLO WORLD!")

x = 2 + 2
print(x)



SENDGRID_API_KEY = "todo"
SENDER_ADDRESS = "example@gmail.com"


def send_email(recipient_address=SENDER_ADDRESS, subject="[Shopping Cart App] Testing 123", html_content="<p>Hello World</p>"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)
    print("TODO...")


send_email()