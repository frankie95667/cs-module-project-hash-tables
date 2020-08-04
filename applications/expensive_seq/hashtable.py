import math

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity



    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_prime = 1099511628211
        hash = 14695981039346656037
        for c in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(c)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for b in key:
            hash = (hash * 33) + ord(b)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        insert_location = self.buckets[self.hash_index(key)]
        if insert_location is None:
            self.buckets[self.hash_index(key)] = HashTableEntry(key, value)
            self.load += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
        else:
            node = self.buckets[self.hash_index(key)]
            if node.key == key:
                node.value = value
                return
            while node.next:
                if node.next.key == key:
                    node.next.value = value
                    return
                node = node.next
            node.next = HashTableEntry(key, value)
                    
            


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        node = self.buckets[self.hash_index(key)]
        if node is not None:
            if node.next:
                if node.key == key:
                    self.buckets[self.hash_index(key)] = node.next
                    return
                while node is not None:
                    if node.next is not None and node.next.key == key:
                        if node.next.next is not None:
                            node.next = node.next.next
                        else:
                            node.next = None
                        break
                    node = node.next
            else:
                if node.key == key:
                    self.buckets[self.hash_index(key)] = None
                    self.load -= 1
                    if self.get_load_factor() < 0.2 and self.capacity > 8:
                        if self.capacity / 2 >= 8:
                            self.resize(math.floor(self.capacity / 2))
                        else:
                            self.resize(MIN_CAPACITY)

                else:
                    return
        else:
            return

                


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        node = self.buckets[self.hash_index(key)]
        if node:
            if node.key == key:
                return node.value
            else:
                while node.next:
                    if node.next.key == key:
                        return node.next.value
                    node = node.next
        else:
            return node
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        new_buckets = self.buckets
        self.buckets = [None] * self.capacity
        for node in new_buckets:
            if node:
                self.put(node.key, node.value)
                if node.next:
                    while node.next:
                        self.put(node.next.key, node.next.value)
                        node = node.next
            



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
