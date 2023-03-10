import calendar


class DVD:
    def __init__(self, name: str, id_num: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_num
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_num: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        month = calendar.month_name[int(month)]
        return cls(name, id_num, int(year), month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
