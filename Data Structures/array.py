class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def get(self, index):
        """
        Get a value from the array
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def set(self, index, value):
        """
        Set values in the array
        :param index:
        :param value:
        :return:
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value

    def __len__(self):
        """
        Len of array
        :return:
        """
        return self.size

    def insert(self, index, value):
        """
        Insert a value into the array
        :param index:
        :param value:
        :return:
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == len(self.data):
            self.resize(2 * self.size)
        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index] = value
        self.size += 1

    def remove(self, value):
        """
        Remove a value from the array
        :param value:
        :return:
        """
        for i in range(self.size):
            if self.data[i] == value:
                self.delete(i)
                return
        raise ValueError("Value not found")

    def delete(self, index):
        """
        Delete a value from the array
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        if self.size <= len(self.data) // 4:
            self.resize(len(self.data) // 2)

    def resize(self, new_size):
        """
        Resize the array
        :param new_size:
        :return:
        """
        new_data = [None] * new_size
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data


arr = Array(5)

arr.set(0, 10)
arr.set(1, 20)
arr.set(2, 30)
arr.set(3, 40)
arr.set(4, 50)

print(arr)  # [10, 20, 30, 40, 50]

value = arr.get(2)
print(value)  # 30

arr.insert(2, 25)
print(arr)  # [10, 20, 25, 30, 40, 50]

arr.remove(25)
print(arr)  # [10, 20, 30, 40, 50]

arr.delete(3)
print(arr)  # [10, 20, 30, 50]

arr.resize(3)
print(arr)  # [10, 20, 30]
