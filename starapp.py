import json, urllib2
from flask import Flask, render_template

starapp = Flask(__name__)

def get_content(api_key):
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=%s"%(api_key))
    parsed_data = json.loads(u.read())
    return parsed_data

@starapp.route('/')
def home():
    parsed_data = get_content("3vSKWgaQEj7l1JUvCaKYZQOG099b0YPu0PKaJV0T")
    return render_template("icstars.html", title=parsed_data["title"], date=parsed_data["date"],
        img_url=parsed_data["url"], cpyrght=parsed_data["copyright"], explain=parsed_data["explanation"])

if __name__ == '__main__':
    starapp.debug = True
    starapp.run()