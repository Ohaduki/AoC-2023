def range_checker(ranges, map):
    current_ranges = ranges
    new_ranges = []
    for map in maps

def full_checker(ranges, maps):
    current_ranges = ranges
    for map in maps:
        new_ranges = []
        for range in current_ranges:
            new_ranges += range_checker(range, map)
        current_ranges = new_ranges
    print(current_ranges)
    