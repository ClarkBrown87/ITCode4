from datetime import date


class Human:
    def __init__(self, name, city, birth_date):
        self.name = name
        self.city = city
        self.birth_date = self.get_birth_date(birth_date)

    def full_years(self):
        today = date.today()
        return today.year - self.birth_date[2] - ((today.month, today.day) < (self.birth_date[1], self.birth_date[0]))

    @staticmethod
    def get_birth_date(birth_date):
        birth_date = birth_date.split('-')
        return [int(i) for i in birth_date]


user_name = "Iskander"
user_city = "Ufa"
user_birth = "24-10-2002"
user = Human(user_name, user_city, user_birth)
print(user.full_years())
