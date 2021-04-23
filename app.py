from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired
from config import Config

import db
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


class CreateForm(FlaskForm):
    lat = StringField(validators=[DataRequired()])
    lon = StringField(validators=[DataRequired()])
    type = RadioField('Typ', choices=[('A', 'Automat'), ('V', 'Verkaufstelle'), ('B', 'Verkaufstelle + Automat')])
    description = StringField("Beschreibung", validators=[DataRequired()])
    location = StringField("Standort", validators=[DataRequired()])
    submit = SubmitField('Eröffnen')


class EditForm(FlaskForm):
    lat = StringField(validators=[DataRequired()])
    lon = StringField(validators=[DataRequired()])
    type = RadioField('Typ', choices=[('A', 'Automat'), ('V', 'Verkaufstelle'), ('B', 'Verkaufstelle + Automat')])
    description = StringField("Beschreibung", validators=[DataRequired()])
    location = StringField("Standort", validators=[DataRequired()])
    submit = SubmitField('Eröffnen')

data = []


@app.route('/')
def index():
    return render_template("uebersicht.html")


@app.route('/loeschen/', methods=['GET', 'POST'])
def loeschen():
    if request.method == "POST":
        x = db.get_db()
        cur = x.cursor()
        try:
            cur.execute("DELETE from station WHERE stationID ={}".format(request.json['id']))
            x.commit()
        finally:
            cur.close()
        return redirect(url_for('liste'))

@app.route('/bearbeiten/')
def bearbeiten():
    print(request.args.get('id'))
    return render_template("bearbeiten.html")



@app.route('/eroeffnen', methods=['GET', 'POST'])
def eroeffnen():
    form = CreateForm()
    if form.validate_on_submit():
        l = request.form.get('lat')
        o = request.form.get('lon')
        t = request.form.get('type')
        des = request.form.get('description')
        loc = request.form.get('location')

        x = db.get_db()

        cur = x.cursor()
        try:
            querey = ("INSERT INTO station (coordsA, coordsL, location, type, description) VALUES ('{}','{}','{}','{}','{}')".format(l, o, loc, t, des))
            # insert sql attack here, sql injection scripting izzz da
            cur.execute(querey)
            x.commit()
        finally:
            cur.close()
        return redirect(url_for('liste'))
    return render_template("eroeffnen.html", title='Sign In', form=form)


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
