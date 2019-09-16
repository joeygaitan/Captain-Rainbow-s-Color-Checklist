checklist = list()

#create or add additional information to list
def create(item):
	checklist.append(item)
	

#Read One Item from an list
def read(index):
    print("on line 10")
    return checklist[index]

def check(index):
    checkerChecker = checklist[int(index)].split()
    if checkerChecker[0] == "√":
       print("This item is already checked")
    else:
        checklist[int(index)] = "√" + checklist[int(index)]
        return True

def uncheck(index):
    checkerChecker = checklist[int(index)][1:]
    checklist[int(index)] = checkerChecker
    

#list all items
def list_all_items():
    if len(checklist) == 0:
        return "Please Add some items to your checklist please" 
    else:
	    index = 0
	    for list_item in checklist:
		    print("{} {}".format(index, list_item))
		    index += 1

#update element in list
def update(index,item):
    if len(checklist) == 0:
        return "There is nothing to change :/"
    else:
	    checklist[index] = item

#remove an element from array
def destroy(index):
	checklist.pop(index)

#takes user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    if function_code == "C" or function_code=="c":
        create(user_input("Input item: "))
        return True
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number: ")
        print(checklist[int(item_index)])
        return True
    elif function_code == "U" or function_code == "u":
        update(user_input("please input an Index you would like to change"),  user_input("please input what you would like to update it with"))
        return update(user_input("please input an Index you would like to change"),  user_input("please input what you would like to update it with"))
    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()
        return True
    elif function_code == "D" or function_code == "d":
        destroy(int(user_input("Please input an index for an element you would like to delete")))
        return True
    elif function_code == "Q" or function_code == "q":
        print("Thanks for using this project")
        return False
    elif function_code == "check" or function_code == "Check":
        check(user_input("please select which one you want to check: "))

    elif function_code == "uncheck" or function_code == "Uncheck":
        uncheck(user_input("Please select index of something you want to uncheck: "))

    else:
        print("Unknown Option")


running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list,\n D to delete an elemnt of the list.\n To add a checkmark to this list please type Check. To uncheck type uncheck and Q to Quit: ")
    check_list = select(selection)
    if check_list == False:
        running = False