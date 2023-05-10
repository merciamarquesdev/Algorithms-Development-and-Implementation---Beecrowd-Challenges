def intervalo():
    x = float(input())
    if (0.0 <= x and x <= 25.0):
        print("Intervalo [0,25]")
    elif (25.0 < x and x <= 50.0):
        print("Intervalo (25,50]")
    elif (50.0 < x and x <= 75.0):
        print("Intervalo (50,75]")
    elif (75.0 < x and x <= 100.0):
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")
        
intervalo()
