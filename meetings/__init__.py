class Meeting:
    def __init__(
        self,
        name,
        responsible_person,
        description,
        category,
        meeting_type,
    ):
        self.name = name
        self.responsible_person = responsible_person
        self.description = description
        self.category = category
        self.meeting_type = meeting_type

    def validate_responsible_person(self, user):
        return self.responsible_person == user

    def to_dict(self):
        return {
            "name": self.name,
            "responsible_person": self.responsible_person.to_dict(),
            "description": self.description,
            "category": self.category,
            "meeting_type": self.meeting_type,
        }

    def __str__(self):
        return (
            f"<Meeting name={self.name} "
            + f"responsible_person={self.responsible_person} "
            + f"description={self.description} "
            + f"category={self.category} "
            + f"type={self.meeting_type}>"
        )
