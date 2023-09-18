import hashlib
import tkinter as tk
from tkinter import messagebox

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

def add_element():
    element = entry.get()
    if element:
        bloom_filter.add(element)
        entry.delete(0, tk.END)
        messagebox.showinfo("Bloom Filter", f"{element} added to the Bloom filter.")

def search_element():
    element = entry.get()
    if element:
        if bloom_filter.contains(element):
            messagebox.showinfo("Bloom Filter", f"{element} may be in the set.")
        else:
            messagebox.showinfo("Bloom Filter", f"{element} is definitely not in the set.")
        entry.delete(0, tk.END)

def exit_program():
    window.destroy()

size = 20
num_hash_functions = 3

hash_functions = [
    lambda x: int(hashlib.md5(x.encode()).hexdigest(), 16),
    lambda x: int(hashlib.sha1(x.encode()).hexdigest(), 16),
    lambda x: int(hashlib.sha256(x.encode()).hexdigest(), 16)
]

bloom_filter = BloomFilter(size, hash_functions)

window = tk.Tk()
window.title("Bloom Filter - Made by Team Alston, Bipin, and Boris")
window.geometry("400x300")  
window.resizable(True, True)  

label = tk.Label(window, text="Enter Book Name:")
entry = tk.Entry(window)
add_button = tk.Button(window, text="Add Book by Entering Name", command=add_element)
search_button = tk.Button(window, text="Search Book", command=search_element)
exit_button = tk.Button(window, text="Exit", command=exit_program)

label.pack(pady=10)
entry.pack(pady=5)
add_button.pack(pady=5)
search_button.pack(pady=5)
exit_button.pack(pady=5)

window.mainloop()