from tkinter import*
from tkinter import ttk


class System:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration System")
        self.root.geometry("1350x700+90+0")
        self.root.iconbitmap('students.ico')

        title_name = Label(self.root, text="Student Registration System", bd=10, relief=GROOVE, font=("Helvetica", 20, "bold"), bg="coral", fg="black")
        title_name.pack(side=TOP, fill=X)

        # First frame for user to enter data
        upload1 = Frame(self.root, bd=4, relief=RIDGE, bg="light salmon")
        upload1.place(x=20, y=100, height=580, width=450)

        frame1_title = Label(upload1, text="Student Data Upload", font=("Helvetica", 18, "bold"), fg="black", bg="light salmon")
        frame1_title.grid(row=0, columnspan=2, pady=20)

        id_label = Label(upload1, text="Student I.D.", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        id_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        id_entry = Entry(upload1, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
        id_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        name_label = Label(upload1, text="Student Name", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        name_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        name_entry = Entry(upload1, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
        name_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        email_label = Label(upload1, text="Email", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        email_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        email_entry = Entry(upload1, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
        email_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        dob_label = Label(upload1, text="D.O.B", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        dob_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        dob_entry = Entry(upload1, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
        dob_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        gender_label = Label(upload1, text="Gender", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        gender_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        gender_drop = ttk.Combobox(upload1, font=("Helvetica", 11, "bold"), state="readonly")
        gender_drop['values'] = ("male", "female", "other", "prefer not to say")
        gender_drop.grid(row=5, column=1, padx=20, pady=10)

        contact_label = Label(upload1, text="Contact No.", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        contact_label.grid(row=6, column=0, padx=20, pady=10, sticky="w")

        contact_entry = Entry(upload1, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
        contact_entry.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        address_label = Label(upload1, text="Address", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        address_label.grid(row=7, column=0, padx=20, pady=10, sticky="w")

        address_txt = Text(upload1, width=27, height=4, font=("", 10))
        address_txt.grid(row=7, column=1, padx=20, pady=10, sticky="w")
        # Button Frame
        button_frame = Frame(upload1, bd=4, relief=RIDGE, bg="light salmon")
        button_frame.place(x=15, y=500, width=410)

        add_btn = Button(button_frame, text="Add", width=10)
        add_btn.grid(row=0, column=0, padx=10, pady=10)
        update_btn = Button(button_frame, text="Update", width=10)
        update_btn.grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(button_frame, text="Delete", width=10)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(button_frame, text="Clear", width=10)
        clear_btn.grid(row=0, column=3, padx=10, pady=10)
        # Second frame for user details
        details2 = Frame(self.root, bd=4, relief=RIDGE, bg="light salmon")
        details2.place(x=500, y=100, height=580, width=830)

        search_label = Label(details2, text="Search By", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        search_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        search_drop = ttk.Combobox(details2, font=("Helvetica", 11, "bold"), state="readonly")
        search_drop['values'] = ("I.D.", "Name", "Contact")
        search_drop.grid(row=0, column=1, padx=20, pady=10)

        search_entry = Entry(details2, font=("Helvetica", 13, "bold"), bd=5, relief=SUNKEN)
        search_entry.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        search_btn = Button(details2, text="Search", width=10, pady=5)
        search_btn.grid(row=0, column=4, padx=10, pady=10)
        show_all_btn = Button(details2, text="Show All", width=10, pady=5)
        show_all_btn.grid(row=0, column=5, padx=10, pady=10)


root = Tk()
obj = System(root)
root.mainloop()