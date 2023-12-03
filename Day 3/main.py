from num_finder import num_finder

def main():
    nums = []
    symbols = []
    sum=0
    with open("input.txt", "r") as f:
        for line in f:
            results = num_finder(line)
            nums.append(results[0])
            symbols.append(results[1])
    for i in range(len(symbols)):
        for col in symbols[i]:
            for num in nums[i-1]:
                if ({col[0]-1, col[0], col[0]+1} & set(num[1])):
                    if col[1] != 0:
                        col[1] *= num[0]
                        sum += col[1]
                    else:
                        col[1] = num[0]
            for num in nums[i]:
                if ({col[0]-1, col[0], col[0]+1} & set(num[1])):
                    if col[1] != 0:
                        col[1] *= num[0]
                        sum += col[1]
                    else:
                        col[1] = num[0]
            for num in nums[i+1]:
                if ({col[0]-1, col[0], col[0]+1} & set(num[1])):
                    if col[1] != 0:
                        col[1] *= num[0]
                        sum += col[1]
                    else:
                        col[1] = num[0]
    print(sum)

if __name__ == "__main__":
    main()