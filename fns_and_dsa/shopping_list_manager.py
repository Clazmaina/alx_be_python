shopping_list = []
def add_item(item):
    shopping_list.append(item)
    print(f"Item '{item}' added to shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item '{item}' removed from shopping list.")
    else:
        print(f"Item '{item}' not found in shopping list.")

def view_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
         print(f"-{item}")
    else:
        print("Shopping list is empty.")

def main():
    while True:
        print("\nShopping List Manager")
        print("1.Add Item")
        print("2.Remove Item")
        print("3.View List")
        print("4.Exit")

        choice = input("Enter your choice(1-4):")

        if choice == '1':
            item = input("Enter item name:")
            add_item(item)
        elif choice == '2':
            item = input("Enter item name to remove:")
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()