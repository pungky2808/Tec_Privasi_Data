from tkinter import *


def encrypt(key, message):
    cipher_text = [''] * key

    for col in range(key):
        position = col

        while position < len(message):
            cipher_text[col] += message[position]
            position += key

    return ''.join(cipher_text)


def decrypt(key, message):
    num_of_cols = int(len(message) / key)
    plain_text = [''] * num_of_cols

    for col in range(num_of_cols):
        position = col

        for row in range(key):
            plain_text[col] += message[position]
            position += num_of_cols

    return ''.join(plain_text)


def submit():
    message = input_box.get("1.0", "end-1c")
    key = int(key_box.get())

    if encrypt_radio.get() == 1:
        result_text = encrypt(key, message)
    elif decrypt_radio.get() == 1:
        result_text = decrypt(key, message)

    output_box.delete("1.0", END)
    output_box.insert("1.0", result_text)


root = Tk()
root.title("Transposition Cipher")

# Key input
key_label = Label(root, text="Key: ")
key_label.grid(row=0, column=0, sticky=W)

key_box = Entry(root)
key_box.grid(row=0, column=1, sticky=W)

# Message input
message_label = Label(root, text="Message: ")
message_label.grid(row=1, column=0, sticky=W)

input_box = Text(root, height=10, width=50)
input_box.grid(row=1, column=1, sticky=W)

# Radio buttons for encrypt/decrypt
encrypt_radio = IntVar()
decrypt_radio = IntVar()

encrypt_radio_button = Radiobutton(
    root, text="Encrypt", variable=encrypt_radio, value=1)
encrypt_radio_button.grid(row=2, column=0, sticky=W)

decrypt_radio_button = Radiobutton(
    root, text="Decrypt", variable=decrypt_radio, value=1)
decrypt_radio_button.grid(row=2, column=1, sticky=W)

# Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, sticky=W)

# Output box
output_label = Label(root, text="Result: ")
output_label.grid(row=4, column=0, sticky=W)

output_box = Text(root, height=10, width=50)
output_box.grid(row=4, column=1, sticky=W)

root.mainloop()
