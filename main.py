import random
import os

# vars
board = [i for i in range(1, 31)]
lucky_tiles = [i for i in range(1, 31)]
all_figures = ['*', '!', '>', '<', '#', '$', '%', 'Σ']
available_figures = all_figures

questions = {
    "easy": [
        {
            "question": "E1",
            "choices": ["A) This is incorrect", "B) This too", "C) I am correct!", "D) C is correct"],
            "answer": "C"
        }
    ],
    "medium": [
        {
            "question": "M1 - your mom",
            "choices": ["A) no u", "B) correct", "C) incorrect"],
            "answer": "B"
        }
    ],
    "hard": [
        {
            "question": "H1 - vewy hawd",
            "choices": ["A) this is easy", "B) no it's not", "C) what?", "D) pick me please"],
            "answer": "D"
        }
    ]
}

lucky_cards = [
    {"message": "You found a shortcut! Move forward", "effect": lambda: random.randint(1, 4)},
    {"message": "You forgot your homework. Move backward", "effect": lambda: -random.randint(1, 3)},
    {"message": "A friendly dog guides you forward. Move forward", "effect": lambda: random.randint(1, 4)},
    {"message": "You tripped on a rock. Move backward", "effect": lambda: -random.randint(1, 3)}
]

# Colors
def gray(str):
    return col(str, 30)

def red(str):
    return col(str, 31)

def green(str):
    return col(str, 32)

def yellow(str):
    return col(str, 33)
    
def cyan(str):
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

        if tile_number in lucky_cards: color_func = magenta

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
        input(red("Press [ENTER] to continue..."))
        return True
    else:
        msg = random.choice(["I diagnose you with skill issue.", "Incorrect. L", "MI BOMBOCLAT (incorrect)", "That question got the best of you.", "Take this personally. (incorrect)"])

        print('')
        print(red(msg))
        input(red("Press [ENTER] to continue..."))
        return False

def draw_lucky_card(player):
    card = random.choice(lucky_cards)
    effect = card["effect"]()
    print(f"{player} landed on a lucky tile! {card['message']} {abs(effect)} step(s).")
    
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

choose_name("p1")
choose_figure("p1")

choose_name("p2")
choose_figure("p2")

clear()

def main_loop():
    max_tile = len(board)
    
    while True:
        for player_key in players:
            player_data = players[player_key]
            display_name = player_data["display_name"]

            draw_board(board, players)

            position = player_data["pos"]
            if position < 11: difficulty = "easy"
            elif position < 21: difficulty = "medium"
            else: difficulty = "hard"

            #print(f"@@@ board length: {len(board)}")

            # ask a question
            if ask_question(display_name, player_key, difficulty):
                if difficulty == "easy": player_data["pos"] += 2
                elif difficulty == "medium": player_data["pos"] += 2
                else: player_data["pos"] += 3
            else:
                if difficulty == "hard": player_data["pos"] -= 1  

            # check for lucky tiles
            if player_data["pos"] in lucky_tiles:
                print("@@@ lucky tile!!!!")
                effect = draw_lucky_card(display_name)
                player_data["pos"] = max(0, min(player_data["pos"] + effect, max_tile - 1))

            # check for wins
            if player_data["pos"] >= max_tile - 1:
                draw_board(board, players)
                fig = player_data["figure"]
                print(green(f"{display_name} ({fig}) has won the game! GGs!"))

                input('Press [ENTER] to exit... ')
                return

main_loop()