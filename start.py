#Contact management system

#def newContact:
    #name = input("")
    #birthdate = input("")
    #number = input("")

class Student():
    def __init__(self, name, date, number):
        self.name = name
        self.date = date
        self.number = number

user = Student(name="", date="", number="")
list = []
list.append(user)

def newContact(list):
    name = input("")
    date = input("")
    number = input("")
    user = Student(name,date,number)


def sort_list():
    for i in range(len(list)):
        for j in range(1, len(list)):
            if (list[i] > list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp


finish = False
while( not finish ):
    action = input("")
    if action == "n":
        list.append(newContact())
    elif action == "e":
        exit()
    elif action == 'h':
        pass
    elif action == "s":
        sort_list()
        for m in range(len(list)):
            print(user.name)

    elif action == "f":
        pass


