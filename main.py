import random
import os

# vars (test commit from laptop)
board = [i for i in range(1, 31)]

# lucky tile gen
def generate_lucky_tiles():
    lucky_tiles = []
    current_tile = 3

    while len(lucky_tiles) < random.randint(6, 7):
        if current_tile >= 27:
            break
        lucky_tiles.append(current_tile)
        current_tile += random.randint(3, 6)
    
    return lucky_tiles

lucky_tiles = generate_lucky_tiles()

all_figures = ['*', '!', '/', '>', '<', '#', '$', '%', 'Σ']
available_figures = all_figures

questions = {
    "easy": [
        {
            "question": "How many generations of computers are there (including the current one)?",
            "choices": ["A) 7", "B) 5", "C) 6", "D) 4"],
            "answer": "C",
            "creator": "JB"
        },
        {
            "question": "What is the primary function of the motherboard in a computer?",
            "choices": ["A) Storing data long-term", "B) Providing a surface for cooling systems", "C) Hosting the CPU and other key components", "D) Connecting the computer to the internet"],
            "answer": "C",
            "creator": "KP"
        },
        {
            "question": "What type of memory is used for frequently accessed data and improves processing speed?",
            "choices": ["A) ROM", "B) Cache memory", "C) Hard disk", "D) USB drive"],
            "answer": "B",
            "creator": "RA"
        },
        {
            "question": "Which type of storage device was primarily used to store data in early computers?",
            "choices": ["A) CD-ROM", "B) USB flash drive", "C) Blu-ray", "D) Punch card"],
            "answer": "D",
            "creator": "BG"
        },
        {
            "question": "What type of cable is typically used to connect hard drives to the motherboard?",
            "choices": ["A) SATA", "B) HDMI", "C) USB", "D) Ethernet"],
            "answer": "A",
            "creator": "KP"
        },
        {
            "question": "Which component is responsible for connecting the CPU to RAM and other high-speed components?",
            "choices": ["A) Southbridge", "B) FSB", "C) Power Supply", "D) PCI slot"],
            "answer": "B",
            "creator": "JB"
        }

    ],

    "medium": [
        {
            "question": "What does CPU stand for?",
            "choices": ["A) Central Performance Unit", "B) Central Processing Unit", "C) Central Processing Utility", "D) Core Processing Unit"],
            "answer": "B",
            "creator": "BG"
        },
        {
            "question": "What is the function of the Southbridge on a motherboard?",
            "choices": ["A) Connects the CPU to the RAM", "B) Manages the interaction between the CPU and the graphics card", "C) Handles communication with slower components like USB ports and hard drives", "D) Controls the cooling systems of the computer"],
            "answer": "C",
            "creator": "RA"
        },
        {
            "question": "Which of the following is not a characteristic of an ATX motherboard?",
            "choices": ["A) It is an Advanced Technology Extended form factor", "B) It is larger than the Micro-ATX", "C) It uses LPX low-profile design", "D) It is widely used in desktop computers"],
            "answer": "C",
            "creator": "BG"
        },
        {
            "question": "What does the abbreviation 'EEPROM' stand for?",
            "choices": ["A) Electrically Erasable Programmable Read-Only Memory", "B) Extended Erasable Programmable Read-Only Memory", "C) External Enhanced Programmable Random-Only Memory", "D) Embedded Eraseable Permanent Read-Only Memory"],
            "answer": "A",
            "creator": "KP"
        },
        {
            "question": "What is the storage capacity of a typical 3.5\" floppy disk?",
            "choices": ["A) 1.44 MB", "B) 720 KB", "C) 500 MB", "D) 2 GB"],
            "answer": "A",
            "creator": "JB"
        },
        {
            "question": "What is the primary difference between RISC and CISC processors?",
            "choices": ["A) RISC processors use a simplified instruction set, while CISC uses complex instructions", "B) CISC processors use reduced instructions, while RISC uses complex instructions", "C) RISC processors are used in desktop computers, CISC is used in smartphones", "D) There is no difference; both terms describe the same type of processor"],
            "answer": "A",
            "creator": "RA"
        },
        {
            "question": "What is the main advantage of flash memory compared to magnetic storage?",
            "choices": ["A) It requires continuous power to retain data", "B) It is slower but more durable", "C) It is faster and more energy-efficient", "D) It uses lasers to store data"],
            "answer": "C",
            "creator": "BG"
        }

    ],

    "hard": [
        {
            "question": "Out of these options, which one ISN't an abbreviation for a type of a memory card?",
            "choices": ["A) BIOS", "B) MMC", "C) SD", "D) CF"],
            "answer": "A",
            "creator": "RA"
        },
        {
            "question": "Which of the following USB standards offers the fastest data transfer rate?",
            "choices": ["A) USB 1.1 - 12 Mbps", "B) USB 2.0 - 480 Mbps", "C) USB 3.0 - 5 Gbps", "D) USB 2.0 - 12 Mbps"],
            "answer": "C",
            "creator": "KP"
        },
        {
            "question": "What is the maximum cable length allowed for USB 2.0 without the use of repeaters?",
            "choices": ["A) 5 meters", "B) 15 meters", "C) 3 meters", "D) 10 meters"],
            "answer": "A",
            "creator": "JB"
        },
        {
            "question": "Which of the following statements about FireWire (IEEE 1394) is incorrect?",
            "choices": ["A) FireWire can support up to 63 connected devices", "B) IEEE 1394b standard supports up to 800 Mbps data transfer speed", "C) FireWire requires external power for all connected devices", "D) Maximum cable length for IEEE 1394a is 4.5 meters"],
            "answer": "C",
            "creator": "RA"
        },
        {
            "question": "Which port type is primarily used for connecting older printers and supports up to 8 Mbps transfer speeds?",
            "choices": ["A) Serial Port", "B) USB 1.1", "C) Parallel Port", "D) HDMI"],
            "answer": "C",
            "creator": "BG"
        },
        {
            "question": "What is the primary use of an SCSI controller in a computer system?",
            "choices": ["A) Connecting wireless devices", "B) Managing audio output", "C) Connecting hard drives and tape drives", "D) Providing internet access via phone line"],
            "answer": "C",
            "creator": "KP"
        },
        {
            "question": "How many USB devices can be connected to a single USB host controller using hubs?",
            "choices": ["A) 64", "B) 127", "C) 32", "D) 255"],
            "answer": "B",
            "creator": "RA"
        }

    ]
}

