import utils

keys, values = utils.get_population()
data = [
    {"Country": "Colombia", "Population": 500},
    {"Country": "Bolivia", "Population": 300},
]


def run():

    print("use function from module", keys, values)

    print("var of module---", utils.a)

    result = utils.population_by_country(data, "Colombia")
    print(result)


if __name__ == "__main__":
    run()
