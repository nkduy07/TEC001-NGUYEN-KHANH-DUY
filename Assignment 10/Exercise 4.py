import json
from flask import Flask

app = Flask(__name__)

with open('airports.json', 'r') as f:
    airports_db = json.load(f)


@app.route('/airport/<icao>')
def find_airport(icao):
    for airport in airports_db:
        if airport['icao'] == icao.upper():
            return {
                "icao": airport['icao'],
                "name": airport['name'],
                "city": airport['municipality'],
                "country": airport['iso_country']
            }
    return {"status": "error", "message": "Not found"}, 404


if __name__ == '__main__':
    app.run()