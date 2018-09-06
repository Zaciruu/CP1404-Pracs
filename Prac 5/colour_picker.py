COLOUR_WHEEL = {"lawnfreen:": "#7cfc00",
                "lavenderblush": "#fff0f5",
                "hotpink": "#ff69b4",
                "indianred": "#cd5c5c",
                "magenta": "#ff00ff",
                "mistyrose": "#ffe4e1",
                "olivedrab": "#6b8e23",
                "powderblue": "#b0e0e6",
                "red": "#ff0000",
                "yellow": "#ffff00"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOUR_WHEEL:
        print(colour, "is", COLOUR_WHEEL[colour])
    else:
        print("Invalid Colour")
    colour = input("Enter a colour: ").lower()
