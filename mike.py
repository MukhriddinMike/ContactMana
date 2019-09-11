def length_of_list():
    global list1
    return len(list1)


def valid_position(index):
    if index < 0:
        return False
    else:
        length = length_of_list()
        if index <= length:
            return True
        else:
            return False


def insert_position():
    global list1
    name = input("\nWho do you want to add to the list?")
    index = int(input("What position do you want to insert name into list?"))
    if valid_position(index):
        list1.insert(index, name)
    else:
        print("\nItem not inserted.  Invalid Position")


def initialize_list():
    global list1
    confirm = input("\nAre you sure you want to initialize list? (y/n)")
    if (confirm == "y"):
        list1 = []


def add_list():
    global list1
    name = input("\nWho do you want to add to the list?")
    list1.append(name)


def find_list():
    global list1
    name_found = False
    name = input("\nWho do you want to find in the list?")
    for x in list1:
        if (x == name):
            print("\nFound " + name)
            name_found = True
    if (not name_found):
        print("\nNot in the list")


def report_all_items(input_list):
    print("\n")
    for item in input_list:
        print(item)


def delete_item():
    global list1
    position = int(input("\nWhat is the position of item you want to delete from list?"))
    if (position >= 0 and position < length_of_list()):
        del list1[position]
    else:
        print("\nThis is not a valid position")


def reverse_list():
    global list1
    temp_list = []
    len_list1 = length_of_list()
    temp_index = len_list1
    if len_list1 >= 2:
        for i in range(len_list1):
            temp_index = temp_index - 1
            temp_list.append(list1[temp_index])
        for i in range(len_list1):
            list1[i] = temp_list[i]


def sort_list():
    global list1
    len_list1 = length_of_list()
    if (len_list1 >= 2):
        for i in range(len_list1 - 1):
            for j in range(1, len_list1):
                if (list1[i] > list1[j]):
                    temp = list1[i]
                    list1[i] = list1[j]
                    list1[j] = temp


done = False
while (not done):
    print("\nWhat would you like to do?")
    print("1.  Initialize the List ")
    print("2.  Add an Item to the List")
    print("3.  Find an Item in the List")
    print("4.  Find the length of the List")
    print("5.  Insert an Item in a postion in List")
    print("6.  Report all Items in the List")
    print("7.  Delete an Item from the List")
    print("8.  Reverse a List")
    print("9.  Sort a list")
    print("10. Quit")
    option = int(input("Choose One: "))
    if (option == 1):
        initialize_list()
    elif (option == 2):
        add_list()
    elif (option == 3):
        find_list()
    elif (option == 4):
        length = length_of_list()
        print("\nThe length of List is: ", length)
    elif (option == 5):
        insert_position()
    elif (option == 6):
        report_all_items(list1)
    elif (option == 7):
        delete_item()
    elif (option == 8):
        reverse_list()
    elif (option == 9):
        sort_list()
    else:
        done = True