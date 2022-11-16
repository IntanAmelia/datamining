from flask import Flask,render_template, json, request 
app = Flask(__name__)
 
@app.route("/")
def main():
    return render_template('data.html')

@app.route("/load_data")
def load_data():
    return render_template('load_data.html')

@app.route("/preprocessing")
def preprocessing():
    return render_template('preprocessing.html')

@app.route("/normalisasidata")
def normalisasidata():
    return render_template('normalisasidata.py')

@app.route("/transformasidata")
def tranformasidata():
    return render_template('transformasidata.py')

@app.route("/implementation")
def tambahdata():
    return render_template('tambah_data.html')
 
if __name__ == "__main__":
    app.run()