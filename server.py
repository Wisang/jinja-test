from flask import Flask, render_template

from datetime import datetime

import requests

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    this_year = now.year
    return render_template("index.html", cur_year=this_year)


@app.route('/guess/<user>')
def guess_me(user):
    response_age = requests.get("https://api.agify.io/", params={"name": user})
    age = response_age.json()['age']
    response_gender = requests.get("https://api.genderize.io/", params={"name": user})
    gender = response_gender.json()["gender"]
    return render_template("guess.html", user_name=user.title(), age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
