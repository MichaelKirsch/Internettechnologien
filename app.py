from flask import Flask, render_template
import db
import sqlite3
app = Flask(__name__)

db.init_app(app)



data=[
    {
        'id' : '1',
        'lat':'47.71423318561046',
        'lon': '10.310717989923432',
        'location':'Kempten',
        'type' : 'Automat',
    }
]


@app.route('/')
def index():
    return render_template("uebersicht.html")

@app.route('/eroeffnen')
def eroeffnen():
    return render_template("eroeffnen.html")

@app.route('/liste')
def liste():
    x = db.get_db()

    cur = x.cursor()
    try:
        cur.execute('SELECT * FROM station')
        data = [dict((cur.description[i][0], value) \
                  for i, value in enumerate(row)) for row in cur.fetchall()]
    finally:
        cur.close()

    return render_template("auflistung.html", data=data)

if __name__ == '__main__':
    app.run()


