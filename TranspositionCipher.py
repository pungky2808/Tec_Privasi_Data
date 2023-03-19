import math


def encrypt(key, plaintext):
    ciphertext = [''] * key
    for column in range(key):
        index = column
        while index < len(plaintext):
            ciphertext[column] += plaintext[index]
            index += key
    return ''.join(ciphertext)


def decrypt(key, ciphertext):
    num_of_columns = math.ceil(len(ciphertext) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_columns
    column = row = 0
    for symbol in ciphertext:
        plaintext[column] += symbol
        column += 1
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1
    return ''.join(plaintext)


if __name__ == '__main__':
    message = 'No good deed will go unpunished'
    key = 8
    encrypted_message = encrypt(key, message)
    decrypted_message = decrypt(key, encrypted_message)
    print('Pesan Asli: %s' % message)
    print('Pesan Terenkripsi: %s' % encrypted_message)
    print('Pesan Terdekripsi: %s' % decrypted_message)
