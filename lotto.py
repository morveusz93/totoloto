import random
import json


# funkcja, która pyta czy chcemy sami podac numery wylosować
# można załadować numery z pliku

def pick_my_numbers():
    while True:
        choice = input("R - Random\nN - New numbers\nL - Load from file\n").capitalize()
        if choice == 'R':
            my_numbers = draw_nums()
            break
        elif choice == 'N':
            my_numbers = give_me_nums()
            break
        elif choice == 'L':
            try:
                load_nums_from_file()
            except FileNotFoundError:
                print("No File Found!")
                choice = ''
                continue
        else:
            print("Wrong answer!")
            continue
    return my_numbers


# losowanie numerów
def draw_nums():
    return random.sample(range(1, 49), 6)


# sprawdzanie numerów
def check_nums(lucky, my):
    count = 0
    for x in my:
        if x in lucky:
            count +=1
    return count


# pobieranie numerów od użykownika
# z możliwością zapisania
def give_me_nums():
    nums = []
    while len(nums) != 6:
        try:
            num = int(input("Give me {}. num: ".format(len(nums) + 1)))
            if num not in nums and num in range(1, 50):
                nums.append(num)
        except ValueError:
            print("Wrong number!")
            continue
    print("Do you want to save these numbers and use it leter?")
    answer = input("y/n: ").upper()
    if answer == 'Y':
        save_nums_to_file(nums)
    return nums


def save_nums_to_file(nums):
    with open('mynumbers.json', 'w') as jf:
        json.dump(nums, jf, indent=2)


def load_nums_from_file():
    with open('mynumbers.json', 'r') as jf:
        nums = jf
    return nums


# ile razy puścić los?
def how_many_times():
    while True:
        number_of_times = input("How many times should I try?: ")
        try:
            number_of_times = int(number_of_times)
            return number_of_times
        except ValueError:
            print("I need number!")


# wczytanie danych z poprzednich losowań
def load_data():
    try:
        with open('results.json', 'r') as jf:
            data = json.load(jf)
            return data
    except FileNotFoundError:
        print("File Doesnt found!")


# zapisanie danych do pliku z poprzednimi losowaniami
def save_data(results):
    print("Do you wanna save?")
    while True:
        save_or_not = input("Y - yes\nN - No\n").upper()
        if save_or_not == 'Y':
            json_data = load_data()
            try:
                new_key = len(json_data.keys()) + 1
            except AttributeError:
                new_key = 1
                json_data = {}
            json_data[new_key] = results
            with open('results.json', 'w') as jf:
                json.dump(json_data, jf)
            print("Data saved!")
            break
        elif save_or_not == 'N':
            print("Not saved!")
            break
        else:
            print("Wrong answer, type Y or N!")
            save_or_not = ''


def main():
    print("Do you want to random nums/give me new nums or load saved nums?:")
    mynumbers = pick_my_numbers()
    times = how_many_times()
    draw_results = []
    for i in range (0, times):
        luckynumbers = draw_nums()
        result = (check_nums(luckynumbers, mynumbers))
        draw_results.append(result)
    full_results = {}
    for i in range(0, 7):
        full_results[i] = draw_results.count(i)
    print(full_results)
    save_data(full_results)


if __name__ == '__main__':
    main()
