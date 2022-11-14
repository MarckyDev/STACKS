
class FIFO:

    def __init__(self):
        self.sorter = []

    def add_item_to_sorter(self, to_be_sorted):
        return self.sorter.append(to_be_sorted)

    def remove_item_from_sorter(self):
        return self.sorter.pop(0)

    # Function to check if a queue is full
    @staticmethod
    def check_if_full(full_queue):
        if len(full_queue) == 3:
            return True
        return False

    @staticmethod
    def check_if_empty(empty_queue):
        if len(empty_queue) < 1:
            return True
        return False


class HANOI:

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
        if len(empty_queue) == 0:
            return True

