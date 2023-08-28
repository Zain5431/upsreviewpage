import tkinter as tk
from tkinter import filedialog
import smtplib
import ssl
from email.message import EmailMessage

def upload_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_entry.delete('1.0', tk.END)
            text_entry.insert('1.0', text)

def send_text():
    text = text_entry.get('1.0', tk.END)
    # Add your sending logic here (e.g., sending the text to a server or performing an action)
    print("Sending Text:")
    
    # Your email sending logic here
    email_sender = 'zainbusiness5431@gmail.com'
    email_password = 'umegtkfekcbvfnlt'

    # Replace this list with the actual email addresses
    file = 'email_list.txt'
    email_receiver = []
    with open(file, "r") as file:
        for line in file:
            email_receiver.append(line.strip())


    # Set the subject and body of the email
    subject = '[IMPORTANT] Your Baby Isnt Safe'
    body = """
    ...  # Your email body here

    Stay safe and keep spreading the word!
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

# Create the main window
root = tk.Tk()
root.title("Text Upload and Send")

# Create and place widgets
upload_button = tk.Button(root, text="Upload Text", command=upload_text)
upload_button.pack(pady=10)

text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_text)
send_button.pack()

# Start the main event loop
root.mainloop()
