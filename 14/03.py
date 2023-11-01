def quarter(xcoord, ycoord):
    if xcoord > 0:
        if ycoord > 0:
            result = "I"
        elif ycoord < 0:
            result = "IV"
    elif xcoord < 0:
        if ycoord > 0:
            result = "II"
        if ycoord < 0:
            result = "III"
    print(result, "чечверть.")


quarter(float(input()), float(input()))
