from ItemSorter import FIFO, HANOI


def fifo():
    sort = FIFO()
    queue = sort.sorter

    food_chest = []
    misc_chest = []
    discard_chest = []
    # FIFO
    running = 0
    print("ANY TYPOGRAPHICAL ERROR WITH ITEM ID WILL BE IMMEDIATELY DISCARDED")
    while running != 3:
        items = input("Please type in the Item You ordered\n")
        item_ID = input("Categories are food (FOOD) and miscellaneous (MISC)\n")
        sort.add_item_to_sorter(items)
        print(queue)

        # sorts immediately as you type
        if item_ID == "FOOD":
            food_chest.append(sort.remove_item_from_sorter())
        elif item_ID == "MISC":
            misc_chest.append(sort.remove_item_from_sorter())
        else:
            discard_chest.append(sort.remove_item_from_sorter())

        print(food_chest)
        print(misc_chest)
        print(discard_chest)

        running += 1




lefo = HANOI

def compare_val(destined_stack, init_stack):
    check = lifo.check_if_empty(destined_stack)
    check_2 = lifo.check_if_empty(init_stack)
    if check and check_2 is False:
        # happens kapag may laman ang both na stack
        element_1 = check.get(destined_stack[-1])
        element_2 = check.get(init_stack[-1])
        if element_1 > element_2:
            destined_stack.append(init_stack.pop([-1]))
        else:
            print("You can't place a bigger value on top of a lesser value")
    elif check or check_2 is True:
        # happens kapag walang laman ang isa sa mga stack
        destined_stack.append(init_stack.pop([-1]))