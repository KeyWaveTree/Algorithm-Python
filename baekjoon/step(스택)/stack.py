import sys

class Stack:
    def __init__(self, size):
        self._space =[0]*(size+1)
        self._top = 0
        self._size = size

    def push(self, get_value):
        self._top+=1
        self._space[self._top] = get_value

    def pop(self)-> int:
        if self._top == 0 : return -1
        pop = self._space[self._top]
        self._top -= 1
        self._space.pop()
        return pop

    def is_empty(self)->bool:
        if self._top == 0: return True
        else: return False

    def value_count(self)->int: return self._top

    def is_value(self)->int:
        if self._top == 0: return -1
        return self._space[self._top]

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    stack = Stack(n)

    for _ in range(n):
        command = sys.stdin.readline().split()
        if command[0] == '1': stack.push(command[1])
        elif command[0] == '2': print(stack.pop())
        elif command[0]== '3': print(stack.value_count())
        elif command[0]== '4': print(int(stack.is_empty()))
        elif command[0] == '5': print(stack.is_value())