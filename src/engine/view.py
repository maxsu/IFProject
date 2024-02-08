from typing import Map

from pydispatch import dispatcher


class View:
    def __init__(self):
        dispatcher.connect(self.print_to_console, signal="Put_Text")
        dispatcher.connect(self.show_choices, signal="Give_Choice")

    def print_to_console(self, sender, text: str):
        print(text)

    def show_choices(self, sender, choices: Map[str, bool]):
        choice: str
        while True:
            choice = input("Choices are " + list(choices.keys()) + "\nEnter something")

            # Only allow choice if it's valid
            if choice in choices:
                dispatcher.send("Make_Choice", self, choice)

            print("Invalid choice, try again.\n")
