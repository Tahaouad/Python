from tkinter import * 
from sqlite3 import * 
from tkinter import messagebox
from tkinter import ttk
class contact :
    def debut (self,main):
        self.main = main 
        self.main.title("contact book")
        self.main.geometry("1200*750+10+10")
        title=Label(self.main,text="contact book",bd=10,relief=GROOVE,font=("times no roman",30,"bold","white"))
        title.pack(side=TOP,fill=X)

        self.name_var=StringVar()
        self.number_var=StringVar()
        Manage_Frame=Frame(self.main,bd=4,relief=RIDGE,bg="mint cream")
        Manage_Frame.place(x=10,y=100,width=500,height=600)
        m_title=Label(Manage_Frame,text="Manage contacts",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=15)
        lbl_name=Label(Manage_Frame,text="Name *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=1,column=0,pady=5,padx=30,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=5,padx=30,sticky="w")
        lbl_number=Label(Manage_Frame,text="Mobile No *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_number.grid(row=4,column=0,pady=5,padx=30,sticky="w")
        txt_number=Entry(Manage_Frame,textvariable=self.number_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_number.grid(row=4,column=1,pady=5,padx=30,sticky="w")
        Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="mint cream")
        Btn_Frame.place(x=10,y=530,width=450)
        addbtn=Button(Btn_Frame,text="Add",font=("times new roman",12,"bold"),width=10,bg="green",fg="white",command=self.add_contacts).grid(row=0,column=0,padx=5,pady=5)
        updatebtn=Button(Btn_Frame,text="Update",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=self.update_data).grid(row=0,column=1,padx=5,pady=5)
        deletebtn=Button(Btn_Frame,text="Delete",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=self.delete_data).grid(row=0,column=2,padx=5,pady=5)
        clearbtn=Button(Btn_Frame,text="Clear",font=("times new roman",12,"bold"))
        Details_Frame=Frame(self.main,bd=4,relief=RIDGE,bg="mint cream")
        Details_Frame.place(x=525,y=100,width=850,height=600)
        lbl_search=Label(Details_Frame,text="Search",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=30,sticky="w")
        combo_search=ttk.Combobox(Details_Frame,width=10,textvariable=self.search_by,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Name","number")
        combo_search.grid(row=0,column=1,padx=30,pady=10,sticky="w")
        txt_search=Entry(Details_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=30,sticky="w")
        searchbtn=Button(Details_Frame,text="Search",bg="green",fg="white",font=("times new roman",12,"bold"),command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Details_Frame,text="Showall",bg="green",fg="white",font=("times new roman",12,"bold"),command=self.fetch_data,width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="mint cream")
        Table_Frame.place(x=10,y=70,width=800,height=500)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.contacts_table=ttk.Treeview(Table_Frame,columns=("Name","number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.contacts_table.xview)
        scroll_y.config(command=self.contacts_table.yview)

        self.contacts_table.heading("Name",text="Name")
        self.contacts_table.heading("number",text="number")
        self.contacts_table.column("Name",width=150)
        self.contacts_table.column("number",width=150)
        self.contacts_table.pack(fill=BOTH,expand=1)
        self.contacts_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        


main=Tk()
con=connect('contacts.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS contacts(Name text NOT NULL, Email text NOT NULL,Gender text NOT NULL,MobileNo integer(10) NOT NULL,teleNo integer(10) ,DateOfBirth text, Address text NOT NULL); ")
con.commit()
con.close()
ob = contact()
main.mainloop()  



