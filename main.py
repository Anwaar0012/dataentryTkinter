import tkinter
from tkinter import ttk,messagebox
import openpyxl
import os
import sqlite3

def enter_data():
    # print("hi")
    accepted=accept_var.get()
    if accepted=="Accepted":
        firstname=first_name_entry.get()
        last_name=last_name_entry.get()
        if firstname and last_name:
            post=post_name_combobox.get()
            age=age_spinbox.get()
            nationality=nationality_combobox.get()
            registeration_status=registeration_variable.get()
            course=numcouses_spinbox.get()
            semester=numsemesters_spinbox.get()
            terms=accept_var.get()
            # print(f"First Name : {firstname}\n Last Name:{last_name}\n,Designation{post}\n,Age{age}\n, Nationality:{nationality}\n,Course{course}\n,Semster{semester}\n,Terms{terms}\n,Registeration:{registeration_status}")
            messagebox.showinfo("Success",f"The data of {firstname} {last_name} is saved successfully")
            
            #  creating sqlite talble
            conn = sqlite3.connect("data.db")
            table_create_query='''CREATE TABLE IF NOT EXISTS student_data
            (firstname TEXT, last_name TEXT,post TEXT,age INT,nationality TEXT,registeration_status TEXT,course INT,semester INT)           
            '''
            conn.execute(table_create_query)
            data_insert_query='''INSERT INTO student_data(firstname, last_name,post,age,nationality,registeration_status,course,semester) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            date_insert_tuple=(firstname, last_name,post,age,nationality,registeration_status,course,semester)
            cursor=conn.cursor()
            cursor.execute(data_insert_query,date_insert_tuple)
            conn.commit()
            conn.close()
            
            
            # saving data into excell file 
            # filepath="F:\\tkinter python gui\dataentry\dataEntry\data.xlsx"
            # if not os.path.exists(filepath):
            #     workbook =openpyxl.Workbook()
            #     sheet = workbook.active
            #     heading=["First Name","Last Name","Designation","Age","Nationality","#Course","# Semester","Regosteratopm Statis"]
            #     sheet.append(heading)
            #     workbook.save(filepath)
            # workbook=openpyxl.load_workbook(filepath)
            # sheet = workbook.active
            # sheet.append([firstname,last_name,post,age,nationality,course,semester,registeration_status])
            # workbook.save(filepath) 
        else:
            messagebox.showwarning("Name Error","Please enter your name.")
    else:
        print("First Accept out terms and conditions")
        messagebox.showerror("Error","First Accept the terms and conditions")

window=tkinter.Tk()
window.title("Data Entry Form")
frame= tkinter.Frame(window,bg="green")
frame.pack()


#  saving user iformation
user_info_frame=tkinter.LabelFrame(frame,text="User Information",bg="yellow")
user_info_frame.grid(row=0,column=0,padx=20,pady=15)

first_name_label=tkinter.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)

Last_name_label=tkinter.Label(user_info_frame,text="Last Name")
Last_name_label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry=tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1,column=1)

post_name_label=tkinter.Label(user_info_frame,text="post_name")
post_name_label.grid(row=0,column=2)
post_name_combobox=ttk.Combobox(user_info_frame,values=["SST","EST","PST","SGD","MALI"])
post_name_combobox.grid(row=1,column=2)

age_label=tkinter.Label(user_info_frame,text="Age")
age_label.grid(row=2,column=0)
age_spinbox=tkinter.Spinbox(user_info_frame,from_=18,to=100)
age_spinbox.grid(row=3,column=0)

nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_label.grid(row=2,column=1)
nationality_combobox=ttk.Combobox(user_info_frame,values=["Pakistan","America","China"])
nationality_combobox.grid(row=3,column=1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)
    
#  saving course iformation
course_frame=tkinter.LabelFrame(frame,bg="yellow")
course_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

registeration_label=tkinter.Label(course_frame,text="Registeration status")
registeration_label.grid(row=0,column=0)
registeration_variable=tkinter.StringVar(value="Not Registered")
registeration_checkbox=tkinter.Checkbutton(course_frame,text="Currently Registered",variable=registeration_variable
                                           ,onvalue="Registered",offvalue="Not Registered")
registeration_checkbox.grid(row=1,column=0)

numcouses_label=tkinter.Label(course_frame,text="# Completed courses")
numcouses_spinbox =tkinter.Spinbox(course_frame,from_=0,to="infinity")
numcouses_label.grid(row=0,column=1)
numcouses_spinbox.grid(row=1,column=1)

numsemester_label=tkinter.Label(course_frame,text="# Semesters")
numsemesters_spinbox =tkinter.Spinbox(course_frame,from_=0,to="infinity")
numsemester_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)
    
# Accept Terms
terms_frame=tkinter.LabelFrame(frame, text="Terms & Conditions",bg="yellow",padx=20,pady=20)
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=20)

accept_var = tkinter.StringVar(value="Not accepted")
terms_check=tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions"
                                ,variable=accept_var,onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

#Button
button = tkinter.Button(frame,text="Enter Data",bg="red",fg="white",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)



window.mainloop()