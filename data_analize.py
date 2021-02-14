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
    print("Cost of one lottery ticket = 3 PLN")
    print("Winnig for 3/6: 24 PLN")
    print("Winnig for all 4/6: ~13% of jeckpot, average: 180 PLN")
    print("Winnig for all 5/6: 8% of jeckpot, average: 5.700 PLN")
    print("Winnig for all 6/6: 43% of jeckpot, average: guaranteed 2.000.000 PLN")
    print()


def calculate_the_win(how_many, which):
    which = int(which)
    how_many = int(how_many)
    if which == 1:
        which = 0
    elif which == 2:
        which = 0
    elif which == 3:
        which = 24
    elif which == 4:
        which = 180
    elif which == 5:
        which = 5700
    elif which == 6:
        if how_many == 0:
            return 0
        else:
            return 2000000
    return which * how_many


def print_winners(jf):
    number_of_draws = len(jf.keys())
    while True:
        try:
            key = input("Give me number of saved data loterry. You can pick one of: {} lotteries.\n"
                        .format(number_of_draws))
            print_infos()
            print("Lottry no. {}. Total draws: {}. Results: \n".format(key, sum(jf[key].values())))
            total_win = 0
            for i in jf[key]:
                print("Wining : {}/6  --- How many tiems: {}.".format(i, jf[key][i], ), end=' | ')
                print("Estimated win : {} PLN" .format(calculate_the_win(jf[key][i], i)))
                total_win += calculate_the_win(jf[key][i], i)
            print("\nMoney spend for lottry tickets: {} PLN".format(sum(jf[key].values()) * 3))
            print("Total win: {} PLN".format(total_win))
            break
        except (ValueError, KeyError):
            print("Wrong number of lottry!")


def main():
    results = load_data()
    print_winners(results)


if __name__ == '__main__':
    main()
