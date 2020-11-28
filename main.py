import csv
from sqlalchemy.orm import sessionmaker
from schema import engine, Countries, Population


c_code = set()
countries_data = []
populaton_data = []
with open("population-estimates.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        if row["Region"] == "Brunei Darussalam":
            row["Region"] = "Brunei"

        if row["Region"] == "Lao People's Democratic Republic":
            row["Region"] = "Laos"

        if row["Region"] == "Viet Nam":
            row["Region"] = "Vietnam"

        if row['Country Code'] not in c_code:
            c_code.add(row['Country Code'])
            countries_data.append(Countries(
                                            country_code=int(
                                                            row['Country Code']
                                                            ),
                                            region=row["Region"]
                                            ))

        populaton_data.append(Population(
                                         year=int(row["Year"]),
                                         population_yearwise=float(
                                                            row["Population"]
                                                            ),
                                         country_code=int(row['Country Code'])
        ))


Session = sessionmaker(bind=engine)
session = Session()
session.add_all(countries_data)
session.add_all(populaton_data)
session.commit()
session.close()
