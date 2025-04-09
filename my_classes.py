from datetime import date


class Person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = birthdate  
        
    def get_age(self):
        today = date.today()
        return today.year - self.__birthdate.year - (
            (today.month, today.day) < (self.__birthdate.month, self.__birthdate.day)
        )


class Subject(Person):
    def __init__(self, first_name, last_name, birthdate, sex):
        super().__init__(first_name, last_name, birthdate)
        self.sex = sex

    def estimate_max_hr(self):
        """Berechnet die maximale Herzfrequenz: 220 - Alter"""
        return 220 - self.get_age()


class Examiner(Person):
    def __init__(self, first_name, last_name, birthdate):
        super().__init__(first_name, last_name, birthdate)


class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subject = None
        self.examiner = None

    def add_subject(self, subject):
        self.subject = subject

    def add_examiner(self, examiner):
        self.examiner = examiner

    def display(self):
        return {
            "Experiment": self.name,
            "Datum": self.date,
            "Teilnehmer": f"{self.subject.first_name} {self.subject.last_name}" if self.subject else "N/A",
            "Versuchsleiter": f"{self.examiner.first_name} {self.examiner.last_name}" if self.examiner else "N/A",
            "Max. Herzfrequenz (geschätzt)": self.subject.estimate_max_hr() if self.subject else "N/A"
        }