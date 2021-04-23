from flask import Flask, render_template

app = Flask(__name__)

data=[
    {
        'name':'Audrin',
        'place': 'kaka',
        'mob': '7736',
        'lat':'47.71423318561046',
        'lon': '10.310717989923432'
    },
    {
        'name': 'Stuvard',
        'place': 'Goa',
        'mob' : '546464',
        'lat': '47.72774478260751',
        'lon': '10.31603949260898'
    },
{
        'name': 'dawrd',
        'place': 'Goa',
        'mob' : '546464',
        'lat': '47.74774478260751',
        'lon': '10.31603949260898'
    },
]


@app.route('/')
def index():
    return render_template("uebersicht.html")

@app.route('/eroeffnen')
def eroeffnen():
    return render_template("eroeffnen.html")

@app.route('/liste')
def liste():
    return render_template("auflistung.html", data=data)

if __name__ == '__main__':
    app.run()


