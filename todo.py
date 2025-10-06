#Display the current list of todos
#Allow the user to add new todo items
#Allow the user to remove existing todo items


my_list = []


while True:
    action = input("do you wanna add, remove or clear broski? (type add,remove or clear)").strip().lower()
    if action == "add":
        print()
        item = input("type something to add something: ")
        my_list.append(item)
        print()
        print("here is what you to do list looks like:", my_list)
    elif action == "remove":
        item = input("type something to remove something: ")
        if item in my_list:
            my_list.remove(item)
            print()
            print("this is your list now buddy:", my_list)
        else:
            print("Item not found.")
    elif action == "clear":
         my_list = []
         print("your list is cleared")
         print("here is what you to do list looks like:", my_list)


       
