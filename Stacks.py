class STACKS:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.lifo_queue = [3, 2, 1]

    def see_queue(self, the_queue):
        return print(the_queue)

    def add_to_lifo_queue(self, to_be_added):
        return self.lifo_queue.append(to_be_added)

    def add_to_stack_1(self, to_be_added):
        return self.stack_1.append(to_be_added)

    def add_to_stack_2(self, to_be_added):
        return self.stack_2.append(to_be_added)

    def remove_from_lifo(self):
        return self.lifo_queue.pop(-1)

    def remove_from_stack_1(self):
        return self.stack_1.pop(-1)

    def remove_from_stack_2(self):
        return self.stack_2.pop(-1)

    @staticmethod
    def check_if_full(full_queue):
        if len(full_queue) == 3:
            return True

    @staticmethod
    def check_if_empty(empty_queue):
        if len(empty_queue) < 0:
            return True


lifo = STACKS()

full_stack_1 = lifo.check_if_full(lifo.stack_1)
full_stack_2 = lifo.check_if_full(lifo.stack_2)
full_stack_3 = lifo.check_if_full(lifo.lifo_queue)

stack_1 = lifo.stack_1
stack_2 = lifo.stack_2
stack_3 = lifo.lifo_queue


def update():
    print("Stack 1")
    lifo.see_queue(stack_1)
    print("Stack 2")
    lifo.see_queue(stack_2)
    print("Stack 3")
    lifo.see_queue(stack_3)


print('''
            STACKSSS
===================================
- This program demonstrates how stack works :>

''')

running = 0

while running == 0:
    update()

    print("Move the top disk? Y/N? ")
    choice = input()

    if choice == "Y":
        choice_3 = int(input("Which top disk of stack 1, 2 or 3?\n"))

        match choice_3:
            case 1:
                print("Stack 1 is selected")
                choice_2 = int(input("To which stack? 1, 2 or 3\n"))
                match choice_2:
                    case 1:
                        print("You can't add what you removed from the same stack")
                        pass
                    case 2:
                        lifo.add_to_stack_2(lifo.remove_from_stack_1())

                    case 3:
                        lifo.add_to_lifo_queue(lifo.remove_from_stack_1())

            case 2:
                print("Stack 2 is selected")
                choice_2 = int(input("To which stack? 1, 2 or 3\n"))
                match choice_2:
                    case 1:
                        lifo.add_to_stack_1(lifo.remove_from_stack_2())

                    case 2:
                        print("You can't add what you removed from the same stack")
                        pass

                    case 3:
                        lifo.add_to_lifo_queue(lifo.remove_from_stack_2())

            case 3:
                print("Stack 3 is selected")
                choice_2 = int(input("To which stack? 1, 2 or 3\n"))
                match choice_2:
                    case 1:
                        lifo.add_to_stack_1(lifo.remove_from_lifo())

                    case 2:
                        # compare_val(stack_2, stack_3)
                        lifo.add_to_stack_2(lifo.remove_from_lifo())

                    case 3:
                        print("You can't add what you removed from the same stack")
                        pass

    else:
        pass

