import re

from range_checker import full_checker
from seed_parser import seed_parser

def main():
    with open("maps.txt") as mapsfile:
        maps_input = re.split(r".+-to-.+ map:", mapsfile.read())
        maps = []
        for i in maps_input:
            rows = i.split("\n")
            if len(rows) > 1:
                new_map = []
                for row in rows:
                    if len(row) > 0:
                        new_map.append([int(x) for x in row.split()])
                maps.append(new_map)
    
    seeds = seed_parser()
    
    full_checker(seeds, maps)

if __name__ == "__main__":
    main()


