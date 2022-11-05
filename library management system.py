books=['Java','python','c++','atomic habits']
books_ol=['Java','python','c++','atomic habits']
print("""1.display list of books
2.withdraw books
3.borrow books
4.add new book""")
for r in range(1000000):
    ch=int(input("Enter your choice: "))
    if ch==1:
        for val in books:
            print(val)
    elif ch==2:
        b1=input("Enter book name to withdraw:")
        if b1 in books:
            books.remove(b1)
        else:
            print(b1,"book is out of stock")
    elif ch==3:
        b2=input("Enter book name to return:")
        if b2 not in books:
            books.append(b2)
        elif b2 in books:
            books.append(b2)
    elif ch==4:
        b3=input("Add a new book:")
        books.append(b3)
print("hi")