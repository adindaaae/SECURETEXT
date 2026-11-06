
import msvcrt
import sys

from encryption import encrypt_message
from decryption import decrypt_message


def input_password(prompt="Masukkan password: "):
    print(prompt, end="", flush=True)

    password = ""

    while True:
        char = msvcrt.getwch()

        if char == "\r":
            print()
            break

        elif char == "\b":
            if password:
                password = password[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()

        elif char in ("\x00", "\xe0"):
            msvcrt.getwch()

        elif char == "\x03":
            raise KeyboardInterrupt

        else:
            password += char
            sys.stdout.write("*")
            sys.stdout.flush()

    return password


def tampilkan_menu():
    print("\n====================================")
    print("          SECURETEXT SYSTEM")
    print("       Aplikasi Keamanan Pesan")
    print("====================================")
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Pesan")
    print("3. Keluar")
    print("====================================")


def menu_enkripsi():
    print("\n========== ENKRIPSI PESAN ==========")

    pesan = input("Masukkan pesan asli: ")
    password = input_password()

    if not pesan or not password:
        print("Pesan dan password tidak boleh kosong!")
        return

    try:
        hasil = encrypt_message(pesan, password)

        print("\n[ENKRIPSI BERHASIL]")
        print("Hasil Enkripsi:")
        print(hasil)

    except Exception as error:
        print("Enkripsi gagal:", error)


def menu_dekripsi():
    print("\n========== DEKRIPSI PESAN ==========")

    pesan = input("Masukkan teks terenkripsi: ")
    password = input_password()

    if not pesan or not password:
        print("Pesan dan password tidak boleh kosong!")
        return

    try:
        hasil = decrypt_message(pesan, password)

        print("\n[DEKRIPSI BERHASIL]")
        print("Pesan Asli:")
        print(hasil)

    except ValueError as error:
        print("\n[DEKRIPSI GAGAL]")
        print(error)


def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            menu_enkripsi()

        elif pilihan == "2":
            menu_dekripsi()

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan SECURETEXT!")
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
