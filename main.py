import json

if __name__ == '__main__':
    with open('birthdays.json', 'r') as f:
        data = json.load(f)

    for i in data:
        y = i
        print(i + ": " + data[y])

    name = input("Give me new name: ")
    year = input("Give me date of birth of that person (mm/dd/yyyy): ")
    entry = {name: year}
    data.update(entry)

    with open('birthdays.json', 'w')as f:
        json.dump(data, f)
