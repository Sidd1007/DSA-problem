class SetADT:
    def __init__(self):
        self.elements = set()

    def add(self, element):
        self.elements.add(element)

    def remove(self, element):
        self.elements.discard(element)

    def contains(self, element):
        return element in self.elements

    def union(self, other):
        return self.elements | other.elements

    def intersection(self, other):
        return self.elements & other.elements

    def difference(self, other):
        return self.elements - other.elements

    def subset(self, other):
        return self.elements <= other.elements

if __name__ == "__main__":
    def get_set_input(prompt):
        return {int(x) for x in input(prompt).split()}

    set1 = SetADT()
    set1.elements = get_set_input("Enter elements for Set 1 (space-separated): ")
    set2 = SetADT()
    set2.elements = get_set_input("Enter elements for Set 2 (space-separated): ")

    print("Union:", set1.union(set2))
    print("Intersection:", set1.intersection(set2))
    print("Difference (Set 1 - Set 2):", set1.difference(set2))
    print("Is Set 1 a subset of Set 2?", set1.subset(set2))
    print("Is Set 2 a subset of Set 1?", set2.subset(set1))

