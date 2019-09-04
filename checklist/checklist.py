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

def update(index,item):
	checklist[index] = item
	return

def destroy(index):
	return checklist.pop(index)

def test():
	create("purple sox")
	create("red cloak")

	print(read(0))
	print(read(1))

	update(0, "purple socks")
	destroy(1)

	print(read(0))

test()