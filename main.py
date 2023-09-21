from stack import Stack
from stack import StackOverflowError
from stack import StackUnderflowError

def main():
        # 使用方式
    s = Stack(capacity=3)
    s.push(1)
    s.push(2)
    s.push(3)

    try:
        s.push(4)  # 觸發 StackOverflowError
    except StackOverflowError:
        print("堆疊溢位")

    print(s.pop())  # 3
    print(s.peek()) # 2
    print(s.size()) # 2

    s.pop()
    s.pop()

    try:
        s.pop()  # 觸發 StackUnderflowError
    except StackUnderflowError:
        print("堆疊下溢")


if __name__ == "__main__":
    main()