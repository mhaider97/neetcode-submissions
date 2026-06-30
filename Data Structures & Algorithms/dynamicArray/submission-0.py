class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        elem = self.arr[self.length - 1]
        self.length -= 1
        return elem

    def resize(self) -> None:
        newCapacity = 2 * self.capacity
        newArr = [0] * newCapacity

        for index in range(self.length):
            newArr[index] = self.arr[index]
        
        self.arr = newArr
        self.capacity = newCapacity

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity
