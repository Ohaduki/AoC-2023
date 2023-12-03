import re

def num_finder(line):
    nums = []
    symbols = []
    mathches = re.finditer(r"\d+|\*", line)
    for match in mathches:
        try:
            value = int(match.group())
            coordinates = [i for i in range (match.start()+1, match.end()+1)]
            nums.append([value, coordinates, False])
        except:
            symbols.append([match.end(), 0])
    return [nums, symbols]