# class Person
# email , password, fullname, age
import datetime
class Person:
    # users list
    users = []
    # instructor of class
    def __init__(self, fname, em, pd, bd, pn):
        self.fullname = fname
        self.email = em
        self.password = pd
        self.birthday = bd
        self.phone = pn
        self.age = self.calculate_age()

    # calculate age
    def calculate_age(self):
        return datetime.datetime.now().year - self.birthday.year
    
    # to add user    
    def add_user(self):
        return Person.users.append(self)
    
    # display users
    def display_users(self):
        for user in Person.users:
            print(f" FullName {user.fullname}, email {user.email}, age {user.age}")


birthday = datetime.datetime(2001, 8, 27)
pr1 = Person("Younes", "soso@gmail.com", "far123", birthday, "062452662")
birthday = datetime.datetime(2003, 8, 27)

pr2 = Person("houssam", "soso@gmail.com", "far123", birthday, "062452662")
birthday = datetime.datetime(2003, 8, 27)

pr3 = Person("anas", "soso@gmail.com", "far123", birthday, "062452662")
birthday = datetime.datetime(2003, 8, 27)

pr4 = Person("ikram", "soso@gmail.com", "far123", birthday, "062452662")

pr1.add_user()
pr2.add_user()
pr3.add_user()
pr4.add_user()

pr4.display_users()