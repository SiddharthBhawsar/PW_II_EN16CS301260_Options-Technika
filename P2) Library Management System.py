# userchoice==1
# display a book :using print(): list
# lend a book: useinputs: lend, booknname,  dict: ,check if avail lendict in lenddict,
# return a book
# add a book
# q to quit c to continue: while loop
# Phase 1:use mysql.connector
# Phase 2: UI: using tkinter
# Phase 3: to convert it into executable file
# sms india
# smtp



from tkinter import *
from PIL import Image, ImageTk

# import tkinter
import mysql.connector
p= mysql.connector.connect(host="localhost",database= "Siddharth",user="root", passwd="1234")
mycursor = p.cursor()

# book = ["Python", "Java", "ML", "Concepts of Physics"]
# lend_dict = {}


def displaybook():

    mycursor.execute("select * from Book")
    dis_obj = Toplevel(screen)
    dis_obj.title("Displaying Books..")
    dis_obj.geometry("600x300")
    l=0.20
    for i,j in mycursor:

        # Label(dis_obj,text=i, bg="", height="2", font=("Calibri", 13)).pack()
        l4 = Label(dis_obj, text="Book Name",bg="grey", font=("Arial", 9,"bold"))
        l4.place(relx=.24, rely=.10)

        l5 = Label(dis_obj, text="Author",bg="grey", font=("Arial", 9, "bold"))
        l5.place(relx=0.59, rely=.10)

        l2 = Label(dis_obj, text=i, font=("Arial", 9))
        l2.place(relx=.24, rely=l)

        l3 = Label(dis_obj, text=j, font=("Arial", 9, "italic"))
        l3.place(relx=0.59, rely=l)

        l=l+.1

        # Label(text="").pack()
        # print(i)


def lend_book():
    book_namei=book_name.get()
    nami=nam.get()
    mycursor.execute("select * from Lend_dict")


    for i,j in mycursor:
        if (i==book_namei):
            lend_obj1 = Toplevel(screen)
            lend_obj1.geometry("400x200")
            lend_obj1.title("Sorry for inconveneince!")
            # mycursor.execute("select name from Lend_dict where bookname=%s", i)
            l4 = Label(lend_obj1, text=f"This book is already issued to {j}.", fg="red", font=("Arial", 9, "bold"))
            l4.place(relx=.24, rely=.10)

            l5 = Label(lend_obj1, text="Please Try Searching for some Other Book!", fg="black", font=("Arial", 9, ))
            l5.place(relx=0.24, rely=.30)
            # Label(lend_obj, text=, bg="red", font=("Calibri", 13))
            # Label(lend_obj, text=j, bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
            # print(f"Sorry, this book is already issued to  {j}")
            break
    else:
        mycursor.execute("insert into Lend_dict (bookname,name) values (%s,%s)",(book_namei,nami))

        p.commit()
        lend_obj2 = Toplevel(screen)
        lend_obj2.geometry("400x100")
        lend_obj2.title("Thanks for issuing!")
        # mycursor.execute("select name from Lend_dict where bookname=%s", i)
        l4 = Label(lend_obj2, text=f"The book name {book_namei} is successfully issued to {nami}!!", fg="Green", font=("Arial", 9))
        l4.place(relx=.1, rely=.10)
    #
def lenddict():

    lend_obj = Toplevel(screen)
    lend_obj.geometry("500x300")
    lend_obj.title("Book Issue Portal")
    global book_name
    book_name = StringVar()
    e1=Entry(lend_obj, textvariable=book_name,bg="grey")
    e1.place(relx=0.4, rely=0.2, relwidth=0.3, relheight=0.1)
    global nam
    nam = StringVar()
    e2=Entry(lend_obj, textvariable=nam,bg="grey")
    e2.place(relx=0.4, rely=0.4, relwidth=0.3, relheight=0.1)
    l2 = Label(lend_obj, text="Enter the book to be issued", font=("Arial", 9))
    l2.place(relx=0.4, rely=0.1, relwidth=0.3, relheight=0.1)

    l3 = Label(lend_obj, text="Enter your name", font=("Arial", 9))
    l3.place(relx=0.4, rely=0.3, relwidth=0.3, relheight=0.1)

    btn1 = Button(lend_obj, text="Submit", bg='black', fg='white', command=lend_book)
    btn1.place(relx=0.4, rely=0.55, relwidth=0.3, relheight=0.1)
    l2.destroy()
    l3.destroy()
    # if book_name in mycursor.execute("select book from Book"): #if (bookname == lend_dict.keys()) kyu use nhi kr skte?
    #     print(f"This book is already issued to {name}")
    # else:
    #     lend_dict.update({book_name:name})


def return_book():
    # mycursor.execute("select * from Lend_dict")
    # for i in mycursor:
    #     if (i == book_name):
    book_namei = book_name.get()
    nami = nam.get()
    mycursor.execute("delete from Lend_dict where bookname= %s  ", (book_namei,))
    p.commit()
    ret_obj2 = Toplevel(screen)
    ret_obj2.geometry("400x100")
    ret_obj2.title("Thanks for returning!")
    # mycursor.execute("select name from Lend_dict where bookname=%s", i)
    l4 = Label(ret_obj2, text=f"The book name {book_namei} is successfully returned by {nami}!!", fg="Green", font=("Arial", 9))
    l4.place(relx=.1, rely=.10)
            # break
            # print(f"The book is already issued to {j}")
    # else:
    #     # mycursor.execute("insert into Lend_dict (bookname,name) values (%s,%s)", (book_name, nam))
    #     print ("Book is not yet issued")
