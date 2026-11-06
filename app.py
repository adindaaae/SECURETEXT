
from flask import Flask, render_template, request
from encryption import encrypt_message
from decryption import decrypt_message

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    pesan = ""
    mode = ""
    error = None

    if request.method == "POST":
        mode = request.form.get("mode", "")
        pesan = request.form.get("pesan", "")
        password = request.form.get("password", "")

        if not pesan or not password:
            error = "Pesan dan password wajib diisi!"

        else:
            try:
                if mode == "encrypt":
                    hasil = encrypt_message(pesan, password)

                elif mode == "decrypt":
                    hasil = decrypt_message(pesan, password)

                else:
                    error = "Pilihan tidak valid!"

            except ValueError:
                error = "Proses gagal! Password salah atau data rusak."

            except Exception:
                error = "Terjadi kesalahan saat memproses pesan."

    return render_template(
        "index.html",
        hasil=hasil,
        pesan=pesan,
        mode=mode,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
