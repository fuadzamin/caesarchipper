1. Fungsi caesar_encrypt(plaintext, shift)
Fungsi ini digunakan untuk melakukan enkripsi pesan menggunakan algoritma Caesar Cipher dengan menggeser setiap karakter dalam teks sebanyak nilai shift tertentu.

Parameter plaintext: Teks asli (belum dienkripsi) yang akan dienkripsi.
Parameter shift: Nilai geser yang menentukan seberapa banyak karakter akan digeser dalam alfabet.
Variabel encrypted: Menyimpan hasil enkripsi dalam bentuk string. += digunakan untuk menambahkan setiap karakter yang sudah digeser ke dalam string encrypted. Penggunaan += di sini berarti "menambahkan ke string yang sudah ada" (concatenation).
Struktur Utama:

if char.isalpha(): Memeriksa apakah karakter dalam teks adalah huruf alfabet. Hanya huruf yang akan dienkripsi, sementara karakter lain (seperti spasi, tanda baca) akan tetap sama.
shift_base = 65 if char.isupper() else 97: Digunakan untuk membedakan antara huruf besar (A-Z) dan huruf kecil (a-z). Kode ASCII dari huruf besar dimulai dari 65 (A) dan dari 97 untuk huruf kecil (a). Ini memastikan penggeseran terjadi di antara huruf yang sesuai.
chr((ord(char) - shift_base + shift) % 26 + shift_base): Rumus ini melakukan penggeseran karakter:
ord(char): Mengonversi karakter menjadi nilai ASCII.
- shift_base: Menggeser nilai ASCII ke basis alfabet (0–25).
+ shift: Menambahkan nilai shift.
% 26: Agar nilai tetap dalam rentang 26 karakter alfabet.
+ shift_base: Mengembalikan nilai ke kode ASCII huruf besar/kecil.
else: encrypted += char: Jika karakter bukan huruf (misalnya spasi, tanda baca), karakter tersebut ditambahkan langsung ke hasil tanpa diubah.
2. Fungsi caesar_decrypt(ciphertext, shift)
Fungsi ini melakukan dekripsi dari teks yang telah dienkripsi menggunakan algoritma Caesar Cipher.

Parameter ciphertext: Teks yang telah dienkripsi dan ingin didekripsi.
Parameter shift: Nilai geser yang digunakan saat teks dienkripsi, yang juga harus digunakan untuk mendekripsi.
Variabel decrypted: Menyimpan hasil dekripsi, yang dibangun dengan cara yang sama seperti pada fungsi caesar_encrypt.
Struktur Utama:

Sama seperti dalam fungsi caesar_encrypt, tetapi dalam hal ini, karakter diambil kembali ke posisi semula dengan pengurangan nilai shift pada baris ord(char) - shift_base - shift.
3. Loop Utama: while True
Bagian ini berfungsi sebagai loop utama program yang memastikan program terus berjalan sampai pengguna memutuskan untuk keluar.

Penjelasan Struktur:

operation = input("Pilih operasi..."): Mengambil input dari pengguna untuk menentukan apakah mereka ingin melakukan enkripsi (enkrip) atau dekripsi (dekrip).

if operation in ['enkrip', 'dekrip']:: Validasi input untuk memastikan pengguna hanya memilih salah satu dari dua opsi yang valid. Jika input tidak valid, program akan meminta ulang hingga input valid dimasukkan.

message = input("Masukkan teks..."): Meminta input teks dari pengguna yang akan dienkripsi atau didekripsi.

try-except untuk shift:

shift = int(input("Masukkan nilai shift...")): Meminta input untuk nilai shift dari pengguna. Program mencoba untuk mengonversi input ke integer.
except ValueError:: Jika input tidak bisa dikonversi menjadi integer (misalnya pengguna memasukkan teks alih-alih angka), akan muncul pesan error dan meminta input ulang. Loop ini akan terus berulang hingga input yang valid dimasukkan.
Operasi if operation == 'enkrip':: Berdasarkan pilihan pengguna, program memutuskan apakah akan memanggil fungsi caesar_encrypt atau caesar_decrypt.

ulang = input("Apakah Anda ingin mengulang?"): Setelah satu operasi (enkripsi/dekripsi) selesai, pengguna diberi pilihan apakah mereka ingin menjalankan program lagi. Jika pengguna memasukkan selain ya, program akan keluar.
