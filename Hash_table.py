class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        output = 0
        for char in string:
            output += ord(char)
        return output

    def add(self, key, value):
        hash_value = self.hash(key)

        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        else:
            self.collection[hash_value] = {key: value}

    def remove(self, key):
        hash_value = self.hash(key)

        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]

    def lookup(self, key):
        hash_value = self.hash(key)

        if hash_value not in self.collection:
            return None

        return self.collection[hash_value].get(key)


hashtable = HashTable()
hashtable.add("a", 100)
print(hashtable.lookup("a"))  # 100

print(hashtable.lookup('b'))

hashtable.remove("a")
print(hashtable.lookup("a"))  # None
