checklist = list()

#create or add additional information to list
def create(item):
	checklist.append(item)
	

#Read One Item from an list
def read(index):
	return checklist[index]

#list all items
def list_all_items():
	index = 0
	for list_item in checklist:
		print("{} {}".format(index, list_item))
		index += 1

#update element in list
def update(index,item):
	checklist[index] = item
	return

#remove an element from array
def destroy(index):
	checklist.pop(index)

#takes user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")
        print(checklist[int(item_index)])

    elif function_code == "U":
        update(user_input("please input an Index you would like to change"),  user_input("please input what you would like to update it with"))

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "D":
        destroy(int(user_input("Please input an index for an element you would like to delete")))

    elif function_code == "Q":
        return False

    else:
        print("Unknown Option")

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list, D to delete an elemnt of the and Q to Quit")
    select(selection)