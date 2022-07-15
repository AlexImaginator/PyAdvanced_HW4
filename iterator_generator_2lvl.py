

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.cursor = 0
        self.cursor_nested = 0
        return self

    def __next__(self):
        if self.cursor < len(self.list_of_lists):
            if self.cursor_nested < len(self.list_of_lists[self.cursor]):
                flat_list_item = self.list_of_lists[self.cursor][self.cursor_nested]
                self.cursor_nested += 1
                if self.cursor_nested >= len(self.list_of_lists[self.cursor]):
                    self.cursor_nested = 0
                    self.cursor += 1
                return flat_list_item
            else:
                self.cursor += 1
                return None
        else:
            raise StopIteration


def flat_generator(list_of_lists):
    for nest_list in list_of_lists:
        for element in nest_list:
            yield element


print('ITERATOR' + '-'*15)
for item in FlatIterator(nested_list):
    print(item)

print('-'*20)
print([item for item in FlatIterator(nested_list)])

print('GENERATOR' + '-'*15)
for item in flat_generator(nested_list):
    print(item)
