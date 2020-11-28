import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Countries, Population
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler


# create Engine
engine = create_engine("postgresql://pranav:password@localhost/un_population")

# creating session
Session = sessionmaker(bind=engine)
session = Session()

# Retriving Indian data
indian_data = {
    "gTitle": "Indian Population For Year 2004 - 2014",
    "xLabels": [
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
    ],
    "xText": "Years",
    "yText": "Population in millions",
}

result = session.query(Population.population_yearwise).\
                    filter(Population.country_code == Countries.country_code).\
                    filter(Countries.region == 'India').\
                    filter(Population.year.in_(indian_data["xLabels"]))

population_data = []
for row in result:
    row = int(row[0] / 1000)
    population_data.append(row)

indian_data["data"] = population_data


# Retriving Asean data
asean_data = {
    "gTitle": "ASEAN Countries Population For Year 2014",
    "xLabels": [
        "Brunei",
        "Cambodia",
        "Indonesia",
        "Laos",
        "Malaysia",
        "Myanmar",
        "Philippines",
        "Singapore",
        "Thailand",
        "Vietnam",
    ],
    "xText": "Countries",
    "yText": "Population in millions",
}

result = session.query(Population.population_yearwise).\
                    filter(Population.country_code == Countries.country_code).\
                    filter(Population.year == 2014).\
                    filter(Countries.region.in_(asean_data["xLabels"]))

population_data = []
for row in result:
    row = int(row[0] / 1000)
    population_data.append(row)

asean_data["data"] = population_data


# Retriving SAARC data
saarc_countries = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka",
]

saarc_data = {
    "gTitle": "SAARC Countries Population For Year 2004 - 2014",
    "xLabels": [
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
    ],
    "xText": "Years",
    "yText": "Population in millions",
    "data": [],
}

for year in saarc_data["xLabels"]:
    result = session.query(Population.population_yearwise).\
                    filter(Population.country_code == Countries.country_code).\
                    filter(Countries.region.in_(saarc_countries)).\
                    filter(Population.year == year)

    result = [row[0] for row in result]
    saarc_data["data"].append(int(sum(result) / 1000))


# Retriving ASEAN data for group bar chart
asean_countries = [
    "Brunei",
    "Cambodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Vietnam",
]
asean_gb_data = {
    "gTitle": "ASEAN Countries Population For Year 2004 - 2014",
    "xLabels": [
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
    ],
    "xText": "Years",
    "yText": "Population in millions",
    "data": [],
}

for country in asean_countries:
    result = session.query(Population.population_yearwise).\
                    filter(Population.country_code == Countries.country_code).\
                    filter(Countries.region == country).\
                    filter(Population.year.in_(asean_gb_data["xLabels"]))

    result = [int(row[0] / 1000) for row in result]
    asean_gb_data["data"].append({
                                "name": country,
                                "data": result
                                })

# closing Session
session.close()

# Writing JSON file

# creating directory
p = Path('json_data')
p.mkdir(exist_ok=True)

all_data = {
    "india": indian_data,
    "asean": asean_data,
    "saarc": saarc_data,
    "aseanGb": asean_gb_data
}

with open("json_data/population.json", mode="w") as f:
    json.dump(all_data, f, indent=4)
    f.close()

# Starting HTTP Server on PORT 8000


def start_server(server_class=HTTPServer, handler=SimpleHTTPRequestHandler):
    PORT = 8000
    server_address = ('localhost', PORT)
    httpd = server_class(server_address, handler)
    print(f"Server started on PORT http://localhost:{PORT}")
    httpd.serve_forever()


start_server()
