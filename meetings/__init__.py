from meetings.category import Category
from meetings.type import Type

class Meeting:
    def __init__(
        self,
        name,
        responsible_person,
        description,
        category,
        meeting_type,
        start_date,
        end_date,
    ):
        self.name = name
        self.responsible_person = responsible_person
        self.description = description
        self.category = category
        self.meeting_type = meeting_type
        self.start_date = start_date
        self.end_date = end_date

    @classmethod
    def from_raw(cls, dict, users):
        responsible_person = None
        for user in users:
            if user.username == dict["responsible_person"]["username"]:
                responsible_person = user
        
        category = Category[dict["category"]]
        meeting_type = Type[dict["meeting_type"]]

        return cls(
            name=dict["name"],
            responsible_person=responsible_person,
            description=dict["description"],
            category=category,
            meeting_type=meeting_type,
            start_date=dict["start_date"],
            end_date=dict["end_date"],
        )
    
    def validate_responsible_person(self, user):
        return self.responsible_person == user

    def to_dict(self):
        return {
            "name": self.name,
            "responsible_person": self.responsible_person.to_dict(),
            "description": self.description,
            "category": self.category.name,
            "meeting_type": self.meeting_type.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    def __str__(self):
        return f"<Meeting name={self.name} " + \
               f"responsible_person={self.responsible_person} " + \
               f"description={self.description} " + \
               f"category={self.category.value} " + \
               f"type={self.meeting_type.value}>"
