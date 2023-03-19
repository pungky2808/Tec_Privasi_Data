# Fungsi untuk mengenkripsi pesan dengan shift cipher
def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        # Mengabaikan karakter selain huruf
        if not char.isalpha():
            cipher_text += char
            continue
        # Mengubah huruf ke dalam bentuk angka (A=0, B=1, dst.)
        ascii_offset = 65 if char.isupper() else 97
        char_index = ord(char) - ascii_offset
        # Menghitung index huruf setelah di-shift
        shifted_index = (char_index + key) % 26
        # Mengubah index kembali ke dalam bentuk huruf
        shifted_char = chr(shifted_index + ascii_offset)
        cipher_text += shifted_char
    return cipher_text

# Fungsi untuk mendekripsi pesan yang telah dienkripsi dengan shift cipher


def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        # Mengabaikan karakter selain huruf
        if not char.isalpha():
            plain_text += char
            continue
        # Mengubah huruf ke dalam bentuk angka (A=0, B=1, dst.)
        ascii_offset = 65 if char.isupper() else 97
        char_index = ord(char) - ascii_offset
        # Menghitung index huruf sebelum di-shift
        shifted_index = (char_index - key) % 26
        # Mengubah index kembali ke dalam bentuk huruf
        shifted_char = chr(shifted_index + ascii_offset)
        plain_text += shifted_char
    return plain_text


# Contoh penggunaan
plain_text = "ini adalah kode rahasia"
key = 69
cipher_text = encrypt(plain_text, key)
print("Pesan terenkripsi: ", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Pesan terdekripsi: ", decrypted_text)