def returnbook():
    ret_obj = Toplevel(screen)
    ret_obj.geometry("500x300")
    ret_obj.title("Do Visit Again")
    global book_name
    book_name = StringVar()
    e1 = Entry(ret_obj, textvariable=book_name, bg="grey")
    e1.place(relx=0.4, rely=0.2, relwidth=0.3, relheight=0.1)
    global nam
    nam = StringVar()
    e2 = Entry(ret_obj, textvariable=nam, bg="grey")
    e2.place(relx=0.4, rely=0.4, relwidth=0.3, relheight=0.1)
    l2 = Label(ret_obj, text="Enter the book you want to return", font=("Arial", 9))
    l2.place(relx=0.38, rely=0.1, relwidth=0.37, relheight=0.1)

    l3 = Label(ret_obj, text="Enter your name", font=("Arial", 9))
    l3.place(relx=0.4, rely=0.3, relwidth=0.3, relheight=0.1)

    btn1 = Button(ret_obj, text="Submit", bg='black', fg='white', command=return_book)
    btn1.place(relx=0.4, rely=0.55, relwidth=0.3, relheight=0.1)
    # l2.destroy()
    # l3.destroy()
def add_book():
    book_namei = book_name.get()
    nami = nam.get()
    mycursor.execute("insert into Book (Book_Name, Author_Name) values (%s,%s) ",(book_namei,nami))
    p.commit()
    add_obj2 = Toplevel(screen)
    add_obj2.geometry("400x100")
    add_obj2.title("Thanks for Adding!")
    l4 = Label(add_obj2, text=f"The book name {book_namei} by author {nami} is added succcesfully!!", fg="Green", font=("Arial", 9))
    l4.place(relx=.1, rely=.10)
def addbook():
    add_obj = Toplevel(screen)
    add_obj.geometry("500x300")
    add_obj.title("Book Adding Portal")
    global book_name
    book_name = StringVar()
    e1 = Entry(add_obj, textvariable=book_name, bg="grey")
    e1.place(relx=0.4, rely=0.2, relwidth=0.3, relheight=0.1)
    global nam
    nam = StringVar()
    e2 = Entry(add_obj, textvariable=nam, bg="grey")
    e2.place(relx=0.4, rely=0.4, relwidth=0.3, relheight=0.1)
    l2 = Label(add_obj, text="Enter the book you want to add", font=("Arial", 9))
    l2.place(relx=0.4, rely=0.1, relwidth=0.35, relheight=0.1)

    l3 = Label(add_obj, text="Enter the Author's Name", font=("Arial", 9))
    l3.place(relx=0.4, rely=0.3, relwidth=0.3, relheight=0.1)

    btn1 = Button(add_obj, text="Submit", bg='black', fg='white', command=add_book)
    btn1.place(relx=0.4, rely=0.55, relwidth=0.3, relheight=0.1)
    # l2.destroy()
    # l3.destroy()
    # add_obj.destroy()
    # book.append(book_name)
# while True:
#     print("Enter the number between 1 to 4")
#     print("1) Display the books in library")
#     print("2) Lend a Book")
#     print("3) Return a Book")
#     print("4) Add a Book")
#     a = int(input())
#     if (a == 1 or a=='1'):
#         displaybook()
#     elif (a == 2 or a=='2'):
#         print("Enter the bookname")
#         book_name = input()
#         print("Enter your name")
#         name = input()
#         lend_book(book_name,name)
#     elif (a == 3 or a =='3'):
#         print("Enter the bookname you want to return")
#         book_name = input()
#
#         print("Enter the bookholder's name")
#         name=input()
#         return_book(book_name,name)
#     elif (a == 4 or a=='4'):
#         print("Enter the bookname you want to add")
#         book_name = input()
#         print("Enter its author")
#         author=input()
#         add_book(book_name,author)
#
#
#
#
#     else:
#         print("You have entered a wrong value")


    # print("Press c to continue and e to exit")
    # x=input()
    # while ((x!='c') or (x!='e')):
    #
    #     if (x=="c"):
    #         continue
    #     elif (x=="e"):
    #         exit()
    # else:
    #         print("You've Entered wrong input")
    #         print("Press c to continue and e to exit")
    #         x=input()

    # print("Press q to quit and c to continue")
    # user_choice = ""
    # while user_choice != "c" and user_choice != "q":
    #         user_choice = input()
    #         if user_choice == "q":
    #             exit()
    #
    #         elif user_choice == "c":
    #             continue
    #         else :
    #             print("You've Entered wrong input")
    #             print("Press c to continue and q to exit")


screen =Tk()
screen.geometry("1080x600")
screen.title("Library Management System")



image2 =Image.open('librarybackground.jpg')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
# screen.geometry('%dx%d+0+0' % (w,h))

canvas=Canvas(screen,width=w,height=h)
image=ImageTk.PhotoImage(Image.open("librarybackground.jpg"))



canvas.create_image(0,0,anchor=NW,image=image)


canvas.pack()

l=Label(screen, text="LIBRARY MANAGEMENT SYSTEM",justify=CENTER , font=("Arial", 20,"bold"))
l.place(relx=0.28, rely=0.15,relwidth=0.45, relheight=0.1)

l1=Label(screen, text="An original idea. That can’t be too hard. The library must be full of them.",fg="grey",justify=CENTER , font=("Arial", 8,"italic"))
l1.place(relx=0.34, rely=0.23)


btn1 = Button(screen, text="Display all Available Books!!", bg='white', fg='black', command=displaybook)
btn1.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.05)

btn2 = Button(screen, text="Want to Lend a Book?", bg='white', fg='black', command=lenddict)
btn2.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.05)

btn3 = Button(screen, text="Want to Return a Book?", bg='white', fg='black', command=returnbook)
btn3.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.05)

btn4 = Button(screen, text="Want to Add a Book?", bg='white', fg='black', command=addbook)
btn4.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.05)


screen.mainloop()





