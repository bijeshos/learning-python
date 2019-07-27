print("-------------")
# list operations
movies = ["avtar", "titanic"]
print(movies)
print("movies length: " + str(len(movies)))
print(movies[1])
movies.append("cars 3")
print(movies)
movies.extend(["toys story 1", "monsters inc"])
print(movies)
movies.pop()
print(movies)
movies.remove("avtar")
print(movies)
movies.insert(0, "up")
print(movies)
movies.insert(0, "incredibles")
print(movies)
movies.insert(0, 1)
movies.insert(2, 2)
num = movies[0]
print(movies)
print("-------------")

# for loop
for item in movies:
    print(item)
print("-------------")

# while loop
count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1
print("-------------")

# add another list to the list
movies.insert(0, ["ted", "king kong"])
print(movies)

# iterating a list within a list : option 1
for item in movies:
    if isinstance(item, list):
        for movie in item:
            print(movie)
    else:
        print(item)
print("-------------")


# a function to iterate a list
def iterate_list(input_list):
    for list_item in input_list:
        print(list_item)


print("-------------")
# iterating a list within a list : option 2
for item in movies:
    if isinstance(item, list):
        iterate_list(item)
    else:
        print(item)

print("-------------")


# a function to iterate a list recursively
def recursive_iterate_list(input_list):
    for list_item in input_list:
        if isinstance(list_item, list):
            recursive_iterate_list(list_item)
        else:
            print(list_item)


recursive_iterate_list(movies)
