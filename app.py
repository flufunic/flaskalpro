from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = 'assets/data.xlsx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    nik = request.form.get('nik').strip()
    try:
        df = pd.read_excel(EXCEL_FILE, dtype={'NIK': str})
        result = df[df['NIK'].str.strip() == nik]
        if result.empty:
            return jsonify({'message': 'Data tidak ditemukan!'}), 404
        data = result[[
            "Nama", "SEMBAKO", "PKH", "PBI", "RST", "BLT ELNINO", "BLT BBM",
            "SEMBAKO ADAPTIF", "BLT MIGOR", "YATIM PIATU", "PERMAKANAN",
            "PENA", "BPNT-PPKM", "BST", "ATENSI"
        ]].to_dict(orient='records')[0]
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
