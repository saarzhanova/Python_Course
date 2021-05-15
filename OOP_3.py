class Box:

    def __init__(self, size):
        self.size = size
        self.count = []

    def check(self):
        print("Free space in the box now:", self.size)
        if len(self.count) != 0:
            print('Items in the box:', ', '.join(self.count))
        else:
            print('There is nothing in the box')
        return self.size


class Create:
    def __init__(self, name,size):
        self.name = name
        self.in_the_box = 'no'
        self.size = size

    def check(self):
        print("Is", self.name, "in the box? - ", self.in_the_box)
        print('The size of the', self.name, 'is', self.size)
        return self.in_the_box

    def put_in_the(self, box):
        if box.size >= self.size:
            self.in_the_box = 'yes'
            box.size -= self.size
            box.count.append(self.name)
            print(self.name, 'is put in the box')
        else:
            print('There is no place in the box for', self.name)
        return self.check(), box.check()


krug = Create('krug', 1)
kv = Create('kvadrat', 4)
tr = Create('treugolnik', 6)
box = Box(10)
box.check()
print()
krug.put_in_the(box)
print()
kv.put_in_the(box)
print()
tr.put_in_the(box)