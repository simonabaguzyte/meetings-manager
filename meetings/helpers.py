from file_helpers import read_json_file, add_to_json_file
from constants import meetings_file_name
from meetings import Meeting
from users.helpers import display_users


def get_initial_meetings():
    meetings = []
    raw_meetings = read_json_file(meetings_file_name)

    for raw_meeting in raw_meetings:
        meeting = Meeting.from_raw(raw_meeting)
        meetings.append(meeting)

    return meetings


def display_meetings(meetings):
    if meetings == []:
        print("No meetings have been created")
        return

    print("Meetings:")
    for meeting in meetings:
        print(meeting)


def get_responsible_person(users):
    while True:
        display_users(users)
        username = input(
            "Please select a user for responsible person from the list above: "
        )

        for user in users:
            if user.username == username:
                return user

        print("Invalid username selected")


def register_meeting(users):
    name = input("Please enter meeting's name: ")
    responsible_person = get_responsible_person(users)
    description = input("Please enter meeting's description: ")
    category = input("Please enter meeting's category: ")
    meeting_type = input("Please enter meeting's type: ")
    start_date = input("Please enter meeting's start date: ")
    end_date = input("Please enter meeting's end date: ")

    meeting = Meeting(
        name,
        responsible_person,
        description,
        category,
        meeting_type,
        start_date,
        end_date,
    )
    return meeting


def create_new_meeting(users):
    new_meeting = register_meeting(users)
    add_to_json_file(meetings_file_name, new_meeting.to_dict())

    print("Meeting has been successfully created!")
    return new_meeting
