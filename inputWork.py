class Student:

    num_of_students = 0

    def __init__(self, name, date, number):
        self.name = name
        self.date = date
        self.number = number

    def get_info(self):
        print(self.name)

    #def __str__(self):
        #return self.name + " " + self.number

def find_contact(self, search):
    self.search = search
    #takes searching name as parameter
    # and put the searched contact into list,
    # check for no duplicate value in the list

def sorter(self):
    pass
    #O(n  log(n))  sorting  algorithm  is  preferred,
    # but  can  use  O(n2) algorithm for 10 point out of 35.
    # Should print ‘is empty’ if the database is empty

def history(self):
    pass
    #print out the list of searched contactsfrom oldest
    # to newest or print ‘is empty’ if list is empty
def printer(self):
    for i in range(len(list)):
        print(list[name])


list = []

#list.append(user)

finish = False

while( not finish):
    input_stream = input().split()
    action = input_stream[0]
    if action == 'n':
        name = input_stream[1]
        birthdate = input_stream[2]
        number = input_stream[3]
        if birthdate == number:
            print("Duplicate Number")
        temp = Student(name, birthdate, number)
        list.append(temp)
    elif action == "e":
        exit()
    elif action == "s":
        for student in list:
            #print(student)
            student.get_info()


    else:
        finish = True











