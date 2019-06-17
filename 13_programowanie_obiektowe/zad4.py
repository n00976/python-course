#Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza.
#Zaimplementuj dziedziczenie wielokrotne. Nasz zegaro-kalendarza powinen móc podawać aktualną datę
#oraz wyświetlać ile dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz
#zawierał datę, godzinę oraz widok dni ułożonych tygodniowo. Dla uproszczenia przyjmij 7 dni w tygodniu
#zawsze zaczyna się od pierwszego dnia.

#Utwórz obiekty, które będą przekazywać różne strefy czasowe i wyświetlać dzięki temu inne czasy zegara.
import calendar
import datetime


class Clock:
    def __init__(self):
        self.now = datetime.datetime.now()
        print(self.now.year, self.now.month)


class Calendar:
    def __init__(self):
        print(calendar.month(2019, 6))


class ClockCalendar(Calendar, Clock):
    def __init__(self):
        super().__init__()


cc = ClockCalendar()

