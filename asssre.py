from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime

image1 = 'library.png'
image2 = 'image2.png'
image3 = 'finance.png'

class menu:
    def __init__(self):
        self.root = Tk()
        self.root.title('Library System - Re-Engineered Edition')
        self.root.state('zoomed')
        
        # Database Setup & Initialization
        conn = sqlite3.connect('test.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS book_info
        (ID VARCHAR PRIMARY KEY NOT NULL,
        TITLE VARTEXT NOT NULL,
        AUTHOR VARTEXT NOT NULL,
        GENRE VARTEXT NOT NULL,
        COPIES VARINT NOT NULL,
        LOCATION VARCHAR NOT NULL);''')
        conn.commit()
        
        conn.execute('''CREATE TABLE IF NOT EXISTS book_issued
        (BOOK_ID VARCHAR NOT NULL,
        STUDENT_ID VARCHAR NOT NULL,
        ISSUE_DATE DATE NOT NULL,
        RETURN_DATE DATE NOT NULL,
        PRIMARY KEY (BOOK_ID,STUDENT_ID));''')
        conn.commit()
        conn.close()

        # Base Canvas Setup with Fallback UI Support
        self.a = self.canvases(image1)
        
        # Centered Navigation Buttons
        Button(self.a, text='BOOK DATA', font=('Helvetica', 16, 'bold'), fg='Yellow', bg='Black', width=18, borderwidth=3, command=self.book).place(relx=0.32, rely=0.70, anchor="center")
        Button(self.a, text='STUDENT DATA', font=('Helvetica', 16, 'bold'), fg='Yellow', bg='Black', width=18, borderwidth=3, command=self.student).place(relx=0.68, rely=0.70, anchor="center")
        
        # Centered Dashboard Real-time Stats Counter Panel
        
        self.render_dashboard_stats()
        
        self.root.mainloop()

    def render_dashboard_stats(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        
        c.execute("SELECT SUM(COPIES) FROM book_info")
        total_copies = c.fetchone()[0] or 0
        
        c.execute("SELECT COUNT(*) FROM book_issued")
        issued_count = c.fetchone()[0] or 0
        conn.close()

        # Perfectly Centered Stats Box
        stats_frame = Frame(self.a, bg='#0f172a', bd=3, relief=RIDGE)
        stats_frame.place(relx=0.5, rely=0.52, anchor="center", width=780, height=55)
        
        lbl = Label(stats_frame, 
                    text=f"📊 LIVE DASHBOARD: Total Book Copies Available: {total_copies}  |  Total Books Issued: {issued_count}", 
                    font=('Helvetica', 12, 'bold'), fg='#38bdf8', bg='#0f172a')
        lbl.pack(expand=True)

    def canvases(self, images):
        self.root.update()
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        
        self.canvas = Canvas(self.root, width=w, height=h, bg='#1e293b')
        self.canvas.grid(row=0, column=0)
        
        try:
            photo = Image.open(images)
            photo1 = photo.resize((w, h), Image.Resampling.LANCZOS)
            photo2 = ImageTk.PhotoImage(photo1)
            self.canvas.create_image(0, 0, anchor=NW, image=photo2)
            self.canvas.image = photo2
        except Exception:
            self.canvas.create_text(w//2, 40, text="LIBRARY MANAGEMENT SYSTEM (RE-ENGINEERED)", font=("Helvetica", 24, "bold"), fill="white")
            
        return self.canvas

    def book(self):
        self.a.destroy()
        self.a = self.canvases(image2)
        Button(self.a, text='Add Books', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.addbook).place(x=30, y=100)
        Button(self.a, text='Search Books', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.search).place(x=30, y=200)
        Button(self.a, text='All Books', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.all).place(x=30, y=300)
        Button(self.a, text='<< Main Menu', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.mainmenu).place(x=30, y=500)

    def addbook(self):
        self.aid = StringVar()
        self.aauthor = StringVar()
        self.aname = StringVar()
        self.acopies = IntVar()
        self.agenre = StringVar()
        self.aloc = StringVar()
        self.f1 = Frame(self.a, height=500, width=650, bg='black')
        self.f1.place(x=350, y=100)
        
        Label(self.f1, text='Book ID : ', font=('Helvetica', 12, 'bold'), fg='Orange', bg='Black').place(x=50, y=50)
        Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aid).place(x=150, y=50)
        
        Label(self.f1, text='Title : ', font=('Helvetica', 12, 'bold'), fg='Orange', bg='Black').place(x=50, y=100)
        Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aname).place(x=150, y=100)
        
        Label(self.f1, text='Author : ', font=('Helvetica', 12, 'bold'), fg='orange', bg='Black').place(x=50, y=150)
        Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aauthor).place(x=150, y=150)
        
        Label(self.f1, text='Genre : ', font=('Helvetica', 12, 'bold'), fg='orange', bg='Black').place(x=50, y=200)
        Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.agenre).place(x=150, y=200)
        
        Label(self.f1, text='Copies : ', font=('Helvetica', 12, 'bold'), fg='orange', bg='Black').place(x=50, y=250)
        Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.acopies).place(x=150, y=250)
        
        Label(self.f1, text='Location : ', font=('Helvetica', 12, 'bold'), fg='orange', bg='Black').place(x=50, y=300)
        Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aloc).place(x=150, y=300)
        
        Button(self.f1, text='Add', font=('Helvetica', 10, 'bold'), fg='black', bg='orange', width=15, bd=3, command=self.adddata).place(x=150, y=400)
        Button(self.f1, text='Back', font=('Helvetica', 10, 'bold'), fg='black', bg='orange', width=15, bd=3, command=self.rm).place(x=350, y=400)

    def rm(self):
        if hasattr(self, 'f1'):
            self.f1.destroy()

    def mainmenu(self):
        self.root.destroy()
        menu()

    def adddata(self):
        a = self.aid.get()
        b = self.aname.get()
        c = self.aauthor.get()
        d = self.agenre.get()
        e = self.acopies.get()
        f = self.aloc.get()
        conn = sqlite3.connect('test.db')
        try:
            if not (a and b and c and d and f):
                messagebox.showinfo("Error", "Fields cannot be empty.")
            else:
                conn.execute("INSERT INTO book_info VALUES (?,?,?,?,?,?)", (a.capitalize(), b.capitalize(), c.capitalize(), d.capitalize(), e, f.capitalize()))
                conn.commit()
                messagebox.showinfo("Success", "Book added successfully")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error", "Book is already present.")
        conn.close()

    def search(self):
        self.sid = StringVar()
        self.f1 = Frame(self.a, height=500, width=650, bg='black')
        self.f1.place(x=350, y=100)
        Label(self.f1, text='Search (ID/Title/Author): ', font=('Helvetica', 10, 'bold'), fg='orange', bg='black').place(x=20, y=40)
        Entry(self.f1, width=25, bd=5, bg='orange', fg='black', textvariable=self.sid).place(x=220, y=40)
        Button(self.f1, text='Search', bg='orange', font=('Helvetica', 10, 'bold'), width=9, bd=2, command=self.serch1).place(x=450, y=37)
        Button(self.f1, text='Back', bg='orange', font=('Helvetica', 10, 'bold'), width=10, bd=2, command=self.rm).place(x=250, y=450)

    def create_tree(self, plc, lists):
        tree = ttk.Treeview(plc, height=13, columns=lists, show='headings')
        for item in lists:
            tree.heading(item, text=item)
            tree.column(item, width=95)
        return tree

    def serch1(self):
        k = self.sid.get()
        if k != "":
            self.list4 = ("BOOK ID", "TITLE", "AUTHOR", "GENRE", "COPIES", "LOCATION")
            self.trees = self.create_tree(self.f1, self.list4)
            self.trees.place(x=25, y=150)
            conn = sqlite3.connect('test.db')
            c = conn.execute("SELECT * FROM book_info WHERE ID=? OR TITLE=? OR AUTHOR=? OR GENRE=?", (k.capitalize(), k.capitalize(), k.capitalize(), k.capitalize()))
            a = c.fetchall()
            if len(a) != 0:
                for row in a:
                    self.trees.insert("", END, values=row)
            else:
                messagebox.showinfo("Error", "Data not found")
            conn.close()
        else:
            messagebox.showinfo("Error", "Search field cannot be empty.")

    def all(self):
        self.f1 = Frame(self.a, height=500, width=650, bg='black')
        self.f1.place(x=350, y=100)
        Button(self.f1, text='Back', bg='orange', fg='black', width=10, bd=3, command=self.rm).place(x=250, y=430)
        conn = sqlite3.connect('test.db')
        self.list3 = ("BOOK ID", "TITLE", "AUTHOR", "GENRE", "COPIES", "LOCATION")
        self.treess = self.create_tree(self.f1, self.list3)
        self.treess.place(x=25, y=50)
        c = conn.execute("SELECT * FROM book_info")
        g = c.fetchall()
        if len(g) != 0:
            for row in g:
                self.treess.insert('', END, values=row)
        conn.close()

    def student(self):
        self.a.destroy()
        self.a = self.canvases(image2)
        Button(self.a, text='Issue book', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.issue).place(x=30, y=100)
        Button(self.a, text='Return Book', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.returnn).place(x=30, y=200)
        Button(self.a, text='Student Activity', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.activity).place(x=30, y=300)
        Button(self.a, text='<< Main Menu', font=('Helvetica', 14, 'bold'), fg='Orange', bg='Black', width=15, command=self.mainmenu).place(x=30, y=500)

    def issue(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()
        self.f1 = Frame(self.a, height=550, width=500, bg='black')
        self.f1.place(x=350, y=100)
        Label(self.f1, text='Book ID : ', font=('Helvetica', 14, 'bold'), bg='black', fg='orange').place(x=50, y=100)
        Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.aidd).place(x=180, y=100)
        Label(self.f1, text='Student Id : ', font=('Helvetica', 14, 'bold'), bg='black', fg='orange').place(x=50, y=150)
        Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.astudentt).place(x=180, y=150)
        Button(self.f1, text='Back', font=('Helvetica', 10, 'bold'), fg='black', bg='orange', width=10, bd=3, command=self.rm).place(x=50, y=250)
        Button(self.f1, text='Issue', font=('Helvetica', 10, 'bold'), fg='black', bg='orange', width=10, bd=3, command=self.issuedbook).place(x=200, y=250)

    def issuedbook(self):
        bookid = self.aidd.get()
        studentid = self.astudentt.get()
        if bookid and studentid:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("SELECT ID, COPIES FROM book_info WHERE ID=?", (bookid.capitalize(),))
            an = cursor.fetchall()
            if an:
                if an[0][1] > 0:
                    try:
                        conn.execute("INSERT INTO book_issued VALUES (?,?,date('now'),date('now','+7 day'))", (bookid.capitalize(), studentid.capitalize()))
                        conn.execute("UPDATE book_info SET COPIES=COPIES-1 WHERE ID=?", (bookid.capitalize(),))
                        conn.commit()
                        messagebox.showinfo("Updated", "Book Issued successfully.")
                    except:
                        messagebox.showinfo("Error", "Book is already issued by student.")
                else:
                    messagebox.showinfo("Unavailable", "Book unavailable. 0 copies remaining.")
            else:
                messagebox.showinfo("Error", "No such Book in Database.")
            conn.close()
        else:
            messagebox.showinfo("Error", "Fields cannot be blank.")

    def returnn(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()
        self.f1 = Frame(self.a, height=550, width=500, bg='black')
        self.f1.place(x=350, y=100)
        Label(self.f1, text='Book ID : ', font=('Helvetica', 14, 'bold'), fg='orange', bg='black').place(x=50, y=100)
        Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.aidd).place(x=180, y=100)
        Label(self.f1, text='Student Id : ', font=('Helvetica', 14, 'bold'), fg='orange', bg='black').place(x=50, y=150)
        Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.astudentt).place(x=180, y=150)
        Button(self.f1, text='Back', font=('Helvetica', 10, 'bold'), bg='orange', fg='black', width=10, bd=3, command=self.rm).place(x=50, y=250)
        Button(self.f1, text='Return', font=('Helvetica', 10, 'bold'), bg='orange', fg='black', width=10, bd=3, command=self.returnbook).place(x=200, y=250)

    def returnbook(self):
        a = self.aidd.get()
        b = self.astudentt.get()
        conn = sqlite3.connect('test.db')
        c = conn.execute("SELECT RETURN_DATE FROM book_issued WHERE BOOK_ID=? AND STUDENT_ID=?", (a.capitalize(), b.capitalize()))
        d = c.fetchone()
        
        if d is not None:
            return_date_str = d[0]
            try:
                ret_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
                today = datetime.now().date()
                fine = 0
                if today > ret_date:
                    overdue_days = (today - ret_date).days
                    fine = overdue_days * 10
            except Exception:
                fine = 0

            conn.execute("DELETE FROM book_issued WHERE BOOK_ID=? AND STUDENT_ID=?", (a.capitalize(), b.capitalize()))
            conn.execute("UPDATE book_info SET COPIES=COPIES+1 WHERE ID=?", (a.capitalize(),))
            conn.commit()
            
            if fine > 0:
                messagebox.showwarning("Book Returned", f"Book returned successfully!\n\n⚠️ OVERDUE FINE: Rs. {fine}\n(Days Overdue: {overdue_days})")
            else:
                messagebox.showinfo("Success", "Book Returned successfully. No fine applied!")
        else:
            messagebox.showinfo("Error", "Data not found.")
        conn.close()

    def activity(self):
        self.aidd = StringVar()
        self.f1 = Frame(self.a, height=550, width=500, bg='black')
        self.f1.place(x=350, y=80)
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = self.create_tree(self.f1, self.list2)
        self.trees.place(x=50, y=150)

        Label(self.f1, text='Book/Student ID : ', font=('Helvetica', 12, 'bold'), fg='Orange', bg='black').place(x=20, y=30)
        Entry(self.f1, width=20, bd=4, bg='orange', textvariable=self.aidd).place(x=200, y=35)
        Button(self.f1, text='Back', bg='orange', font=('Helvetica', 10, 'bold'), width=10, bd=3, command=self.rm).place(x=340, y=450)
        Button(self.f1, text='Search', bg='orange', font=('Helvetica', 10, 'bold'), width=10, bd=3, command=self.searchact).place(x=40, y=450)
        Button(self.f1, text='All', bg='orange', font=('Helvetica', 10, 'bold'), width=10, bd=3, command=self.searchall).place(x=190, y=450)

    def searchact(self):
        conn = sqlite3.connect('test.db')
        bid = self.aidd.get()
        c = conn.execute("SELECT * FROM book_issued WHERE BOOK_ID=? OR STUDENT_ID=?", (bid.capitalize(), bid.capitalize()))
        d = c.fetchall()
        for i in self.trees.get_children():
            self.trees.delete(i)
        if len(d) != 0:
            for row in d:
                self.trees.insert("", END, values=row)
        else:
            messagebox.showinfo("Error", "Data not found.")
        conn.close()

    def searchall(self):
        conn = sqlite3.connect('test.db')
        c = conn.execute("SELECT * FROM book_issued")
        d = c.fetchall()
        for i in self.trees.get_children():
            self.trees.delete(i)
        for row in d:
            self.trees.insert("", END, values=row)
        conn.close()

# Start Application
def canvases(images, w, h):
    canvas = Canvas(root, width=w, height=h, bg='#1e293b')
    canvas.grid(row=0, column=0)
    try:
        photo = Image.open(images)
        photo1 = photo.resize((w, h), Image.Resampling.LANCZOS)
        photo2 = ImageTk.PhotoImage(photo1)
        canvas.create_image(0, 0, anchor=NW, image=photo2)
        canvas.image = photo2
    except Exception:
        canvas.create_text(w//2, 80, text="ADMIN LOGIN", font=("Helvetica", 24, "bold"), fill="orange")
    return canvas

root = Tk()
root.title("LOGIN")
root.state('zoomed')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
canvas = canvases(image3, w, h)

def Database():
    global conn, cursor
    conn = sqlite3.connect("python1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `login` WHERE `username` = 'Usman' AND `password` = 'root'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `login` (username, password) VALUES('Usman', 'root')")
        conn.commit()

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error", "Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `login` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            root.destroy()
            a = menu()
        else:
            messagebox.showinfo("Error", "Invalid username or password.")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()

USERNAME = StringVar()
PASSWORD = StringVar()

lbl_title = Label(canvas, text="ADMIN LOGIN", font=('Helvetica', 28, 'bold'), bg='black', fg='orange')
lbl_title.place(relx=0.5, rely=0.2, anchor="center")

lbl_username = Label(canvas, text="Username:", font=('Helvetica', 14, 'bold'), bd=4, bg='black', fg='orange')
lbl_username.place(relx=0.40, rely=0.38, anchor="e")

lbl_password = Label(canvas, text="Password :", font=('Helvetica', 14, 'bold'), bd=3, bg='black', fg='orange')
lbl_password.place(relx=0.40, rely=0.48, anchor="e")

username = Entry(canvas, textvariable=USERNAME, font=('Helvetica', 14), bg='black', fg='orange', bd=5)
username.place(relx=0.42, rely=0.38, anchor="w", width=220)

password = Entry(canvas, textvariable=PASSWORD, show="*", font=('Helvetica', 14), bg='black', fg='orange', bd=5)
password.place(relx=0.42, rely=0.48, anchor="w", width=220)

btn_login = Button(canvas, text="LOGIN", font=('Helvetica', 14, 'bold'), width=20, command=Login, bg='black', fg='orange')
btn_login.place(relx=0.5, rely=0.60, anchor="center")

root.mainloop()