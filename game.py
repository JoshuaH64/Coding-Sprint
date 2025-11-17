# Simple text-based adventure game (starter code)

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.inventory = []
    
    def display_status(self):
        print(f"\n=== {self.name}'s Status ===")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Inventory: {self.inventory if self.inventory else 'Empty'}")
        print("=" * 30 + "\n")
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"You take {damage} damage! Health: {self.health}")
    
    def heal(self, amount):
        self.health = min(100, self.health + amount)
        print(f"You heal {amount} HP! Health: {self.health}")
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"You found: {item}")
    
    def award_points(self, points):
        self.score += points
        print(f"You earn {points} points! Total score: {self.score}")

player_name = input("Enter your name, adventurer: ")
player = Player(player_name)
print(f"Welcome, {player_name}! Your journey begins...")

def explore():
    print("You walk into a dark forest.")
    print("A wild creature appears!")
    action = input("Do you [fight] or [run]? ")
    if action.lower() == "fight":
        print("You bravely fight and win!")
        player.award_points(50)
        player.add_item("Golden Sword")
        player.take_damage(20)
    elif action.lower() == "run":
        print("You escape safely, but miss out on treasure.")
        player.score -= 10
        print(f"Score reduced: {player.score}")
    else:
        print("You hesitate and the creature vanishes.")
        print("Indecision costs you 5 points!")
        player.score -= 5

def cave():
    print("\nYou enter a mysterious cave...")
    print("You find a treasure chest!")
    action = input("Do you [open] it or [leave] it? ")
    if action.lower() == "open":
        print("You open the chest and find riches!")
        player.award_points(100)
        player.add_item("Treasure Chest")
    else:
        print("You wisely leave the suspicious chest behind.")
        player.award_points(10)

def village():
    print("\nYou arrive at a peaceful village.")
    print("A villager approaches you...")
    action = input("Do you [help] them or [ignore] them? ")
    if action.lower() == "help":
        print("The grateful villager gives you a healing potion!")
        player.add_item("Healing Potion")
        player.award_points(30)
    else:
        print("The villager looks disappointed.")
        player.award_points(5)

def castle():
    print("\nYou approach a grand castle...")
    print("Guards block your path!")
    action = input("Do you [negotiate] or [sneak]? ")
    if action.lower() == "negotiate":
        print("The guards let you pass. You're a true diplomat!")
        player.award_points(75)
        player.add_item("Royal Pass")
    elif action.lower() == "sneak":
        print("You sneak past the guards, but get spotted!")
        player.take_damage(25)
        player.award_points(40)
    else:
        print("You stand confused. The guards move you along.")
        player.score -= 5

import random

def random_encounter():
    encounters = [
        {
            "name": "Wandering Merchant",
            "text": "A merchant offers you a rare item for 20 points. Accept?",
            "accept": lambda: (player.award_points(-20), player.add_item("Rare Gem")) if player.score >= 20 else print("Not enough points!"),
            "decline": lambda: print("You move on.")
        },
        {
            "name": "Hidden Spring",
            "text": "You find a magical spring. Drink from it?",
            "accept": lambda: player.heal(50) or player.award_points(25),
            "decline": lambda: print("You continue your journey.")
        }
    ]
    encounter = random.choice(encounters)
    print(f"\n[Random Encounter] {encounter['name']}")
    print(encounter['text'])
    action = input("[yes] or [no]? ")
    if action.lower() == "yes":
        encounter['accept']()
    else:
        encounter['decline']()

def main():
    print("\n=== Welcome to the Adventure Game ===")
    print("Available commands:")
    print("  'explore' - Visit the dark forest")
    print("  'cave' - Enter a mysterious cave")
    print("  'village' - Visit a peaceful village")
    print("  'castle' - Approach a grand castle")
    print("  'encounter' - Try your luck with a random event")
    print("  'status' - View your health, inventory, and score")
    print("  'quit' - Exit the game\n")
    
    while True:
        command = input("> ")
        if command.lower() == "explore":
            explore()
        elif command.lower() == "cave":
            cave()
        elif command.lower() == "village":
            village()
        elif command.lower() == "castle":
            castle()
        elif command.lower() == "encounter":
            random_encounter()
        elif command.lower() == "status":
            player.display_status()
        elif command.lower() == "quit":
            print(f"Thanks for playing, {player.name}!")
            print(f"Final Score: {player.score}")
            print(f"Final Health: {player.health}")
            break
        else:
            print("Unknown command. Valid commands: explore, cave, village, castle, encounter, status, quit")

if __name__ == "__main__":
    main()