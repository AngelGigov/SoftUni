class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails_as_objects = []

information = input()
while information != "Stop":
    sender, receiver, content = information.split()
    email_info = Email(sender, receiver, content)
    emails_as_objects.append(email_info)
    information = input()

indexes = [int(x) for x in input().split(', ')]

for index in indexes:
    emails_as_objects[index].send()

for current_email in emails_as_objects:
    print(current_email.get_info())
