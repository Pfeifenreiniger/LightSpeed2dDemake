

class Player:
    def __init__(self, pn):
        self.pn = pn
        if self.pn == 1:
            self.row = 1
            self.column = 1
        else:
            self.row = 1
            self.column = 2

        if self.pn == 1:
            self.cells_dict = {
                "r1c1": True,
                "r1c2": False,
                "r1c3": False,
                "r1c4": False,
                "r1c5": False,
                "r1c6": False,
                "r2c1": True,
                "r2c2": False,
                "r2c3": False,
                "r2c4": False,
                "r2c5": False,
                "r2c6": False,
                "r3c1": False,
                "r3c2": False,
                "r3c3": False,
                "r3c4": False,
                "r3c5": False,
                "r3c6": False,
                "r4c1": False,
                "r4c2": False,
                "r4c3": False,
                "r4c4": False,
                "r4c5": False,
                "r4c6": False,
                "r5c1": False,
                "r5c2": False,
                "r5c3": False,
                "r5c4": False,
                "r5c5": False,
                "r5c6": False,
                "r6c1": False,
                "r6c2": False,
                "r6c3": False,
                "r6c4": False,
                "r6c5": False,
                "r6c6": False,
            }
        else:
            self.cells_dict = {
                "r1c1": False,
                "r1c2": True,
                "r1c3": True,
                "r1c4": False,
                "r1c5": False,
                "r1c6": False,
                "r2c1": False,
                "r2c2": False,
                "r2c3": False,
                "r2c4": False,
                "r2c5": False,
                "r2c6": False,
                "r3c1": False,
                "r3c2": False,
                "r3c3": False,
                "r3c4": False,
                "r3c5": False,
                "r3c6": False,
                "r4c1": False,
                "r4c2": False,
                "r4c3": False,
                "r4c4": False,
                "r4c5": False,
                "r4c6": False,
                "r5c1": False,
                "r5c2": False,
                "r5c3": False,
                "r5c4": False,
                "r5c5": False,
                "r5c6": False,
                "r6c1": False,
                "r6c2": False,
                "r6c3": False,
                "r6c4": False,
                "r6c5": False,
                "r6c6": False,
            }

p1 = Player(1)
p2 = Player(2)


if p2.row == 1:
    if p2.column == 2:
        pass

for key, val in p1.cells_dict.items():
    if val:
        # in gleicher row
        if int(key[1]) == p2.row:
            if int(key[3]) - p2.column == -1:
                print("GEHE LINKS!!")
            if int(key[3]) - p2.column == 1:
                print("GEHE RECHTS!!")
        # eine row oben drüber
        if int(key[1]) - p2.row == 1:
            # celle gleich oben drüber
            if int(key[3]) == p2.column:
                print("GLEICH OBEN DRÜBER!!")
            if int(key[3]) - p2.column == -1:
                print("OBEN LINKS!!")
            if int(key[3]) - p2.column == 1:
                print("OBEN RECHTS!!")
        # eine row drunter
        if int(key[1]) - p2.row == -1:
            # celle gleich oben drüber
            if int(key[3]) == p2.column:
                print("GLEICH UNTEN DRUNTER!!")
            if int(key[3]) - p2.column == -1:
                print("UNTEN LINKS!!")
            if int(key[3]) - p2.column == 1:
                print("UNTEN RECHTS!!")



