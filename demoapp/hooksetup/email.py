import frappe

# Hook 1: change sender
def get_sender_details():
    return "John Doe", "johndoe@example.com"

# Hook 2: override email sending
def send(self, sender, recipient, msg):
    print("Sending email to", recipient)
    self.update_status("Sent")  # mark email as sent
