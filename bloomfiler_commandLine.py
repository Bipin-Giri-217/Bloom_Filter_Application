import hashlib

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size  
        self.bit_array = [0] * size
        self.hash_functions = hash_functions 

    def add(self, element):
        for hash_func in self.hash_functions:
            index = hash_func(element) % self.size
            self.bit_array[index] = 1

    def contains(self, element):
        for hash_func in self.hash_functions:
            index = hash_func(element) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

def main():
    size = 20
    num_hash_functions = 3

    hash_functions = [
        lambda x: int(hashlib.md5(x.encode()).hexdigest(), 16),
        lambda x: int(hashlib.sha1(x.encode()).hexdigest(), 16),
        lambda x: int(hashlib.sha256(x.encode()).hexdigest(), 16)
    ]

    bloom_filter = BloomFilter(size, hash_functions)

    while True:
        print("1. Add element")
        print("2. Search for element")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            element = input("Enter element to add: ")
            bloom_filter.add(element)
            print(f"{element} added to the Bloom filter.")
        elif choice == "2":
            element = input("Enter element to search: ")
            if bloom_filter.contains(element):
                print(f"{element} may be in the set.")
            else:
                print(f"{element} is definitely not in the set.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
