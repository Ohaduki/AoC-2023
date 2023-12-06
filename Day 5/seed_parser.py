def seed_parser():
    seeds = []
    with open("seeds.txt") as seedsfile:
        nums = [int(num) for num in seedsfile.read().split()]
        for i in range(0, len(nums), 2):
            seeds.append([nums[i], nums[i+1]])

        
    return seeds