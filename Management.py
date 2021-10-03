from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3


# function to define database
def database():
    global conn, cursor
    # creating student database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    # creating STUD_REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID text, STU_NAME text, STU_EMAIL text,STU_DOB text,STU_GENDER text, STU_CONTACT int, STU_ADDRESS text)")


def displayform():
    root = Tk()
    root.title("Employee Registration System")
    root.geometry("1350x700+90+0")
    root.iconbitmap('students.ico')

    title_name = Label(root, text="Employee Registration System", bd=10, relief=GROOVE,
                       font=("Helvetica", 20, "bold"), bg="coral", fg="black")
    title_name.pack(side=TOP, fill=X)

    global tree
    global SEARCH
    global id_no, name, email, dob, gender, contact, address

    # All entry variables
    SEARCH = StringVar()
    id_no = StringVar()
    name = StringVar()
    email = StringVar()
    dob = StringVar()
    gender = StringVar()
    contact = StringVar()
    address = StringVar()

    # First frame for user to enter data
    upload1 = Frame(root, bd=4, relief=RIDGE, bg="light salmon")
    upload1.place(x=20, y=100, height=580, width=450)

    frame1_title = Label(upload1, text="Employee Data Upload", font=("Helvetica", 18, "bold"), fg="black",
                         bg="light salmon")
    frame1_title.grid(row=0, columnspan=2, pady=20)

    id_label = Label(upload1, text=" I.D.", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    id_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

    id_entry = Entry(upload1, textvariable=id_no, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
    id_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    name_label = Label(upload1, text=" Name", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    name_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

    name_entry = Entry(upload1, textvariable=name, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
    name_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    email_label = Label(upload1, text="Email", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    email_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    email_entry = Entry(upload1, textvariable=email, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
    email_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

    dob_label = Label(upload1, text="D.O.B", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    dob_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

    dob_entry = Entry(upload1, textvariable=dob, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
    dob_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

    gender_label = Label(upload1, text="Gender", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    gender_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

    gender_drop = ttk.Combobox(upload1, textvariable=gender, font=("Helvetica", 11, "bold"), state="readonly")
    gender_drop['values'] = ("male", "female", "other", "prefer not to say")
    gender_drop.grid(row=5, column=1, padx=20, pady=10)

    contact_label = Label(upload1, text="Contact No.", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    contact_label.grid(row=6, column=0, padx=20, pady=10, sticky="w")

    contact_entry = Entry(upload1, textvariable=contact, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
    contact_entry.grid(row=6, column=1, padx=20, pady=10, sticky="w")

    address_label = Label(upload1, text="Address", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    address_label.grid(row=7, column=0, padx=20, pady=10, sticky="w")

    address_txt = Entry(upload1, textvariable=address, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
    address_txt.grid(row=7, column=1, padx=20, pady=10, sticky="w")
    # Button Frame
    button_frame = Frame(upload1, bd=4, relief=RIDGE, bg="light salmon")
    button_frame.place(x=15, y=500, width=410)

    add_btn = Button(button_frame, text="Add", width=10, pady=5, command=register)
    add_btn.grid(row=0, column=0, padx=10, pady=10)
    update_btn = Button(button_frame, text="Update", width=10, pady=5, command=Update)
    update_btn.grid(row=0, column=1, padx=10, pady=10)
    delete_btn = Button(button_frame, text="Delete", width=10, pady=5, command=Delete)
    delete_btn.grid(row=0, column=2, padx=10, pady=10)
    clear_btn = Button(button_frame, text="Clear", width=10, pady=5, command=Reset)
    clear_btn.grid(row=0, column=3, padx=10, pady=10)
    # Second frame for user details
    details2 = Frame(root, bd=4, relief=RIDGE, bg="light salmon")
    details2.place(x=500, y=100, height=580, width=830)

    search_label = Label(details2, text="Search By", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
    search_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    def Search():
        if search_drop.get() == 'ID':
            search_ids()
        if search_drop.get() == 'Name':
            search_name()
        if search_drop.get() == 'Contact':
            search_contact()

    def search_contact():
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        # creating STUD_REGISTRATION table
        cursor.execute('''SELECT * FROM STUD_REGISTRATION''')
        all = cursor.fetchall()
        data2 = []
        for id in all:
            if search_entry.get() == str(id[5]):
                # clear current data
                tree.delete(*tree.get_children())
                for data in id:
                    data2.append(data)

        tree.insert('', 'end', values=tuple(data2))
        tree.bind("<Double-1>", OnDoubleClick)
        cursor.close()
        conn.close()

    def search_name():
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        # creating STUD_REGISTRATION table
        cursor.execute('''SELECT * FROM STUD_REGISTRATION''')
        all = cursor.fetchall()
        data2 = []
        for id in all:
            if search_entry.get() == id[1]:
                # clear current data
                tree.delete(*tree.get_children())
                for data in id:
                    data2.append(data)

        tree.insert('', 'end', values=tuple(data2))
        tree.bind("<Double-1>", OnDoubleClick)
        cursor.close()
        conn.close()

    def search_ids():
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        # creating STUD_REGISTRATION table
        cursor.execute('''SELECT * FROM STUD_REGISTRATION''')
        all = cursor.fetchall()
        data2 = []
        for id in all:
            if search_entry.get() == id[0]:
                # clear current data
                tree.delete(*tree.get_children())
                for data in id:
                    data2.append(data)

        tree.insert('', 'end', values=tuple(data2))
        tree.bind("<Double-1>", OnDoubleClick)
        cursor.close()
        conn.close()

    search_drop = ttk.Combobox(details2, font=("Helvetica", 11, "bold"), state="readonly")
    search_drop['values'] = ("ID", "Name", "Contact")
    search_drop.grid(row=0, column=1, padx=20, pady=10)
    search_drop.current(0)

    search_entry = Entry(details2, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
    search_entry.grid(row=0, column=2, padx=20, pady=10, sticky="w")

    search_btn = Button(details2, text="Search", width=10, pady=5, command=Search)
    search_btn.grid(row=0, column=4, padx=10, pady=10)
    show_all_btn = Button(details2, text="Show All", width=10, pady=5, command=DisplayData)
    show_all_btn.grid(row=0, column=5, padx=10, pady=10)

    # Table Frame
    table_frame = Frame(details2, bd=4, relief=RIDGE, bg="light salmon")
    table_frame.place(x=10, y=70, height=490, width=800)

    scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(table_frame, orient=VERTICAL)
    tree = ttk.Treeview(table_frame,
                        columns=("i.d.", "name", "email", "d.o.b", "gender", "contact", "address"),
                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=tree.xview)
    scroll_y.config(command=tree.yview)

    tree.heading("i.d.", text="ID")
    tree.heading("name", text="Name")
    tree.heading("email", text="Email")
    tree.heading("d.o.b", text="D.O.B")
    tree.heading("gender", text="Gender")
    tree.heading("contact", text="Contact No")
    tree.heading("address", text="Address")
    tree["show"] = "headings"

    tree.pack(fill=BOTH, expand=1)
    DisplayData()


# function to update data into database
def Update():
    database()
    # getting form data
    name1 = name.get()
    con1 = contact.get()
    email1 = email.get()
    id1 = id_no.get()
    dob1 = dob.get()
    gender1 = gender.get()
    address1 = address.get()
    # applying empty validation
    if name1 == '' or con1 == '' or email1 == '' or id1 == '' or dob1 == '' or gender1 == "" or address1 == "":
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:
        # getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        # update query
        conn.execute(
            f'UPDATE STUD_REGISTRATION SET STU_ID=?,STU_NAME=?,STU_EMAIL=?,STU_DOB =?,STU_GENDER = ?, STU_CONTACT=?, STU_ADDRESS=? WHERE STU_ID = ?',
            (id1, name1, email1, dob1, gender1, con1, address1, selecteditem[0]))

        conn.commit()
        tkMessageBox.showinfo("Message", "Updated successfully")
        # reset form
        Reset()
        # refresh table data
        DisplayData()
        conn.close()


def register():
    database()
    # getting form data
    name1 = name.get()
    con1 = contact.get()
    email1 = email.get()
    id1 = id_no.get()
    dob1 = dob.get()
    gender1 = gender.get()
    address1 = address.get()
    # applying empty validation
    if name1 == '' or con1 == '' or email1 == '' or id1 == '' or dob1 == '' or gender1 == "" or address1 == "":
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:

        conn.execute(f'''INSERT INTO STUD_REGISTRATION VALUES (:a,:b,:c,:d,:e,:f,:g)''',
                     {"a": id1, "b": name1, "c": email1, "d": dob1, "e": gender1, "f": con1, "g": address1})

        conn.commit()
        tkMessageBox.showinfo("Message", "Stored successfully")
        # refresh table data
        DisplayData()
        conn.close()


def Reset():
    # clear current data from table
    tree.delete(*tree.get_children())
    # refresh table data
    DisplayData()
    # clear search text
    SEARCH.set("")
    name.set("")
    contact.set("")
    email.set("")
    id_no.set("")
    dob.set("")
    gender.set("")
    address.set("")


def Delete():
    # open database
    database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

    # function to search data


'''def SearchRecord():
    # open database
    database()
    # checking search text is empty or not
    if SEARCH.get() != "":
        # clearing current display data
        tree.delete(*tree.get_children())
        # select query with where clause
        cursor = conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_NAME LIKE ?",
                              ('%' + str(SEARCH.get()) + '%',))
        # fetch all matching records
        fetch = cursor.fetchall()
        # loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()'''


# defining function to access data from SQLite database


def DisplayData():
    # open database
    database()
    # clear current data
    tree.delete(*tree.get_children())
    # select query
    cursor = conn.execute("SELECT * FROM STUD_REGISTRATION")
    # fetch all data from database
    fetch = cursor.fetchall()
    # loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>", OnDoubleClick)
    cursor.close()
    conn.close()


def OnDoubleClick(self):
    # getting focused item from treeview
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    # set values in the fields
    id_no.set(selecteditem[0])
    name.set(selecteditem[1])
    email.set(selecteditem[2])
    dob.set(selecteditem[3])
    gender.set(selecteditem[4])
    contact.set(selecteditem[5])
    address.set(selecteditem[6])


# calling function
displayform()
if __name__ == '__main__':
    # Running Application
    mainloop()