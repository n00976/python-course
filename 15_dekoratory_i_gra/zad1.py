import datetime
import holidays


class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()


    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)


    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6 or day in holidays.Polish():
            return 'Nie'
        else:
            return 'Tak'


#today = datetime.date.today()

today = datetime.date(2019, 1, 1)


print('Czy dzisiaj są zajęcia? ', Student.academic_day(today))