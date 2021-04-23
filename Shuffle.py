def shuffle(deck, show = True):
    temp_deck = []
    length = len(deck)
    for i in range(int(length/2)):
        temp_deck.append(deck[i])
        temp_deck.append(deck[i + int(length/2)])

    if show:
        print(temp_deck)

    return temp_deck

def i_shuffle(deck, show = True):
    temp_deck = []
    length = len(deck)
    for i in range(int(length/2)):
        temp_deck.append(deck[i + int(length/2)])
        temp_deck.append(deck[i])        

    if show:
        print(temp_deck)

    return temp_deck

def check_perfect(deck, base, describe = True):
    if len(deck) == len(base):
        for i in range(len(deck)):
            if deck[i] != base[i]:
                if describe:
                    print("Not A Perfect Deck!")
                return False
        if describe:
            print("Perfect Deck!")
        return True
    else:
        print("Current deck not the same size as base deck")


if __name__ == "__main__":
    
    # Making the base deck
    deck = []
    types = ["h", "c", "d", "s"]
    half = int(len(types)/2)
    quantity_per_type = 13
    for ty in types[:half]:
        for i in range(quantity_per_type):     
            deck.append(ty + str(i+1))

    for ty in types[half:]:
        for i in range(quantity_per_type):     
            deck.append(ty + str(quantity_per_type-i))

    deck_base = deck

    order = ["o", "i"]
    # order = ["o", "i", "i", "o", "i", "i", "i"]
    # order = ["o", "o", "o", "o", "o", "o", "o", "i"]
    perfect = False
    count = 0
    while not perfect:
        for shuf in order:
            if shuf == "o":
                deck = shuffle(deck, show = False)
            elif shuf == "i":
                deck = i_shuffle(deck, show = False)

        perfect = check_perfect(deck, deck_base, describe = False)
        count += len(order)
    print(count)