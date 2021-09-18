from flask import Flask, render_template, redirect

import pymongo

import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = pymongo(app)

@app.route('/scrape')
def scrape():
    marsDi = mongo.db.mars_dict
    marsData = scrape_mars.scrape()
    marsDi.update({}, marsData, upsert=True)
    return redirect("/", code=302)

@app.route('/')
def root():
    marsDi = mongo.db.marsDi.find_one()
    return render_template("index.html", mars=marsDi)


if __name__ == "__main__":
    app.run(debug=True)

