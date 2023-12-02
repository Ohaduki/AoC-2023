import re

def check_game(game):
    reds = re.findall(r"\d+ red", game)
    blues = re.findall(r"\d+ blue", game)
    greens = re.findall(r"\d+ green", game)
    for instance in reds:
        if int(instance.split()[0]) > 12:
            return False
    for instance in greens:
        if int(instance.split()[0]) > 13:
            return False
    for instance in blues:
        if int(instance.split()[0]) > 14:
            return False
    return True

print(check_game("12 red, 13 green, 14 blue"))