from file_helpers import read_json_file, write_json_file
from constants import users_file_name
from users import User


def save_users(users):
    users_dict = []
    for user in users:
        users_dict.append(user.to_dict())
    write_json_file(users_file_name, users_dict)



def register_user():
    username = input("Please enter a username you would like to register: ")
    user = User(username)
    return user


def add_user(prev_users):
    new_user = register_user()

    users = prev_users + [new_user]
    save_users(users)

    print("User has been successfully created!")
    return users


def get_initial_users():
    users = []
    raw_users = read_json_file(users_file_name)
    if raw_users == []:
        users = add_user(users)

    for raw_user in raw_users:
        user = User.from_raw(raw_user)
        users.append(user)

    return users


def display_users(users, with_index=False):
    if users == []:
        print("No users have been created")
        return

    print("Users:")
    if (with_index):
        for index, user in enumerate(users):
            print(f"  {index + 1}. {user}")
    else:
        for user in users:
            print(user)


def login(users):
    while True:
        display_users(users, with_index=True)
        number = input("Please select a number for a user from the list above: ")

        try:
            number = int(number)
        except ValueError:
            print("Please select a valid number")
            continue

        if (number > 0 and number <= len(users)):
            return users[number - 1]
        
        print("Invalid number selected")

def display_logged_in_user(user):
    print(f"Currently logged in as {user}")