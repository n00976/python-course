#Utwórz klasę Pracownik.
    #Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
    #Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
    #pensja + work experience * (pensja * 5%)
    #Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
    #Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
    #Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
    #Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.
    #Adam Kowalski Love Python Company
    #email -> smkwlsk@lovepythoncompany.com

class Worker:

    def __init__(self, job, salary, name, surname, work_experience):
        self.job = job
        self.salary = salary
        self.name = name
        self.surname = surname
        self.work_experience = work_experience

