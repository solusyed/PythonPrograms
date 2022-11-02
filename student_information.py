class StudentInformation:

    firstname = "sohail"
    lastname = "syed"
    age = 22
    study = "btech"
    marks = 70

    if marks >= 70:
        print("good")
    elif marks >= 40:
        print("PASS")
    else:
        print("fail")

    def get_fullname(self):
        return self.firstname + self.lastname

    def get_age(self):
        return self.age


cs = StudentInformation()
res = cs.get_fullname()
print(res)
res = cs.get_age()
print(res)
