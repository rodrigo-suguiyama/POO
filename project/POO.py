from csv import writer


class Person:
    count = 0

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        Person.count += 1

    def name(self):
        name = self.first_name + " " + self.last_name
        return name

    def return_dict(self):
        return dict(first_name=self.first_name, last_name=self.last_name, sex=self.gender)


def user_input_firstnm_lstnm():
    first_name = input("The first name: ").title().strip()
    last_name = input("The last name: ").title().strip()
    gender = input("The gender: ").title().strip()
    return first_name, last_name, gender


person_list = []
_ = str
while _ != "no":
    print(f"Adding the user number {Person.count+1}.")
    input_data = user_input_firstnm_lstnm()
    person_list.append(Person(*input_data).return_dict())

    _ = input("keep adding? type [yes] or [no]: ").lower()

for i in person_list:
    print(i)


with open("user_names.csv", "w") as txt:
    writer = writer(txt)
    writer.writerow(["First Name", "Last Name", "Gender"])
    for i in person_list:
        writer.writerow(i.values())