lucky_cards = [
    # positives
    {"message": "You passed the sectoral basic exam!", "effect": lambda: random.randint(1, 3)},
    {"message": "You hop into your superior gaming chair, and speed up.", "effect": lambda: random.randint(1, 2)},
    {"message": "You chug three bottles of XIXO, and feel the power rushing through your veins.", "effect": lambda: random.randint(1, 5)},
    {"message": "Listening to Avatar has brought you power!", "effect": lambda: random.randint(1, 3)},
    {"message": "You are sprinting in order to catch your bus.", "effect": lambda: random.randint(1, 4)},

    # negatives
    {"message": "You didn't score enough points on your IT test.", "effect": lambda: -random.randint(1, 3)},
    {"message": "You brought your backpack in the classroom, and your IKT teacher tripped over in it. He got mad, and roundhouse kicked you in the head.", "effect": lambda: -random.randint(1, 4)},
    {"message": "You listened to too much generic NPC music, and are now dazed and confused.", "effect": lambda: -random.randint(1, 4)}
]

# colors
def gray(str):
    return col(str, 30)

def red(str):
    return col(str, 31)

def green(str):
    return col(str, 32)

def yellow(str):
    return col(str, 33)
    
def blue(str):
    return col(str, 34)

def magenta(str):
    return col(str, 35)

def cyan(str):
    return col(str, 36)

