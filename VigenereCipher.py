# Fungsi untuk mengenkripsi teks dengan kunci
def encrypt(plain_text, key):
    cipher_text = ""
    key_index = 0
    for char in plain_text:
        # Jika karakter bukan huruf, langsung tambahkan ke hasil enkripsi
        if not char.isalpha():
            cipher_text += char
        else:
            # Konversi huruf ke angka 0-25
            plain_num = ord(char.lower()) - ord('a')
            key_num = ord(key[key_index % len(key)].lower()) - ord('a')
            cipher_num = (plain_num + key_num) % 26
            # Konversi angka ke huruf
            cipher_text += chr(cipher_num + ord('a'))
            key_index += 1
    return cipher_text

# Fungsi untuk mendekripsi teks dengan kunci


def decrypt(cipher_text, key):
    plain_text = ""
    key_index = 0
    for char in cipher_text:
        # Jika karakter bukan huruf, langsung tambahkan ke hasil dekripsi
        if not char.isalpha():
            plain_text += char
        else:
            # Konversi huruf ke angka 0-25
            cipher_num = ord(char.lower()) - ord('a')
            key_num = ord(key[key_index % len(key)].lower()) - ord('a')
            plain_num = (cipher_num - key_num) % 26
            # Konversi angka ke huruf
            plain_text += chr(plain_num + ord('a'))
            key_index += 1
    return plain_text


# Contoh penggunaan
plain_text = "Ini adalah contoh teks yang akan dienkripsi."
key = "269"
cipher_text = encrypt(plain_text, key)
print("Teks asli: " + plain_text)
print("Kunci: " + key)
print("Teks yang dienkripsi: " + cipher_text)
plain_text = decrypt(cipher_text, key)
print("Teks yang didekripsi: " + plain_text)
