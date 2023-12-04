import re

def card_check(card):
    nums = re.findall(r"\d+", card)
    winningNums = [int(num) for num in nums[1:11]]
    restOfNums = [int(num) for num in nums[11:]]
    winnings = 0
    for num in restOfNums:
        if num in winningNums:
            winnings += 1
    return winnings