def col(msg, color):
    return '\033[1;' + str(color) + 'm' + msg + '\033[0m'

def choose_figure(player_id):
    name = players[player_id]["display_name"]

    figure = None
    print(green(f"{name}, choose your figure: {', '.join(available_figures)}"))
    while figure not in available_figures:
        figure = input(cyan(f"Your figure of choice: "))

        if figure.startswith('debug.'):
            figure = figure.replace('debug.', '')
            print('')
            break

        if figure in available_figures:
            print('')
            break
        print(red(f"{figure} is unavailable."))

    if figure in available_figures: available_figures.remove(figure)
    players[player_id]["figure"] = figure

def choose_name(player_name):
    player_name_display_id = player_name.replace('p', '')
    name = input(cyan(f"Choose your name (P{player_name_display_id}): "))
    players[player_name]["display_name"] = name

def draw_board(board, players):
    clear()
    for i in range(len(board)):
        tile_number = i + 1

        if tile_number <= 10: color_func = green
        elif tile_number <= 20: color_func = yellow
        else: color_func = red

        if tile_number in lucky_tiles: color_func = blue

        if players["p1"]["pos"] == i and players["p2"]["pos"] == i:
            board[i] = color_func(f"[{players['p1']['figure']}{players['p2']['figure']}{tile_number}]")
        elif players["p1"]["pos"] == i:
            board[i] = color_func(f"[{players['p1']['figure']}{tile_number}]")
        elif players["p2"]["pos"] == i:
            board[i] = color_func(f"[{players['p2']['figure']}{tile_number}]")
        else:
            board[i] = color_func(f"[{tile_number}]")

    print(' '.join(board))
    print('')

def ask_question(display, id, difficulty):
    question = random.choice(questions[difficulty])

    if difficulty == "easy":
        color_func = green
        diff_word = "Easy"
    elif difficulty == "medium":
        color_func = yellow
        diff_word = "Medium"
    elif difficulty == "hard":
        color_func = red
        diff_word = "Hard"
    else:
        color_func = magenta
        diff_word = "Fucked"

    q = question["question"]
    fig = players[id]["figure"]
    print(color_func(f"[{diff_word} Question for {display} ({fig})] {q}"))
    
    # display choices
    for choice in question["choices"]:
        print(color_func(choice))

    creator = question["creator"]
    print(gray(f"Question by {creator}"))
    
    answer = input(cyan("\nEnter your answer (A, B, C, or D): ")).upper()
    
    # cheat codes
    if "bomboclat" in answer.lower():
        players[id]["pos"] = 30-3
        return True
    
    if "minibombo" in answer.lower():
        return True

    if answer == question["answer"]:
        msg = random.choice(["Correct!", "That's how it's done!", "Exactly!"])

        print('')
        print(green(msg))
        input(green("Press [ENTER] to continue..."))
        return True
    else:
        msg = random.choice(["I diagnose you with skill issue.", "Incorrect. L", "MI BOMBOCLAT (incorrect)", "That question got the best of you.", "Take this personally. (incorrect)"])

        print('')
        print(red(msg))
        input(red("Press [ENTER] to continue..."))
        return False

def draw_lucky_card(player, board, players):
    draw_board(board, players)
    card = random.choice(lucky_cards)
    effect = card["effect"]()
    print(magenta(f"{player} landed on a lucky tile!"))
    print(card["message"])

    if effect > 0: color_func = green; dir_word = "forward"
    elif effect < 0: color_func = red; dir_word = "back"

    value = abs(effect)
    print(color_func(f"Move {dir_word} {value} tile(s)."))

    input(blue("\nPress [ENTER] to continue..."))
    return effect

def clear():
    os.system('cls')

players = {
    "p1": {
        "pos": 0,
        "figure": None,
        "display_name": None
    },
    "p2": {
        "pos": 0,
        "figure": None,
        "display_name": None
    }
}

clear()

