# Ryan Huckaby            11-05-2025
# Assignment #5
#
# Description: This is the code for a TODO list which can help someone
#              to keep track of what tasks need to be completed.
#              You can load previous lists, save ones recently, and add/delete/move items into different categories.

import sys
import pickle

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("The Ultimate TODO List!")
    print()
    print("By: Ryan Huckaby")
    print("[COM S 1270 2]")
    print()

def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def checkIfListEmpty(todoList):
    """This function checks if there are any entries in the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean: If there is at least one item in the data structure, return False - it is not empty. Otherwise return True.
    """
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1
    item = item.lower().strip()

    for i in todoList:
        for j in range(len(todoList[i])):
            if todoList[i][j].strip().lower() == item:
                itemFound = True
                keyName = i
                index = j
                break
        if itemFound:
            break
    
    return itemFound, keyName, index

def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    clean = item.strip()
    result = checkItem(clean, todoList)
    itemFound = result[0]
    keyName = result[1]
    index = result[2]

    if itemFound:
        print(f"ERROR: The item '{clean}' is already in list '{keyName}' at position {index}.")
    else:
        todoList[toList].append(clean)

    return todoList

def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    result = checkItem(item, todoList)
    itemFound = result[0]
    keyName = result[1]
    index = result[2]

    if itemFound:
        todoList[keyName].pop(index)
    else:
        print(f"ERROR: '{item}' not found in category.")

    return itemFound, todoList

def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    result = deleteItem(item, todoList)
    itemFound = result[0]
    todoList = result[1]

    if itemFound:
        addItem(item, toList, todoList)
    
    return todoList

def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    for i in todoList:
        print(f"{i}: {todoList[i]}")

    return None

def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            x = input("Please enter an item: ")
            y = addItem(x, "backlog", todoList)
            printTODOList(y)
            pass
        elif choice == "m":
            if checkIfListEmpty(todoList) == False:
                while True:
                    x = input("What is the item you would like to move: ").strip()
                    result = checkItem(x, todoList)
                    itemFound = result[0]
                    if itemFound:
                        break
                    else:
                        print("Error: Item does not exist.")

                toList = ""

                while toList not in todoList:
                    toList = input("Enter the list to move the item to: ").strip()
                    if toList not in todoList:
                        print("Error: List does not exist.")

                todoList = moveItem(x, toList, todoList)
            else:
                print("No items to move!")

            printTODOList(todoList)
            pass
        elif choice == "d":
            if checkIfListEmpty(todoList) == False:
                item = input("What is the item you would like to delete: ")
                deleteItem(item, todoList)
            else:
                print("No items to delete!")

            printTODOList(todoList)
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    printTitleMaterial()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()