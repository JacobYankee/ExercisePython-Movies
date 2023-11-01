from movies import Movies

movies = Movies('./movies.txt')

choice = ""
enc = 'utf-8'
with open("movies.txt", "r", encoding=enc) as data:
    list = data.readlines()
while choice != "q":
    print("Menu options: \n q: quit \n list: list all movies \n sn: search movie names")
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