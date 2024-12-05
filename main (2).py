from contact_manager import add_contact, view_contacts, remove_contact, search_contacts
from file_handler import load_contacts, save_contacts

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            remove_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
