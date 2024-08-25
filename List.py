marks = [94.5,98.9,67.6,45.6,87.8]
print(type(marks), len(marks), marks)
print(marks[1])
marks[1] = 56.9
print(marks[1])

print(marks[1:3])
print(marks[:len(marks)])

marks.append(75.8)
marks.sort(reverse=True)
marks.insert(2,35.6)
print(marks)
