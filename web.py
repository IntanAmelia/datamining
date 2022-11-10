from flask import Flask,render_template, json, request 
app = Flask(__name__)
 
@app.route("/")
def main():
    return render_template('data.html')

@app.route("/tambahdata")
def tambahdata():
    return render_template('tambah_data.html')
 
if __name__ == "__main__":
    app.run()