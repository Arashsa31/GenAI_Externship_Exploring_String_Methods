#Task 1 - String Slicing and Indexing
task_1 = "Python is amazing!"
first = task_1[0:6]
second = task_1.split("is ")[1].split("!")[0]
reverse = task_1[::-1]

print("First word: ", first)
print("Amazing part: ", second)
print("Reversed string: ", reverse)
print()

#Task 2 - String Methods
task_2 =  " hello, python world! "
print(task_2.strip())
print(task_2.capitalize())
print(task_2.replace("world", "universe"))
print(task_2.upper())
print("")

#Task 3 - Check for Palindromes
task_3 = str(input("Enter a word: "))
palindrome = task_3[::-1]
if task_3 == palindrome:
    print(f"Yes,", task_3, "is a palindrome!")
else:
    print(f"No,", task_3, "is not a palindrome.")
