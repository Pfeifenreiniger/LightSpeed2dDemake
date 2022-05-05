"""
CPU opponent is - if activated - always player 2 and competes against player 1
"""

import random

prios = {
    "up" : 0,
    "left" : 0,
    "right" : 0,
    "down" : 0
}

def check_surrounding_tiles(difficulty: str, p1, p2):
    global prios
    for key, val in p1.cells.items():
        # p2 (cpu) prioritizes cells owned by p1 most
        # in case the cell is owned by p1...
        if val:
            # teleporter
            if difficulty == "hard" or difficulty == "very hard":
                # left
                if key == "r6c6" and (p2.row1 and p2.column1):
                    prios["left"] += 2
                # up
                if key == "r1c6" and (p2.row6 and p2.column1):
                    prios["up"] += 2
                # right
                if key == "r1c1" and (p2.row6 and p2.column6):
                    prios["right"] += 2
                # down
                if key == "r6c1" and (p2.row1 and p2.column6):
                    prios["down"] += 2
            # p1 cells and p2 are in same row
            if int(key[1]) == p2.return_row_number():
                # left
                if int(key[3]) - p2.return_column_number() == -1:
                    prios["left"] += 2
                # one more left
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == -2:
                        prios["left"] += 1
                # and one final more left
                if difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == -3:
                        prios["left"] += 0.5
                # right
                if int(key[3]) - p2.return_column_number() == 1:
                    prios["right"] += 2
                # one more right
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == 2:
                        prios["right"] += 1
                # and one final more right
                if difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == 3:
                        prios["right"] += 0.5
            # p1 cells are one row above p2
            if int(key[1]) - p2.return_row_number() == 1:
                # up
                if int(key[3]) == p2.return_column_number():
                    prios["up"] += 2
                # up left
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == -1:
                        prios["up"] += 1
                        prios["left"] += 1
                # up left left
                if difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == -2:
                        prios["up"] += 0.5
                        prios["left"] += 0.5
                # up right
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == 1:
                        prios["up"] += 1
                        prios["right"] += 1
                # up right right
                if difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == 2:
                        prios["up"] += 0.5
                        prios["right"] += 0.5
            # p1 cells are two rows above p2
            if difficulty == "hard" or difficulty == "very hard":
                if int(key[1]) - p2.return_row_number() == 2:
                    # up up
                    if int(key[3]) == p2.return_column_number():
                        prios["up"] += 1
                    # up up left
                    if int(key[3]) - p2.return_column_number() == -1:
                        prios["up"] += 1
                        prios["left"] += 1
                    # up up right
                    if int(key[3]) - p2.return_column_number() == 1:
                        prios["up"] += 1
                        prios["right"] += 1
            # p1 cells are three rows above p2
            if difficulty == "very hard":
                if int(key[1]) - p2.return_row_number() == 3:
                    # up up up
                    if int(key[3]) == p2.return_column_number():
                        prios["up"] += 0.5
                    # up up up left
                    if int(key[3]) - p2.return_column_number() == -1:
                        prios["up"] += 0.25
                        prios["left"] += 0.25
                    # up up up right
                    if int(key[3]) - p2.return_column_number() == 1:
                        prios["up"] += 0.25
                        prios["right"] += 0.25
            # p1 cells are one row below p2
            if int(key[1]) - p2.return_row_number() == -1:
                # down
                if int(key[3]) == p2.return_column_number():
                    prios["down"] += 2
                # down left
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == -1:
                        prios["down"] += 1
                        prios["left"] += 1
                # down right
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[3]) - p2.return_column_number() == 1:
                        prios["down"] += 1
                        prios["right"] += 1
            # p1 cells are two rows below p2
            if difficulty == "hard" or difficulty == "very hard":
                if int(key[1]) - p2.return_row_number() == -2:
                    # down down
                    if int(key[3]) == p2.return_column_number():
                        prios["down"] += 1
                    # down down left
                    if int(key[3]) - p2.return_column_number() == -1:
                        prios["down"] += 1
                        prios["left"] += 1
                    # down down right
                    if int(key[3]) - p2.return_column_number() == 1:
                        prios["down"] += 1
                        prios["right"] += 1
            # p1 cells are three rows below p2
            if difficulty == "very hard":
                if int(key[1]) - p2.return_row_number() == -3:
                    # down down down
                    if int(key[3]) == p2.return_column_number():
                        prios["down"] += 0.5
                    # down down down left
                    if int(key[3]) - p2.return_column_number() == -1:
                        prios["down"] += 0.25
                        prios["left"] += 0.25
                    # down down down right
                    if int(key[3]) - p2.return_column_number() == 1:
                        prios["down"] += 0.25
                        prios["right"] += 0.25
        # p2 (cpu) prioritizes free cells less
        # else not owned by p1...
        else:
            # in case the cell is also not owned by p2 (cpu)
            if p2.cells[key] != True:
                # free cells and p2 are in same row
                if int(key[1]) == p2.return_row_number():
                    # left
                    if int(key[3]) - p2.return_column_number() == -1:
                        prios["left"] += 1
                    # one more left
                    if difficulty == "hard" or difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == -2:
                            prios["left"] += 0.5
                    # and one final more left
                    if difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == -3:
                            prios["left"] += 0.25
                    # right
                    if int(key[3]) - p2.return_column_number() == 1:
                        prios["right"] += 1
                    # one more right
                    if difficulty == "hard" or difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == 2:
                            prios["right"] += 0.5
                    # and one final more right
                    if difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == 3:
                            prios["right"] += 0.25
                # free cells are one row above p2
                if int(key[1]) - p2.return_row_number() == 1:
                    # up
                    if int(key[3]) == p2.return_column_number():
                        prios["up"] += 1
                    # up left
                    if difficulty == "hard" or difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == -1:
                            prios["up"] += 0.5
                            prios["left"] += 0.5
                    # up left left
                    if difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == -2:
                            prios["up"] += 0.25
                            prios["left"] += 0.25
                    # up right
                    if difficulty == "hard" or difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == 1:
                            prios["up"] += 0.5
                            prios["right"] += 0.5
                    # up right right
                    if difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == 2:
                            prios["up"] += 0.25
                            prios["right"] += 0.25
                # free cells are two rows above p2
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[1]) - p2.return_row_number() == 2:
                        # up up
                        if int(key[3]) == p2.return_column_number():
                            prios["up"] += 0.5
                        # up up left
                        if int(key[3]) - p2.return_column_number() == -1:
                            prios["up"] += 0.5
                            prios["left"] += 0.5
                        # up up right
                        if int(key[3]) - p2.return_column_number() == 1:
                            prios["up"] += 0.5
                            prios["right"] += 0.5
                # free cells are three rows above p2
                if difficulty == "very hard":
                    if int(key[1]) - p2.return_row_number() == 3:
                        # up up up
                        if int(key[3]) == p2.return_column_number():
                            prios["up"] += 0.25
                        # up up up left
                        if int(key[3]) - p2.return_column_number() == -1:
                            prios["up"] += 0.12
                            prios["left"] += 0.12
                        # up up up right
                        if int(key[3]) - p2.return_column_number() == 1:
                            prios["up"] += 0.12
                            prios["right"] += 0.12
                # free cells are one row below p2
                if int(key[1]) - p2.return_row_number() == -1:
                    # down
                    if int(key[3]) == p2.return_column_number():
                        prios["down"] += 1
                    # down left
                    if difficulty == "hard" or difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == -1:
                            prios["down"] += 0.5
                            prios["left"] += 0.5
                    # down right
                    if difficulty == "hard" or difficulty == "very hard":
                        if int(key[3]) - p2.return_column_number() == 1:
                            prios["down"] += 0.5
                            prios["right"] += 0.5
                # free cells are two rows below p2
                if difficulty == "hard" or difficulty == "very hard":
                    if int(key[1]) - p2.return_row_number() == -2:
                        # down down
                        if int(key[3]) == p2.return_column_number():
                            prios["down"] += 0.5
                        # down down left
                        if int(key[3]) - p2.return_column_number() == -1:
                            prios["down"] += 0.5
                            prios["left"] += 0.5
                        # down down right
                        if int(key[3]) - p2.return_column_number() == 1:
                            prios["down"] += 0.5
                            prios["right"] += 0.5
                # free cells are three rows below p2
                if difficulty == "very hard":
                    if int(key[1]) - p2.return_row_number() == -3:
                        # down down down
                        if int(key[3]) == p2.return_column_number():
                            prios["down"] += 0.25
                        # down down down left
                        if int(key[3]) - p2.return_column_number() == -1:
                            prios["down"] += 0.12
                            prios["left"] += 0.12
                        # down down down right
                        if int(key[3]) - p2.return_column_number() == 1:
                            prios["down"] += 0.12
                            prios["right"] += 0.12

    # reduces prio if p1 is next to p2
    # p1 in same row as p2
    if p1.return_row_number() == p2.return_row_number():
        if p1.return_column_number() - p2.return_column_number() == -1:
            prios["left"] = 0
        elif p1.return_column_number() - p2.return_column_number() == 1:
            prios["right"] = 0
    # p1 in same column as p2
    if p1.return_column_number() == p2.return_column_number():
        if p1.return_row_number() - p2.return_column_number() == -1:
            prios["down"] = 0
        elif p1.return_row_number() - p2.return_column_number() == -1:
            prios["up"] = 0

    max_prio_direct = []
    max_prio_value = 0

    for key, val in prios.items():
        if val > max_prio_value:
            max_prio_value = val
            max_prio_direct.clear()
            max_prio_direct.append(key)
        elif val == max_prio_value:
            max_prio_direct.append(key)

    prios = {
        "up": 0,
        "left": 0,
        "right": 0,
        "down": 0
    }

    if difficulty == "easy":
        # in easy or hard difficulty a 50% chance that the cpu will take a random direction despite the prio
        if random.randint(1, 200) < 101:
            return random.choice(["up", "left", "right", "down"])
        else:
            return random.choice(max_prio_direct)
    # in hard difficulty a 20% chance
    elif difficulty == "hard":
        if random.randint(1, 200) < 41:
            return random.choice(["up", "left", "right", "down"])
        else:
            return random.choice(max_prio_direct)
    # in very hard difficulty a 10% chance
    elif difficulty == "very hard":
        if random.randint(1, 200) < 21:
            return random.choice(["up", "left", "right", "down"])
        else:
            return random.choice(max_prio_direct)
