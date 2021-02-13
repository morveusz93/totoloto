import json


def input_num(string):
    while True:
        answer = input(string)
        try:
            num = int(answer)
            return num
        except ValueError:
            print("Wrong! Give me number!")


def load_data():
    with open('results.json', 'r') as jf:
        return json.load(jf)


def print_infos():
    print("Koszt pojedynczego losu to 3zł")
    print("Wygrana za 3 trafienia to: 24 zł")
    print("Wygrana za 4 trafienie to: ~13% puli")
    print("Wygrana za 5 trafień to: 8% puli")
    print("Wygrana za 6 trafień to: 43% puli")


def print_winners(jf):
    number_of_draws = len(jf.keys())
    while True:
        try:
            key = input("Podaj numer losowania. Do wyboru masz {} losowań.\n".format(number_of_draws))
            print("Losowanie numer {}: ".format(key))
            for i in jf[key]:
               print("Trafienia: {}  --- ilość: {}.".format(i, jf[key][i]))
            break
        except (ValueError, KeyError):
            print("Błędny numer losowania!")


def main():
    results = load_data()
    # jackpot = input_num("Podaj pulę wygranych: ")
    print_winners(results)


if __name__ == '__main__':
    main()
