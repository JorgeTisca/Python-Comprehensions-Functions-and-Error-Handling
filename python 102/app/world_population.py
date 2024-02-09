import charts
import read_csv

#     percentages_dict = {
#         item["Country/Territory"]: item["World Population Percentage"] for item in data
#     }

#     names = percentages_dict.keys()
#     per = percentages_dict.values()

#     return names, per


def run():
    data = read_csv.read_csv("./app/data.csv")
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    countries = list(
        map(lambda x: x["Country/Territory"], data)
    )  # get just the column of Country/Territory
    percentages = list(
        map(lambda x: x["World Population Percentage"], data)
    )  # get just the column of World Population Percentage

    charts.generate_pie_chart(countries, percentages)


if __name__ == "__main__":
    run()
