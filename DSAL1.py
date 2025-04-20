class HashTable:
    def __init__(self):
        self.m = int(input("Enter size of hash table: "))
        self.hashTable = [None] * self.m
        self.elecount = 0
        print(self.hashTable)

    def hashFunction(self, key):
        return key % self.m

    def isfull(self):
        return self.elecount == self.m

    def linearProbe(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        while self.hashTable[index] is not None:
            index = (index + 1) % self.m
            compare += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print("Data inserted at index", index)
        print(self.hashTable)
        print("Number of comparisons:", compare)

    def getLinear(self, key, data):
        index = self.hashFunction(key)
        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            index = (index + 1) % self.m
        return None

    def quadraticProbe(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        i = 0
        while self.hashTable[index] is not None:
            index = (index + i * i) % self.m
            compare += 1
            i += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print("Data inserted at index", index)
        print(self.hashTable)
        print("Number of comparisons:", compare)

    def getQuadratic(self, key, data):
        index = self.hashFunction(key)
        i = 0
        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            i += 1
            index = (index + i * i) % self.m
        return None

    def insertViaLinear(self, key, data):
        if self.isfull():
            print("Table is full")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print("Data inserted at index", index)
            print(self.hashTable)
        else:
            print("Collision occurred, applying Linear Probing")
            self.linearProbe(key, data)

    def insertViaQuadratic(self, key, data):
        if self.isfull():
            print("Table is full")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print("Data inserted at index", index)
            print(self.hashTable)
        else:
            print("Collision occurred, applying Quadratic Probing")
            self.quadraticProbe(key, data)


def menu():
    obj = HashTable()
    ch = 0
    while ch != 3:
        print("************************")
        print("1. Linear Probe")
        print("2. Quadratic Probe")
        print("3. Exit")
        print("************************")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            ch2 = 0
            while ch2 != 3:
                print("** 1. Insert **")
                print("** 2. Search **")
                print("** 3. Exit **")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:
                    a = int(input("Enter phone number: "))
                    b = str(input("Enter name: "))
                    obj.insertViaLinear(a,b)
                elif ch2 == 2:
                    k = int(input("Enter key to be searched: "))
                    b = str(input("Enter name: "))
                    f = obj.getLinear(k,b)
                    if f is None:
                        print("Key not found")
                    else:
                        print("Key found at index", f)
        elif ch == 2:
            ch2 = 0
            obj1 = HashTable()
            while ch2 != 3:
                print("** 1. Insert **")
                print("** 2. Search **")
                print("** 3. Exit **")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:
                    a = int(input("Enter phone number: "))
                    b = str(input("Enter name: "))
                    obj1.insertViaQuadratic(a, b)
                elif ch2 == 2:
                    k = int(input("Enter key to be searched: "))
                    b = str(input("Enter name: "))
                    f = obj1.getQuadratic(k, b)
                    if f is None:
                        print("Key not found")
                    else:
                        print("Key found at index", f)
 

menu()
