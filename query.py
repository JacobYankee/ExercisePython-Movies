from movies import Movies

movies = Movies('./movies.txt')

choice = ""
enc = 'utf-8'
with open("movies.txt", "r", encoding=enc) as data:
    list = data.readlines()
while choice != "q":
    print("Menu options: \n q: quit \n list: list all movies")
    choice = input()
    if choice =="q":
        print("exiting menu")
        break
    elif choice == "list":
        row_idx = 0
        for line in list:
            if row_idx%3==0:
                print(line, end="")
            row_idx+=1