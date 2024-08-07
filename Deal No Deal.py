import random

# Define the game class
class DealOrNoDeal:
    def __init__(self):
        # Initialize the game with boxes and their values
        self.boxes = {
            1: 0.01, 2: 1, 3: 5, 4: 10, 5: 25,
            6: 50, 7: 75, 8: 100, 9: 500, 10: 1000,
            11: 5000, 12: 10000, 13: 25000, 14: 50000, 15: 100000
        }
        self.selected_box = None
        self.removed_boxes = []
        self.rounds = 3  # Number of rounds before a deal is offered
        self.bank_offer = 0
        self.player_money = 0

    def choose_box(self):
        """Player selects a box."""
        print("Choose a box number from 1 to 15:")
        while True:
            try:
                choice = int(input())
                if choice in self.boxes:
                    self.selected_box = choice
                    print(f"You have selected box {choice} which contains ${self.boxes[choice]:.2f}")
                    break
                else:
                    print("Invalid choice. Please choose a valid box number.")
            except ValueError:
                print("Please enter a number.")

    def remove_boxes(self):
        """Simulates removing boxes in each round."""
        for _ in range(self.rounds):
            while True:
                try:
                    choice = int(input("Choose a box to remove: "))
                    if choice in self.boxes and choice != self.selected_box and choice not in self.removed_boxes:
                        self.removed_boxes.append(choice)
                        print(f"Box {choice} removed, which contained ${self.boxes[choice]:.2f}")
                        break
                    else:
                        print("Invalid choice. Please choose a box that is not your selected box or already removed.")
                except ValueError:
                    print("Please enter a number.")

    def make_bank_offer(self):
        """Calculate a bank offer based on remaining boxes."""
        remaining_values = [self.boxes[box] for box in self.boxes if box not in self.removed_boxes and box != self.selected_box]
        self.bank_offer = sum(remaining_values) / len(remaining_values) * 0.5  # Bank offers 50% of the average
        print(f"The bank offers you: ${self.bank_offer:.2f}")

    def player_decision(self):
        """Player decides to accept or reject the bank offer."""
        decision = input("Do you accept the offer? (yes/no): ").strip().lower()
        if decision == 'yes':
            self.player_money = self.bank_offer
            print(f"You accepted the offer and won: ${self.player_money:.2f}")
        else:
            self.player_money = self.boxes[self.selected_box]
            print(f"You rejected the offer and won the amount in your box: ${self.player_money:.2f}")

    def play_game(self):
        """Main game loop."""
        print("Welcome to Deal or No Deal!")
        self.choose_box()
        self.remove_boxes()
        self.make_bank_offer()
        self.player_decision()

# Run the game
if __name__ == "__main__":
    game = DealOrNoDeal()
    game.play_game()