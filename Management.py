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
        upload1.place(x=20, y=70, height=560, width=450)

        frame1_title = Label(upload1, text="Student Data Upload", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        frame1_title.grid(row=0, columnspan=2, pady=20)

        id_label = Label(upload1, text="Student I.D.", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        id_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        id_entry = Entry(upload1,font=("Helvetica", 10, "bold"), bd=5, relief=SUNKEN)
        id_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        name_label = Label(upload1, text="Student Name", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        name_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        name_entry = Entry(upload1,font=("Helvetica", 10, "bold"), bd=5, relief=SUNKEN)
        name_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        email_label = Label(upload1, text="Email", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        email_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        email_entry = Entry(upload1,font=("Helvetica", 10, "bold"), bd=5, relief=SUNKEN)
        email_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        dob_label = Label(upload1, text="D.O.B", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        dob_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        dob_entry = Entry(upload1,font=("Helvetica", 10, "bold"), bd=5, relief=SUNKEN)
        dob_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        gender_label = Label(upload1, text="Gender", font=("Helvetica", 15, "bold"), fg="black", bg="light salmon")
        gender_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        gender_drop = ttk.Combobox(upload1, font=("Helvetica", 10, "bold"))
        gender_drop['values'] = ("male","female","other","prefer not to say")
        gender_drop.grid(row=5, column=1, padx=20, pady=10)

        # Second frame for user details
        frame2 = Frame(self.root, bd=4, relief=RIDGE, bg="light salmon")
        frame2.place(x=500, y=70, height=560, width=800)


root = Tk()
obj = System(root)
root.mainloop()