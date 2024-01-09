def quarter(xcoord, ycoord):
    if ycoord == 0:
        print("Ось X.")
    elif xcoord == 0:
        print("Ось Y.")
    elif xcoord > 0:
        if ycoord > 0:
            result = "I"
        elif ycoord < 0:
            result = "IV"
        print(result, "четверть.")
    elif xcoord < 0:
        if ycoord > 0:
            result = "II"
        if ycoord < 0:
            result = "III"
        print(result, "четверть.")
