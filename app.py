from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Fungsi untuk menghitung angka rahasia
def hitung_angka_rahasia():
    hari_ini = datetime.now()
    return hari_ini.day + 5 

# Variabel global
angka_rahasia = hitung_angka_rahasia()
kesempatan = 5

@app.route('/')
def home():
    global angka_rahasia, kesempatan
    angka_rahasia = hitung_angka_rahasia()  
    kesempatan = 5  
    print(f"Angka rahasia adalah: {angka_rahasia}")  
    return render_template('home.html', kesempatan=kesempatan, pesan=None)

@app.route('/tebak', methods=['POST'])
def tebak():
    global angka_rahasia, kesempatan

    # Ambil input tebakan
    tebakan = int(request.form.get('tebakan'))  
    kesempatan -= 1  

    # Cek apakah tebakan benar
    if tebakan == angka_rahasia:
        print("Boom! Anda menang!")
        return render_template('menang.html', kesempatan=kesempatan, pesan="Boom! Anda menang!")
    # Cek jika tebakan terlalu kecil
    elif tebakan < angka_rahasia:
        print("Terlalu kecil.")
        if kesempatan == 0:
            return redirect(url_for('game_over'))
        else:
            return render_template('home.html', kesempatan=kesempatan, pesan="Terlalu kecil.")
    # Cek jika tebakan terlalu besar
    else:
        print("Terlalu besar.")
        if kesempatan == 0:
            return redirect(url_for('game_over'))
        else:
            return render_template('home.html', kesempatan=kesempatan, pesan="Terlalu besar.")

@app.route('/game-over')
def game_over():
    print(f"Kesempatan habis! Angka rahasia adalah {angka_rahasia}.")  # Debugging
    return render_template('game_over.html', pesan=f"Kesempatan habis! Angka rahasia adalah {angka_rahasia}.")

if __name__ == '__main__':
    app.run(debug=True)
