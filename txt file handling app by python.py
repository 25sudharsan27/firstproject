print("Welcome copy paste file system")
def wri():
    fin=open("a.txt","w")
    d=input("Enter your word to copy: ")
    fin.write(d)
    fin.close()

    fin=open("a.txt","r")
    fin1=open("b.txt","w")
    c=fin.read()
    fin1.write(c)
    fin.close()
    fin1.close()
def cop():
    fin = open("a.txt", "r")
    fin1 = open("b.txt", "w")
    c = fin.read()
    fin1.write(c)
    fin.close()
    fin1.close()
def re():
    d=input("Enter file name to read: ")
    try:
        fin=open(d,"r")
        print("--------------------------------")
        print(fin.read())
        print("--------------------------------")
    except FileNotFoundError:
        print("File is not found please enter the file name correctly")

def wr():
    d=input("Enter file name to write: ")
    c=input("Enter a word to write: ")
    try:
        fin=open(d,"w")
        fin.write(c)
    except FileNotFoundError:
        print("File is not found please enter the file name correctly")





print("\*  /\*  /  |>  |  |-  |-|  |_|_|  |>")
print(" \*/  \*/   |_  |_ |_  |_|  | | |  |_")

for i in range(10000000):
    print("---------------------")
    print("1.Write and copy")
    print("2.Just copy")
    print("3:Exit")
    print("4:Read file")
    print("5:Write file")
    print("----------------------")
    ch=int(input("Enter your choice:"))
    if ch==1:
        wri()
    if ch==2:
        cop()
    if ch==3:
        print("-------------------------------------------------------------")

        print("------  |   |    /|  |   |  | /      \  /  |---|  |    |")
        print("  |     |___|   / |  |___|  |/        \/   |   |  |    |")
        print("  |     |   |  /__|  |   |  |\         |   |   |  \*   /")
        print("  |     |   | /   |  |   |  | \*       |   |___|   \__/")

        print("------------------------------------------------------------")

        break
    if ch==4:
        re()
    if ch==5:
        wr()
    else:
        print("please enter a correct choice")







