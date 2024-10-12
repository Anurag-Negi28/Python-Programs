# Importing the necessary libraries
import tkinter as tk

# Creating the main window
root = tk.Tk()
root.title("Simple Messaging App")

# Creating a frame for displaying the messages
message_frame = tk.Frame(root)
message_frame.pack()

# Creating a text box for entering messages
message_box = tk.Entry(root)
message_box.pack()

# Function to send the message
def send_message():
    message = message_box.get()
    message_box.delete(0, tk.END)
    tk.Label(message_frame, text=message).pack()

# Creating a button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Running the main event loop
root.mainloop()
