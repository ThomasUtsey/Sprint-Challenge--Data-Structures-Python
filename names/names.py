import time
'''***!Important!*** If you are running this using PowerShell by clicking on the green play button, you will get an error that `names1.txt` is not found.  To resolve this, run it, get the error, then `cd` into the `names` directory in the `python` terminal that opens in VSCode.

Navigate into the `names` directory. Here you will find two text files containing 10,000 
names each, along with a program `names.py` that compares the two files and prints out 
duplicate name entries. Try running the code with `python3 names.py`. 
Be patient because it might take a while: approximately six seconds on my laptop. 
What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code. 
Can you get the runtime to under a second? Under one hundredth of a second?

*You may not use the built in Python list or set for this problem*

(Hint: You might try importing a data structure you built during the week)'''


class BinarySearchTree:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []


tree_one = BinarySearchTree(names_2[0])
for name_1 in names_1[1:]:
    tree_one.insert(name_1)
for name_2 in names_2:
    if tree_one.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
