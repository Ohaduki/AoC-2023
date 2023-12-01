from new_calibration import calibration

def main():
    with open("input.txt", "r") as f:
        sum = 0
        for i, line in enumerate(f):
            print(f"line {i}: {line} {calibration(line)}")
            sum += calibration(line)
    print(sum)

if __name__ == "__main__":
    main()