def find_farthest_orbit(list_of_orbits):
    areas = list_of_orbits[::]
    for i in range(len(list_of_orbits)):
        if list_of_orbits[i][0] == list_of_orbits[i][1]:
            areas[i] = 0
            continue
        areas[i] = list_of_orbits[i][0] * list_of_orbits[i][1]

    return list_of_orbits[areas.index(max(areas))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))