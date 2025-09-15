# Erica Kinch
# TextBasedGame.py
# SNHU IT 140 – Project Two: Text-Based Adventure Game

DANGER_ROOM = 'Control Center'
REQUIRED_ITEMS = 6

rooms = {
    'Docking Bay': {'North': 'Security Office', 'East': 'Bio Lab', 'item': None},
    'Security Office': {
        'South': 'Docking Bay', 'North': 'Server Room',
        'East': 'Engineering Bay', 'item': 'Circuit Override Key'
    },
    'Bio Lab': {'West': 'Docking Bay', 'item': 'Access Card'},
    'Server Room': {'South': 'Security Office', 'East': 'Control Center',
                    'item': 'EMP Device Core'},
    'Control Center': {'West': 'Server Room', 'North': 'Maintenance Tunnel',
                       'item': None},
    'Engineering Bay': {
        'West': 'Security Office', 'North': 'Observation Deck',
        'East': 'Maintenance Tunnel', 'item': 'Engineering Scanner'
    },
    'Observation Deck': {'South': 'Engineering Bay', 'item': 'Cryo Sample Vial'},
    'Maintenance Tunnel': {
        'West': 'Engineering Bay', 'South': 'Control Center',
        'item': 'Plasma Torch'
    }
}


def show_instructions():
    print(
        "Welcome to Echoes of the Deep!\n\n"
        "You awaken alone in the Docking Bay of Abyssus-9, a derelict space "
        "station orbiting the edge of known space. A rogue AI known as The "
        "Marrow has taken over the Control Center.\n\n"
        "Commands:\n"
        "- Move: go North, go South, go East, go West\n"
        "- Collect item: get [item name]\n"
        "- Quit: quit"
    )


def show_status(current_room, inventory):
    exits = [
        f"- Exit {direction} to {rooms[current_room][direction]}"
        for direction in ['North', 'South', 'East', 'West']
        if direction in rooms[current_room]
    ]
    item = rooms[current_room]['item']
    item_msg = f"You see a {item}\n" if item and item not in inventory else ""
    print(
        f"\n----------------------------\n"
        f"You are in the {current_room}\n"
        f"Inventory: {inventory}\n"
        f"{item_msg}{chr(10).join(exits)}\n"
        f"----------------------------"
    )


def get_new_state(direction, current_room):
    return rooms[current_room].get(direction, current_room)


def main():
    current_room = 'Docking Bay'
    inventory = []

    show_instructions()

    # CLEANER LOOP: Only continues while game is active
    # Exits when in danger room OR all items collected (condition 2 in while statement)
    while current_room != DANGER_ROOM and len(inventory) < REQUIRED_ITEMS:
        show_status(current_room, inventory)

        # IF #1: If in room with item - collect if not already collected
        item = rooms[current_room]['item']
        if item and item not in inventory:
            inventory.append(item)
            rooms[current_room]['item'] = None
            print(f"You found and collected: {item}")

        # Get user command  
        command = input("Enter your command:\n> ").strip().lower()

        # IF #2: Handle movement commands (quit and invalid have same result - exit or continue)
        if command.startswith("go "):
            direction = command[3:].capitalize()
            new_room = get_new_state(direction, current_room)
            if new_room != current_room:
                current_room = new_room
            else:
                print("You can't go that way!")
        elif command == 'quit':
            print("Mission aborted. Game Over.")
            return
        else:
            print("Invalid command. Use 'go direction' or 'quit'.")

    # Game ends here: either win or lose based on conditions
    print("\n----------------------------")
    print("You've entered the Control Center...\n")
    print("The lights flicker. The Marrow awakens.\n")

    if len(inventory) == REQUIRED_ITEMS:
        print(
            "You unleash the EMP Core. The Marrow is neutralized!\n"
            "You disabled The Marrow and escaped. You win!"
        )
        status = "SUCCESS"
    else:
        print(
            "You entered unprepared. The Marrow overwhelms you.\n"
            "Game Over – The AI has claimed Abyssus-9."
        )
        status = "FAILURE"

    print(
        "Thanks for playing Echoes of the Deep.\n"
        "--- Mission Summary ---\n"
        f"Items Collected: {inventory}\n"
        f"Total Items: {len(inventory)} / {REQUIRED_ITEMS}\n"
        f"Status: {status}\n"
        "------------------------"
    )


if __name__ == "__main__":
    main()