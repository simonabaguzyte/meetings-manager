from meetings.helpers import (
    add_meeting,
    delete_meeting,
    display_meetings_with_filters,
    get_initial_meetings,
)

from users.helpers import (
    add_user,
    display_logged_in_user,
    display_users,
    get_initial_users,
    login,
)


def get_option():
    print("""
--------------------------
Main Menu
  1. Login as a user
  2. Create a user
  3. Create a meeting
  4. Delete a meeting

  5. Display currently logged in user
  6. Display users
  7. Display meetings
  
  0. Exit the program
""")
    option = input("Please choose an option: ")
    return option


def run_program():
    print("\n\n***Welcome to Simona's meeting manager app***\n")

    users = get_initial_users()
    meetings = get_initial_meetings(users)
    user = login(users)

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
            print("Please select a valid menu option:")


if __name__ == "__main__":
    run_program()
