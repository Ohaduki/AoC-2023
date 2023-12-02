import re

def power_check(game):
    reds = re.findall(r"\d+ red", game)
    blues = re.findall(r"\d+ blue", game)
    greens = re.findall(r"\d+ green", game)

    red_nums = map(lambda x: int(x.split()[0]), reds)
    blue_nums = map(lambda x: int(x.split()[0]), blues)
    green_nums = map(lambda x: int(x.split()[0]), greens)

    return max(red_nums) * max(blue_nums) * max(green_nums)