

data = [[3, 10], [1, 20], [2, 15]]

data.sort()

data.sort(key=lambda x:x[1])


print(data)


nums = [42, 15, 37, 21, 8]

nums.sort(key=lambda x:x%10)



words = ["apple", "kiwi", "banana", "grape"]
words.sort(key=len)


students = [
    ["Tom", 85],
    ["Anna", 92],
    ["John", 78]
]

students.sort(key=lambda x:x[1])

students1 = [
    ["Tom", 85],
    ["Anna", 92],
    ["John", 78]
]

students1.sort()

data = [(3, 10), (1, 20), (2, 15)]
data.sort(key=lambda x:x[1])


nums = [-10, 5, -2, 8]
nums.sort(key=abs)

words = ["cat", "apple", "dog", "ball"]

words.sort(key=lambda x:x[0][1])

#1.nums.sort(key=lambda x:x%10)
#2.words.sort(key=len)
#students.sort(key=lambda x:x[1])
#students1.sort()
#data.sort(key=lambda x:x[1])
