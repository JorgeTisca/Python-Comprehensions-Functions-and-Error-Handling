import charts
import read_csv
import utils

keys, values = utils.get_population()
data = [
    {"Country": "Colombia", "Population": 500},
    {"Country": "Bolivia", "Population": 300},
]


def project_graph():
    data_read = read_csv.read_csv("./app/data.csv")
    # print(data_read)
    country = input("Type Country --->").capitalize()
    print(country)
    result = utils.population_finally_bycountry(data_read, country)
    # print(result)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_finally_population(country)
        print(labels, values)
        charts.generate_bar_chart(labels, values)


def run():

    print("use function from module", keys, values)

    print("var of module---", utils.a)

    result = utils.population_by_country(data, "Colombia")
    print(result)

    print("-" * 20, "Proyect with CSV", "-" * 20)
    project_graph()


if __name__ == "__main__":
    run()
