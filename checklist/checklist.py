print("Hello World")


def my_fun_function(say_this):
	print(say_this)

print(my_fun_function('Hello World'))

checklist = list()

#create or add additional information to list
def create(item):
	return checklist.append(item)
	

#Read One Item from an list
def read(index):
	return checklist[index]

def list_all_items():
	index = 0
	for list_item in checklist:
		print("{} {}".format(index, list_item))
		index += 1

def update(index,item):
	checklist[index] = item
	return

def destroy(index):
	return checklist.pop(index)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
	create("purple sox")
	create("red cloak")

	print(read(0))
	print(read(1))

	update(0, "purple socks")
	destroy(1)

	print(read(0))

	list_all_items()
	 # Your testing code here
    # ...
    # Call your new function with the appropriate value
	select("C")
    # View the results
	list_all_items()
    # Call function with new value
	select("R")
    # View results
	list_all_items()
    # Continue until all code is run

def mark_completed(index):
	checklist[index] = "√" + checklist[index]
	return checklist[index]

test()

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")