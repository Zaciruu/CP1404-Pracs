COLOUR_WHEEL = {"lawnGreen:": "#7cfc00",
                "lavenderBlush": "#fff0f5",
                "hotPink": "#ff69b4",
                "indianRed": "#cd5c5c",
                "magenta": "#ff00ff",
                "mistyRose": "#ffe4e1",
                "oliveDrab": "#6b8e23",
                "powderBlue": "#b0e0e6",
                "red": "#ff0000",
                "yellow": "#ffff00"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOUR_WHEEL:
        print(colour, "is", COLOUR_WHEEL[colour])
    else:
        print("Invalid Colour")
    colour = input("Enter a colour: ").lower()