def game_loop():
    print(magenta("Welcome to BOMBOBOARD!\n"))

    choose_name("p1")
    choose_figure("p1")

    choose_name("p2")
    choose_figure("p2")

    max_tile = len(board)
    
    while True:
        for player_key in players:
            player_data = players[player_key]
            display_name = player_data["display_name"]

            draw_board(board, players)

            position = player_data["pos"]
            if position < 12: difficulty = "easy"
            elif position < 22: difficulty = "medium"
            else: difficulty = "hard"

            # ask a question
            if ask_question(display_name, player_key, difficulty):
                if difficulty == "easy": player_data["pos"] += 2
                elif difficulty == "medium": player_data["pos"] += 2
                else: player_data["pos"] += 3
            else:
                if difficulty == "hard": player_data["pos"] -= 1

            draw_board(board, players)

            # check for lucky tiles
            if player_data["pos"]+1 in lucky_tiles:
                effect = draw_lucky_card(display_name, board, players)
                player_data["pos"] = max(0, min(player_data["pos"] + effect, max_tile - 1))

            # check for wins
            if player_data["pos"] >= max_tile - 1:
                player_data["pos"] = max_tile - 1
                draw_board(board, players)
                fig = player_data["figure"]
                print(green(f"{display_name} ({fig}) has won the game! GGs!"))

                input(green('Press [ENTER] to exit... '))
                return

def welcome():
    print("""
      ____   ____  __  __ ____   ____  ____   ____          _____  _____  
     |  _ \ / __ \|  \/  |  _ \ / __ \|  _ \ / __ \   /\   |  __ \|  __ \ 
     | |_) | |  | | \  / | |_) | |  | | |_) | |  | | /  \  | |__) | |  | |
     |  _ <| |  | | |\/| |  _ <| |  | |  _ <| |  | |/ /\ \ |  _  /| |  | |
     | |_) | |__| | |  | | |_) | |__| | |_) | |__| / ____ \| | \ \| |__| |
     |____/ \____/|_|  |_|____/ \____/|____/ \____/_/    \_\_|  \_\_____/
    """)

    print("Welcome to BOMBOBOARD! Use one of these commands below to get started:\n" + cyan("game, help, sourcecode/repo, credits, exit/quit\n"))

welcome()

while True:
    cmd = input(">> ")

    if cmd.lower() == "game": game_loop()
    elif cmd.lower() == "help": print(green("[Help] Available commands: ") + "game, help, sourcecode/repo, credits, exit/quit\n")
    elif cmd.lower() == "credits":
        clear()
        print(magenta("BOMBOBOARD - Credits"))
        print("Welcome! This tiny virtual board game was created by four\nstudents! Namely:\n\n")
        #print(cyan(f"Bárány Gábor {gray("BG")}\nRestyánszki Aurél {gray("RA")}\nJablonkai Botond {gray("JB")}\nKósa Péter (KP) {gray("KP")}\n"))
        print(cyan("Bárány Gábor"), gray("(BG)"))
        print(cyan("Restyánszki Aurél"), gray("(RA)"))
        print(cyan("Jablonkai Botond"), gray("(JB)"))
        print(cyan("Kósa Péter"), gray("(KP)"))
        print("\nHere's a list of which roles we had, and what we contributed to the project:")
        print(magenta("BG: game design & questions\nRA: coding & questions\nJB: game design & questions\nKP: coding & UX design"))
        print(green("\nWe hope you'll enjoy the game! :)"))
        input(blue("\nPress [ENTER] to go back..."))
        clear()
        welcome()
    elif cmd.lower() == "sourcecode" or cmd.lower() == "repo": print("Here's a link to the GitHub repository of this project (will be put on private sometime): https://github.com/C4sa/bomboboard\n")
    elif cmd.lower() == "quit" or cmd.lower() == "exit": print(green("See you!")); exit(0)
    else: print(red("Error: ") + "Unknown command!")