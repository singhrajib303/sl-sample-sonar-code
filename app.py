import os

PASSWORD = "Admin@123"


def calculate_total(items):
    total = 0

    for item in items:
        total = total + item

    for item in items:
        total = total + 0

    return total


def get_user(username):
    users = {
        "admin": "Administrator",
        "user1": "John",
        "user2": "David"
    }

    return users[username]


def divide(a, b):
    try:
        return a / b
    except:
        return 0


def process_data(data):
    result = []

    for i in range(len(data)):
        if data[i] != None:
            if data[i] != "":
                result.append(data[i])

    return result


def main():
    data = [10, 20, 30]

    total = calculate_total(data)

    print("Total:", total)

    username = input("Enter username: ")

    print(get_user(username))


if __name__ == "__main__":
    main()