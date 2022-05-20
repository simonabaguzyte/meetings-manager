from file_helpers import read_json_file, write_json_file
from meetings import Meeting
from users.helpers import display_users


def get_initial_meetings(users):
    meetings = []
    raw_meetings = read_json_file("meetings.json")

    for raw_meeting in raw_meetings:
        name = raw_meeting["name"]
        
        responsible_person = None
        for user in users:
            if user.username == dict["responsible_person"]["username"]:
                responsible_person = user

        description = raw_meeting["description"]
        category = dict["category"]
        meeting_type = dict["meeting_type"]

        meeting = Meeting(name, responsible_person, description, category, meeting_type)
        meetings.append(meeting)

    return meetings


def filter_by_description(meetings):
    filter = input("Please enter a phrase to filter description: ")

    filtered_meetings = []
    for meeting in meetings:
        if filter in meeting.description:
            filtered_meetings.append(meeting)

    if filtered_meetings == []:
        print("No meetings matching the filter were found")
    else:
        display_meetings(filtered_meetings)


def filter_by_responsible_person(meetings, users):
    responsible_person = get_responsible_person(users)

    filtered_meetings = []
    for meeting in meetings:
        if meeting.responsible_person == responsible_person:
            filtered_meetings.append(meeting)

    if filtered_meetings == []:
        print("No meetings assigned to the responsible person were found")
    else:
        display_meetings(filtered_meetings)


def filter_by_category(meetings):
    category = get_meeting_category()

    filtered_meetings = []
    for meeting in meetings:
        if meeting.category == category:
            filtered_meetings.append(meeting)

    if filtered_meetings == []:
        print("No meetings matching the category were found")
    else:
        display_meetings(filtered_meetings)


def filter_by_type(meetings):
    meeting_type = get_meeting_type()

    filtered_meetings = []
    for meeting in meetings:
        if meeting.meeting_type == meeting_type:
            filtered_meetings.append(meeting)

    if filtered_meetings == []:
        print("No meetings matching the type were found")
    else:
        display_meetings(filtered_meetings)


def display_meetings_with_filters(meetings, users):
    if meetings == []:
        print("No meetings have been created")
        return

    print("""
--------------------------
Meetings Filters
  1. No filter (display all meetings)
  2. Filter by description
  3. Filter by responsible person
  4. Filter by category
  5. Filter by type
""")
    option = input("Please select a filter: ")

    if option == "1":
        display_meetings(meetings)
    elif option == "2":
        filter_by_description(meetings)
    elif option == "3":
        filter_by_responsible_person(meetings, users)
    elif option == "4":
        filter_by_category(meetings)
    elif option == "5":
        filter_by_type(meetings)
    else:
        print("Invalid option selected")


def display_meetings(meetings, with_index=False):
    if meetings == []:
        print("No meetings have been created")
        return

    print("Meetings:")
    if with_index:
        for index, meeting in enumerate(meetings):
            print(f"  {index + 1}. {meeting}")
    else:
        for meeting in meetings:
            print(meeting)


def get_responsible_person(users):
    while True:
        display_users(users, True)
        number = input("Please select a user from the list above: ")

        try:
            number = int(number)
        except ValueError:
            print("Please select a valid number")
            continue

        if number > 0 and number <= len(users):
            return users[number - 1]

        print("Invalid number selected")


def get_meeting_category():
    categories = ["CodeMonkey", "Hub", "Short", "TeamBuilding"]
    while True:
        print("Categories:")
        for category in categories:
            print(category)

        selection = input("Please enter category: ")

        if selection in categories:
            return selection
        
        print("Please enter a category from the list")


def get_meeting_type():
    types = ["Live", "InPerson"]
    while True:
        print("Types:")
        for meeting_type in types:
            print(meeting_type)

        selection = input("Please enter type: ")

        if selection in types:
            return selection
            
        print("Please enter a type from the list")


def register_meeting(users):
    name = input("Please enter meeting's name: ")
    responsible_person = get_responsible_person(users)
    description = input("Please enter meeting's description: ")
    category = get_meeting_category()
    meeting_type = get_meeting_type()

    meeting = Meeting(name, responsible_person, description, category, meeting_type)
    return meeting


def add_meeting(prev_meetings, users):
    new_meeting = register_meeting(users)

    meetings = prev_meetings + [new_meeting]
    save_meetings(meetings)

    print("Meeting has been successfully created!")
    return meetings


def select_meeting_to_delete(meetings):
    while True:
        display_meetings(meetings, with_index=True)
        number = input(
            "Please select a number for a meeting you would like to delete: "
        )

        try:
            number = int(number)
        except ValueError:
            print("Please select a valid number")
            continue

        if number > 0 and number <= len(meetings):
            return meetings[number - 1]

        print("Invalid number selected")


def save_meetings(meetings):
    meetings_dict = []
    for meeting in meetings:
        meetings_dict.append(meeting.to_dict())
    print(meetings_dict)
    write_json_file("meetings.json", meetings_dict)


def delete_meeting(meetings, user):
    meeting = select_meeting_to_delete(meetings)

    valid = meeting.validate_responsible_person(user)
    if not valid:
        print(
            f"You are not the responsible person for this meeting. Please login as {meeting.responsible_person}"
        )
        return meetings

    meetings.remove(meeting)
    save_meetings(meetings)
    print("Meeting has been deleted")
    return meetings
