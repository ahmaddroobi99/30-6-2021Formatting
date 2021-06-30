
class Person():
    def __init__(self, first_name, last_name, ide, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.ide = ide
        self.nationality = nationality

    def print_person(self):
        print(f"hi my name is {self.first_name} {self.last_name} and my nationality is  {self.nationality}and my ide "
              f"in case u wanna contact  {self.ide}")


user1 = Person("ahmad ", "Droobi", "4047297855567", "Palestinian")

user1.print_person()
