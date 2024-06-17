import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

tesDB = mysql.connector.connect(host="localhost",
                                port="3306",
                                user="root",
                                password="",
                                database="tes")

cursor = tesDB.cursor()


def GetValue(event):
    selected_row = listBox.selection()[0]
    selected = listBox.set(selected_row)
    id_var.set(selected['id'])
    name_var.set(selected['name'])
    address_var.set(selected['address'])
    email_var.set(selected['email'])
    telp_num_var.set(selected['telp_num'])


def add():
    name = name_var.get()
    address = address_var.get()
    email = email_var.get()
    telp_num = telp_num_var.get()
    try:
        sql = "INSERT INTO contacts (name, address, email, telp_num) VALUES (%s, %s, %s, %s)"
        val = (name, address, email, telp_num)
        cursor.execute(sql, val)
        tesDB.commit()
        messagebox.showinfo("Information", "Contact added successfully")
        clear_entries()
        show()
    except Exception as e:
        print(e)
        tesDB.rollback()


def update():
    id = id_var.get()
    name = name_var.get()
    address = address_var.get()
    email = email_var.get()
    telp_num = telp_num_var.get()
    try:
        sql = "UPDATE contacts SET name = %s, address = %s, email = %s, telp_num = %s WHERE id = %s"
        val = (name, address, email, telp_num, id)
        cursor.execute(sql, val)
        tesDB.commit()
        messagebox.showinfo("Information", "Contact updated successfully")
        clear_entries()
        show()
    except Exception as e:
        print(e)
        tesDB.rollback()


def delete():
    id = id_var.get()
    try:
        sql = "DELETE FROM contacts WHERE id = %s"
        val = (id, )
        cursor.execute(sql, val)
        tesDB.commit()
        messagebox.showinfo("Information", "Contact deleted successfully")
        clear_entries()
        show()
    except Exception as e:
        print(e)
        tesDB.rollback()


def show():
    cursor.execute("SELECT id, name, address, email, telp_num FROM contacts")
    records = cursor.fetchall()
    listBox.delete(*listBox.get_children())
    for i, (id, name, address, email, telp_num) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, name, address, email, telp_num))


def clear_entries():
    id_var.set("")
    name_var.set("")
    address_var.set("")
    email_var.set("")
    telp_num_var.set("")


root = tk.Tk()
root.geometry("1000x500")
root.title('Phone Book')
tk.Label(root, text="ID").place(x=10, y=10)
tk.Label(root, text="Name").place(x=10, y=40)
tk.Label(root, text="Address").place(x=10, y=70)
tk.Label(root, text="Email").place(x=10, y=100)
tk.Label(root, text="Phone Number").place(x=10, y=130)

id_var = tk.StringVar()
name_var = tk.StringVar()
address_var = tk.StringVar()
email_var = tk.StringVar()
telp_num_var = tk.StringVar()

id = tk.Entry(root, textvariable=id_var, state='disabled')
id.place(x=140, y=10)

name = tk.Entry(root, textvariable=name_var)
name.place(x=140, y=40)

address = tk.Entry(root, textvariable=address_var)
address.place(x=140, y=70)

email = tk.Entry(root, textvariable=email_var)
email.place(x=140, y=100)

telp_num = tk.Entry(root, textvariable=telp_num_var)
telp_num.place(x=140, y=130)

tk.Button(root, text="Add", command=add, height=3, width=13).place(x=30, y=170)
tk.Button(root, text="Update", command=update, height=3, width=13).place(x=140,
                                                                         y=170)
tk.Button(root, text="Delete", command=delete, height=3, width=13).place(x=250,
                                                                         y=170)

cols = ('id', 'name', 'address', 'email', 'telp_num')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=220)

show()
listBox.bind('<Double-1>', GetValue)

root.mainloop()
