from card_check import card_check

class Cards:
    def __init__(self, input):
        self.input = input
        self.cards = {i: 1 for i in range(1, 197)}
    
    def check_card(self, cardLine, card):
        winnings = card_check(cardLine)
        for i in range(1, winnings + 1):
            self.cards[card + i] += self.cards[card]
    
    def check_cards(self):
        with open(self.input, "r") as file:
            lines = file.readlines()
            for i in range(0, 196):
                self.check_card(lines[i], i+1)
    
    def print_cards(self):
        sum = 0
        for card in self.cards:
            sum += self.cards[card]
        print(sum)