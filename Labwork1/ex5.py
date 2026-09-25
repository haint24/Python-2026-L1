List_colors = ["red", "green", "blue", "yellow", "purple"]
colors = input("What is your favorite color?")
if colors in List_colors:
    index = List_colors.index(colors)
    print("Your color is at index", index,"in my list")
else:
    print("Sorry, I could not find your color")
    
    