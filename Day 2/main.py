from power_check import power_check as check_game

def main():
    with open("input.txt", "r") as f:
        sum = 0
        for line in f:
            sum += check_game(line)
    print(sum)

if __name__ == "__main__":
    main()