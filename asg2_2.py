def cabin():
    cabin= input("the cabin class of a cruise ship (Lux/A/B/C): ")
    if cabin == "Lux" or (cabin == "lux"):
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin == "A" or (cabin == "a"):
        print("A: above the car deck, equipped with a window.")
    elif cabin == "B" or (cabin == "b"):
        print("B: windowless cabin above the car deck.")
    elif cabin == "C" or (cabin == "c"):
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")

cabin()