tup = (10,20,30,40,30,400,30)
print(type(tup))
print(tup.index(30))
print(tup.count(30))

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movie = []
movie.append(input("Enter movie :"))
movie.append(input("Enter movie :"))
movie.append(input("Enter movie :"))

print(movie)

movie = []
mov1 = (input("Enter Movie :"))
mov2 = (input("Enter Movie :"))
mov3 = (input("Enter Movie :"))

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)

print(movie)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1= [1,2,3,4,5]
list2 = [1,2,1]

list1_copy = list1.copy()
list1_copy.reverse()

list2_copy = list2.copy()
list2_copy.reverse()

if(list1 == list1_copy):
    print("list1 is palindrome")
else:
    (print("list1 is not palindrome")) 

if(list2 == list2_copy):
    print("list2 is a palindrome")       
else:
    print("list2 is not a palindrome")


# WAP to count the number of students with the “A” grade in the following tuple.

tup = ("a","b","c","d","f","a","c")
print(tup.count("a"))


grade = ["a","b","c","d","f","a","c"]
grade.sort()
print(grade)