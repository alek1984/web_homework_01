from abc import ABC, abstractmethod

# Abstract base class for Views
class AbstractView(ABC):

    @abstractmethod
    def display(self, data):
        """Method to display data to the user."""
        pass

    @abstractmethod
    def prompt(self, message):
        """Method to prompt the user for input."""
        pass

# Console-specific implementation of the view
class ConsoleView(AbstractView):

    def display(self, data):
        print(data)

    def prompt(self, message):
        return input(message)

# Model to manage the application's data
class Model:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def get_contacts(self):
        return self.contacts

# Controller to handle logic
class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_contact(self):
        name = self.view.prompt("Enter contact name: ")
        phone = self.view.prompt("Enter contact phone: ")
        self.model.add_contact(name, phone)
        self.view.display(f"Contact {name} added successfully.")

    def show_contacts(self):
        contacts = self.model.get_contacts()
        if contacts:
            self.view.display("Your contacts:")
            for name, phone in contacts.items():
                self.view.display(f"{name}: {phone}")
        else:
            self.view.display("No contacts found.")

    def show_help(self):
        self.view.display("""
Available commands:
  add - Add a new contact
  list - List all contacts
  help - Show this help message
  exit - Exit the program
""")

# Main application loop
class Main:

    def __init__(self):
        self.model = Model()
        self.view = ConsoleView()
        self.controller = Controller(self.model, self.view)

    def run(self):
        self.view.display("Welcome to the Personal Assistant!")
        while True:
            command = self.view.prompt("Enter a command (help for options): ")
            if command == "add":
                self.controller.add_contact()
            elif command == "list":
                self.controller.show_contacts()
            elif command == "help":
                self.controller.show_help()
            elif command == "exit":
                self.view.display("Goodbye!")
                break
            else:
                self.view.display("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    app = Main()
    app.run()

