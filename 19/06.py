def find_farthest_orbit(list_of_orbits):
    areas = list()
    [areas.append(list_of_orbits[i][0] * list_of_orbits[i][1]) for i in range(len(list_of_orbits))]
    for i in range(len(areas)):
        if list_of_orbits[i][0] == list_of_orbits[i][1]:
            areas[i] = 0

    return list_of_orbits[areas.index(max(areas))]
