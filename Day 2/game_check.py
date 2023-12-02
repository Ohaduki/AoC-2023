import re

def check_game(game):
    id = re.findall(r"Game \d+", game)[0].split()[1]
    reds = re.findall(r"\d+ red", game)
    blues = re.findall(r"\d+ blue", game)
    greens = re.findall(r"\d+ green", game)
    for instance in reds:
        if int(instance.split()[0]) > 12:
            return 0
    for instance in greens:
        if int(instance.split()[0]) > 13:
            return 0
    for instance in blues:
        if int(instance.split()[0]) > 14:
            return 0
    return int(id)