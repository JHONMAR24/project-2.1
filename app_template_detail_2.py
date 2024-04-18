from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r"C:\Users\legion\OneDrive\Documents\Data Analytic\flask1")
db_name = "autos1.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sales")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    auto = cursor.execute("SELECT * FROM auto").fetchall()
    con.close()

    return render_template("data_table.html", auto = auto)

if __name__=="__main__":
    app.run(debug=True)
