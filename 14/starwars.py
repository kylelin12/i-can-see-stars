from flask import Flask, render_template, request
import urllib2, json

api_foundation = "https://swapi.co/api/{0}/{1}/?format=json" 
# Formatting Strings for parameters. Inspired by James' work.

starwars = Flask(__name__)

def get_thing(thing, number):
    data_url = api_foundation.format("{}".format(thing), "{}".format(number))
    print data_url
    request = urllib2.Request(data_url, headers={'User-Agent' : "Magic Browser"}) # Headers required to avoid 403
    u = urllib2.urlopen(request)
    results = json.loads(u.read())
    if results["name"] == []:
        return 0
    return results

def parse_thing(thing, results):
    if thing == "planets":
        return render_template('results.html', name=results["name"], 
            orbital=results["orbital_period"], population=results["population"])
    if thing == "starships":
        return render_template('results.html', name=results["name"],
            model=results["model"], starship_class=results["starship_class"])
    if thing == "vehicles":
        return render_template('results.html', name=results["name"],
            model=results["model"], manufacturer=results["manufacturer"])
    if thing == "people":
        return render_template('results.html', name=results["name"],
            height=results["height"], gender=results["gender"])
    if thing == "species":
        return render_template('results.html', name=results["name"],
            classification=results["classification"], lifespan=results["average_lifespan"])
    return render_template('errorpage.html')

@starwars.route("/", methods=["GET", "POST"])
def root():
    if request.method == "GET":
        return render_template('searchpage.html')
    if request.method == "POST":
        results = get_thing(request.form["thing"], request.form["number"])
        if results == 0:
            return render_template('errorpage.html')
        return parse_thing(request.form["thing"], results)

if __name__ == "__main__":
    starwars.debug = True
    starwars.run()