import cmath

main = input("Which calculator Lenght or Coordinate(Enter either l or c): ")

if main == "l":
    print("Lenght Calculator: ")
    xtwo = float(input("enter in x2: "))
    xone = float(input("enter in x1: "))

    ytwo = float(input("enter in y2: "))
    yone = float(input("enter in y1: "))

    x = ((( xtwo - xone ) ** 2) + ((ytwo - yone) ** 2))
    y = cmath.sqrt(x)

    print(y)

elif main == "c":
    print("Coordinate Calculator: ")
    zone = float(input("enter in x1: "))
    ztwo = float(input("enter in x2: "))

    tone = float(input("enter in y1: "))
    ttwo = float(input("enter in y2: "))

    z = ((zone + ztwo) / 2)
    t = ((tone + tone) / 2)

    print(f"[{z} , {t}]")
else:
    print("Please print in a valid statement (Error 458) ")
