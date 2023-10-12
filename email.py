# Compulsory Task 1
# Re-submitted for review after necessary corrections

# Create Email class
class Email:
    # Initialise the instance variables for email class
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    # Define a method to mark email as read
    def mark_as_read(self):
        self.has_been_read = True

    # Define a method to mark email as spam
    def mark_as_spam(self):
        self.is_spam = True


# Create Inbox class
class Inbox:
    # Initialise the instance variable for Inbox class
    def __init__(self):
        self.inbox_list = []

    # Define a method to add email in the inbox list
    def add_email(self, from_address, subject_line, email_contents):
        email = Email(from_address, subject_line, email_contents)
        self.inbox_list.append(email)

    # Define a method to list emails from a specific sender
    def list_messages_from_sender(self, sender_address):
        emails = [e for e in self.inbox_list if e.from_address == sender_address]
        if not emails:
            return f"No emails from {sender_address}"
        else:
            output = f"Emails from {sender_address}:\n"
            for count, email in enumerate(emails):
                output += f"{count} {email.subject_line}"
            return output

    # Define a method to get email from a specific sender and at a specific index
    def get_email(self, sender_address, index):
        emails = [e for e in self.inbox_list if e.from_address == sender_address]
        if not emails:
            return None
        elif index < 0 or index >= len(emails):
            return None
        email = emails[index]
        email.has_been_read = True
        return email

    # Define a method to mark email as spam
    def mark_as_spam(self, sender_address, index):
        emails = [e for e in self.inbox_list if e.from_address == sender_address]
        if not emails:
            return f"No emails from {sender_address}"
        elif index < 0 or index >= len(emails):
            return f"Invalid index!"
        email = emails[index]
        email.is_spam = True
        return "Email has been marked as spam."

    # Define a method to get the unread emails
    def get_unread_email(self):
        unread_emails = [e for e in self.inbox_list if not e.has_been_read]
        if not unread_emails:
            return "No unread emails"
        else:
            output = ""
            for email in unread_emails:
                output += email.subject_line + "\n"
            return output

    # Define a method to get the emails which are marked as spam
    def get_spam_email(self):
        spam_emails = [e for e in self.inbox_list if e.is_spam]
        if not spam_emails:
            return "No spam emails"
        else:
            output = ""
            for email in spam_emails:
                output += email.subject_line + "\n"
            return output

    # Define a method to delete emails from specific sender and at a specif index
    def delete(self, sender_address, index):
        emails = [e for e in self.inbox_list if e.from_address == sender_address]
        if not emails:
            return f"No emails from {sender_address}"
        elif index < 0 or index >= len(emails):
            return f"Invalid index!"
        email = emails[index]
        self.inbox_list.remove(email)
        return "Email deleted!"


usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
: '''

# An Email Simulation

inbox = Inbox()

user_choice = ""

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")
        # Now add the email to the Inbox
        inbox.add_email(sender_address, subject_line, contents)
        # Print a success message
        print("Email has been added to inbox.")

        pass
    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")
        # Now list all emails from this sender
        output = inbox.list_messages_from_sender(sender_address)
        print(output)

        pass
    elif user_choice == "r":
        # Read an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Step 2: show all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))
        # Step 4: display the email
        email_object = inbox.get_email(sender_address, email_index)
        print(email_object.email_contents)


        pass
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Step 2: show all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be marked as spam\n:"))
        # Step 4: mark the email as spam
        inbox.mark_as_spam(sender_address, email_index)
        # Step 5: print a success message
        print("Email has been marked as spam")

        pass
    elif user_choice == "gu":
        # List all unread emails
        unread_email_list = inbox.get_unread_email()
        print(unread_email_list)
        pass

    elif user_choice == "gs":
        # List all spam emails
        spam_email_list = inbox.get_spam_email()
        print(spam_email_list)
        pass

    elif user_choice == "e":
        print("Goodbye")
        break

    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Step 2: show all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be deleted\n:"))
        # Step 4: delete the email
        inbox.delete(sender_address, email_index)
        # Step 5: print a success message
        print("Email has been deleted")
        pass
    else:
        print("Oops - incorrect input")
