def seed_checker(seed, maps):
    current_value = seed
    for map in maps:
        for row in map:
            if row[1] <= current_value <= row[1] + row[2]:
                current_value = row[0]+(current_value-row[1])
                break
    return current_value
