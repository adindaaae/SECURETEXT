
from encryption import encrypt_message
from decryption import decrypt_message

print("================================")
print("   PENGUJIAN SISTEM SECURETEXT")
print("================================")

pesan = "Data rahasia mahasiswa"
password = "Secure123!"

hasil_enkripsi = encrypt_message(pesan, password)

print("\n[1] Pengujian Enkripsi")
print("Status: BERHASIL")
print("Ciphertext:", hasil_enkripsi)

hasil_dekripsi = decrypt_message(
    hasil_enkripsi,
    password
)

print("\n[2] Pengujian Dekripsi")

assert hasil_dekripsi == pesan

print("Status: BERHASIL")
print("Pesan asli:", hasil_dekripsi)

print("\n[3] Pengujian Password Salah")

try:
    decrypt_message(hasil_enkripsi, "PasswordSalah")
    print("Status: GAGAL - Password diterima!")

except ValueError:
    print("Status: BERHASIL - Password ditolak!")

print("\n[4] Pengujian Data Rusak")

data_rusak = hasil_enkripsi[:-4] + "AAAA"

try:
    decrypt_message(data_rusak, password)
    print("Status: GAGAL - Data diterima!")

except ValueError:
    print("Status: BERHASIL - Data ditolak!")

print("\n================================")
print("   PENGUJIAN SELESAI")
print("================================")
