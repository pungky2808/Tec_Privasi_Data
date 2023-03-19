import string

# Membuat dictionary untuk menghubungkan huruf-huruf pada kunci


def generate_key(key):
    alphabet = string.ascii_uppercase
    key = key.upper().replace(" ", "")
    key += alphabet

    # Menghapus huruf-huruf yang duplikat pada kunci
    unique_chars = []
    for char in key:
        if char not in unique_chars:
            unique_chars.append(char)

    # Menghubungkan huruf-huruf pada kunci ke huruf-huruf pada alfabet
    key_dict = {}
    for i in range(len(alphabet)):
        key_dict[alphabet[i]] = unique_chars[i]

    return key_dict

# Fungsi enkripsi


def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    key_dict = generate_key(key)

    # Mengganti setiap huruf pada plaintext menggunakan dictionary kunci
    for char in plaintext:
        ciphertext += key_dict[char]

    return ciphertext

# Fungsi dekripsi


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    key_dict = generate_key(key)

    # Mengganti setiap huruf pada ciphertext menggunakan dictionary kunci yang terbalik
    reverse_key_dict = dict((value, key) for key, value in key_dict.items())
    for char in ciphertext:
        plaintext += reverse_key_dict[char]

    return plaintext


# Contoh penggunaan
key = "KUNCI"
plaintext = "INI ADALAH CONTOH"
ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
