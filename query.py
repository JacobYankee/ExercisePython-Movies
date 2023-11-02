from movies import Movies

movies = Movies('./movies.txt')

choice = ""

with open("movies.txt", "r", encoding='utf-8') as data:
    list = data.readlines()
while choice != "q":
    print("Menu options: \n q: quit \n list: list all movies \n sn: search movie names \n sc: search casts")
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
    elif choice =="sn":
        print("Enter a word to search: ")
        word = input()
        row_idy = 0
        for line in list:
            if row_idy%3 == 0:
                if word.lower() in line.lower():
                    print(line, end="");
            row_idy += 1
    elif choice == "sc":
        print("Enter a word to search:")
        word = input()
        row_idz = 0
        castlist= []
        count = 0
        for line in list:
            if row_idz%3==0:
                temp = line

            if row_idz%3==1:
                cast = line.rstrip().split(",")
                for name in cast:
                    if word.lower() in name.lower():
                        castlist.append(name)
                        count+=1
                        print(temp, end="")
                        print(castlist)
            if row_idz%3==2:
                castlist.clear()
                temp = ""
            row_idz +=1
