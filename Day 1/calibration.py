def calibration(line):
    nums = []
    for char in line:
        try:
            nums.append(int(char))
        except:
            pass
    return nums[0]*10 + nums[-1]



