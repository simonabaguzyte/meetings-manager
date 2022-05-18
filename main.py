from meetings.helpers import (
    add_meeting,
    delete_meeting,
    display_meetings_with_filters,
    get_initial_meetings,
)
from texts import main_menu_options
from users.helpers import (
    add_user,
    display_logged_in_user,
    display_users,
    get_initial_users,
    login,
)


def get_option():
    print(main_menu_options)
    option = input("Please chose an option: ")
    return option


def run_program():
    print("Welcome to Simona's meeting manager app")

    users = get_initial_users()
    user = login(users)
    meetings = get_initial_meetings(users)

    while True:
        option = get_option()

        if option == "1":
            user = login(users)
        elif option == "2":
            users = add_user(users)
        elif option == "3":
            meetings = add_meeting(meetings, users)
        elif option == "4":
            meetings = delete_meeting(meetings, user)
        elif option == "5":
            display_logged_in_user(user)
        elif option == "6":
            display_users(users)
        elif option == "7":
            display_meetings_with_filters(meetings, users)
        elif option == "0":
            break
        else:
            print("Please select a valid menu option")


if __name__ == "__main__":
    run_program()
