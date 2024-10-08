def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += char
    return decrypted

while True:
    while True:
        operation = input("Pilih operasi (enkrip/dekrip): ").lower()
        if operation in ['enkrip', 'dekrip']:
            break
        else:
            print("Operasi tidak valid. Silakan pilih 'enkrip' atau 'dekrip'.")
    
    message = input("Masukkan teks/kata yang akan diolah: ")

    while True:
        try:
            shift = int(input("Masukkan nilai shift (integer): "))
            break
        except ValueError:
            print("Nilai shift harus berupa integer. Silakan coba lagi.")
    
    if operation == 'enkrip':
        result = caesar_encrypt(message, shift)
        print("Hasil enkripsi:", result)
    elif operation == 'dekrip':
        result = caesar_decrypt(message, shift)
        print("Hasil dekripsi:", result)

    ulang = input("Apakah Anda ingin mengulang? (ya/tidak): ").lower()
    if ulang != 'ya':
        print("FUADZ MISBAHUL AMIN (220202689)")
        print("Program selesai. Terima kasih!")
        break
