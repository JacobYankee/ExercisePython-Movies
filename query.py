from movies import Movies

movies = Movies('./movies.txt')

choice = ""
while choice != "q":
    print("Menu options: \n q: quit")
    choice = input()
    if choice =="q":
        print("exiting menu")
        break