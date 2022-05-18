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
    def from_raw(cls, dict):
        return cls(
            name=dict["name"],
            responsible_person=dict["responsible_person"],
            description=dict["description"],
            category=dict["category"],
            meeting_type=dict["meeting_type"],
            start_date=dict["start_date"],
            end_date=dict["end_date"],
        )

    def to_dict(self):
        return {
            "name": self.name,
            "responsible_person": self.responsible_person,
            "description": self.description,
            "category": self.category,
            "meeting_type": self.meeting_type,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    def __str__(self):
        return f"<Meeting> name={self.name} responsible_person={self.responsible_person}"
