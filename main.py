
class Stack1():

    def __init__(self, stack:str=''):
        self.stack = list(stack)

    def isEmpty(self):
        return False if len(self.stack) > 0 else True

    def push(self, item:str):
        self.stack += item

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)



def is_balanced(some_stack:Stack1):
    if not some_stack.isEmpty() and not some_stack.size() % 2:
        right_stack = Stack1()
        while some_stack.size() > 1:
            last_item = some_stack.pop()
            next_item = some_stack.peek()
            is_closed = (next_item + last_item) in pairs
            if right_stack.size() > some_stack.size():
                flag = False
                break
            if not is_closed:
                right_stack.push(last_item)
                continue
            some_stack.pop()
            flag = True
            while not right_stack.isEmpty():
                next_item = some_stack.pop()
                last_item = right_stack.pop()
                is_closed = (next_item + last_item) in pairs
                if not is_closed:
                    flag = False
    else:
        flag = False
    return flag


def test():
    stack = Stack1('(((([{}]))))')
    assert is_balanced(stack)
    stack = Stack1('[([])((([[[]]])))]{()}')
    assert is_balanced(stack)
    stack = Stack1('{{[()]}}')
    assert is_balanced(stack)
    stack = Stack1('}{}')
    assert not is_balanced(stack)
    stack = Stack1('{{[(])]}}')
    assert not is_balanced(stack)
    stack = Stack1('[[{())}]')
    assert not is_balanced(stack)
    stack = Stack1('()((((((((((((((((((')
    assert not is_balanced(stack)
    print('Все тесты прошли успешно!')


if __name__ == '__main__':

    test()