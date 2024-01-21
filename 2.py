from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from datetime import datetime
from tkinter import messagebox
import sys

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")
        
        self.title_label = Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)


#========================bg image=================================================
        self.load = Image.open("1.jpg")
        self.bulao = ImageTk.PhotoImage(self.load)
        img = Label(self.win, image=self.bulao)
        img.place(x=0,y=0,relheight=1,relwidth=1)
#-========================main frame================================================
        self.main_frame = Frame(self.win,bg="black",bd=6,relief=GROOVE)
        self.main_frame.place(x=300,y=200,width=800,height=400)
    
        self.login_lbl = Label(self.main_frame,text="login",bd=6,relief=GROOVE,anchor=CENTER,bg="white",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",fg="white",bd=6,relief=GROOVE,bg="black",font=('sans-serif,18'))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        self.entus_lbl = Label(self.entry_frame,text="Enter Username: ",bg="black",fg="white",font=('sans=serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        #========================variables============================

        username = StringVar()
        password = StringVar()

        #==============================================================

        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,bg="red",fg="black",textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        self.entpass_lbl = Label(self.entry_frame,text="Enter Password: ",fg="white",bg="black",font=('sans=serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.entpass_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,bg="red",fg="black",textvariable=password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)

        #=======================Functions==================

        def check_login():

            if username.get() == "BHOKAT" and password.get() == "1234":
                self.billing_btn.config(state="normal")
            else:
                pass   #----> message box


        def reset():
            username.set("")
            password.set("")
        
        def billing_sec():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)

        #===================Functions===========================
        
        def add_pur():
            pass

        #=======================BUTTONS====================
        self.button_frame = LabelFrame(self.entry_frame,text="Options",font=('Arial',15),bg="red",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn = Button(self.button_frame,text="Login",font=('Arial',14),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn = Button(self.button_frame,text="Billing",font=('Arial',14),bd=5,width=15,command=billing_sec)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',14),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)

        #===========================================================

class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")

        #self.win.resizable(0,0)
        #=====================image===========================
        self.load = Image.open("salad-2068220_1920.jpg")
        self.bulao = ImageTk.PhotoImage(self.load)
        img = Label(self.win, image=self.bulao)
        img.place(x=0,y=0,relheight=1,relwidth=1)

        self.title_label = Label(self.win,text="Amrutshala",font=('Arial',35,'bold'),bg="orange",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
    #======================================= ENTRY =================================
        self.entry_frame = LabelFrame(self.win,text="Enter Details",bg="yellow",font=('Arial,20'),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=520,height=650)


        #===============================functions================================
        total_list = []
        self.grd_total = 0 
     #======================variables ==============================================      
        bill_no = random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()
        date_pr.set(datetime.now())

        total_list = []
        self.grd_total = 0
        #=========================default==========================
        def default_bill(): 
            self.bill_txt.insert(END,"\t\t\t            AMRUTSHALA")
            self.bill_txt.insert(END,"\n\t\t\t a-1,tara city,ramdhara road,loni kalbor")
            self.bill_txt.insert(END,"\n\t\t\t      Contact = +9370692726")
            self.bill_txt.insert(END,"\n==========================================================================")
            self.bill_txt.insert(END,f"\nBill Number = {bill_no_tk.get()}")


        def genbill():
            self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
            self.bill_txt.insert(END,f"\nCustomer Contact : {cust_cot.get()}")
            self.bill_txt.insert(END,f"\nDate :{date_pr.get()}")
            self.bill_txt.insert(END,"\n===================================================================================================================================")
            self.bill_txt.insert(END,f"\nProduct Name\t\t     Quantity\t\t\t  Per Cost\t\t      Total")
            self.bill_txt.insert(END,"\n===================================================================================================================================")

            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")
        

        
        # def total_func():
            #globall grd_total
           # for item in total_list:
               # self.grd_total = self.grd_total + item
           # self.bill_txt.insert(END,"\n =================================================================================")
            #self.bill_txt.insert(END,f"\t\t\t\t\tGrand Total: {self.grd_total}")
           # self.bill_txt.insert(END,"\n =================================================================================")


        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("") 

        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()

        def add_func():
            qty = int(item_qty.get())
            cones = int(cone.get())
            total = qty * cones
            total_list.append(total)
            self.bill_txt.insert(END,f"\n {item_pur.get()}\t\t            {item_qty.get()}\t\t\t  RS. {cone.get()}\t\t      Rs. {total}")
        
        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n==========================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t\tGrand Total :{self.grd_total}")
            self.bill_txt.insert(END,"\n==========================================================================")            
        
        def save_func():
            user_choice = messagebox.askyesno("Confirm?",f"do you want to save the bill {bill_no_tk.get()}")
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                con = open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")
                con.write(self.bill_content)
                con.close()
                messagebox,messagebox.showinfo("Success!!",f"Bill {bill_no_tk.get()} has been saved succesfully",parent=self.win)
            else:
                return


 #========================= Buttons ======================================
        self.button_frame = LabelFrame(self.entry_frame,bd=4,text="options",bg="lightgrey",font=('Arial,15'))
        self.button_frame.place(x=20,y=280,width=470,height=300)

        self.add_btn = Button(self.button_frame,bd=4,text="Add",font=('Arial,12'),width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        
        self.generate_btn = Button(self.button_frame,bd=4,text="Generate",font=('Arial,12'),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn = Button(self.button_frame,bd=4,text="Clear",font=('Arial,12'),width=12,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)


        self.total_btn = Button(self.button_frame,bd=4,text="Total",font=('Arial,12'),width=12,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.reset_btn = Button(self.button_frame,bd=4,text="Reset",font=('Arial,12'),width=12,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.save_btn = Button(self.button_frame,bd=4,text="save",font=('Arial,12'),width=12,height=3,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)

        #self.add_btn = Button(self.button_frame,bd=4,text="Add",font=('Arial,12'),width=12,height=3)
        #self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        self.var_txt=StringVar()
        self.var_operator=''
        #==========================================================
        

        self.bill_no_lbl = Label(self.entry_frame,text="BILL NUMBER ",font=('arial,15'),bg="yellow")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)
        self.bill_no_ent = Entry(self.entry_frame,bd=5,textvariable=bill_no_tk,bg="orange",fg="black",font=('Arial,15'))
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        #self.bill_no_ent.config(state="disabled")
        
        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name ",font=('arial,15'),fg="black",bg="yellow")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)
        self.cust_nm_ent= Entry(self.entry_frame,bd=5,textvariable=cust_nm,bg="orange",fg="black",font=('Arial,15'))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)
        
        self.cust_cot_lbl = Label(self.entry_frame,text="Customer Contact ",font=('arial,15'),fg="black",bg="yellow")
        self.cust_cot_lbl.grid(row=2,column=0,padx=2,pady=2)
        self.cust_cot_ent = Entry(self.entry_frame,bd=5,textvariable=cust_cot,bg="orange",fg="black",font=('Arial,15'))
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl = Label(self.entry_frame,text="Date ",font=('arial,15'),bg="yellow")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)
        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,bg="orange",fg="black",font=('Arial,15'))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.item_pur_lbl = Label(self.entry_frame,text="Item Purchased ",font=('arial,15'),fg="black",bg="yellow")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,bg="orange",fg="black",font=('Arial,15'))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qty_lbl = Label(self.entry_frame,text="Item Quantity ",font=('arial,15'),bg="yellow")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)
        self.item_qty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty,bg="orange",fg="black",font=('Arial,15'))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl = Label(self.entry_frame,text="Cost Of One ",font=('arial,15'),bg="yellow")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)
        self.cost_one_ent = Entry(self.entry_frame,bd=5,textvariable=cone,bg="orange",fg="black",font=('Arial,15'))
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)
        # ===========================================================
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
                
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
        Cal_Frame=Frame(self.win,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=590,y=110,width=250,height=305)

        txt_Result=Entry(Cal_Frame,bg='lightyellow',textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT)
        txt_Result.place(x=0,y=0,relwidth=1,height=50)

        #===========Row1=================

        btn_7=Button(Cal_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=0,y=52,width=60,height=60)
        btn_8=Button(Cal_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=61,y=52,width=60,height=60)
        btn_9=Button(Cal_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=122,y=52,width=60,height=60)
        btn_div=Button(Cal_Frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=183,y=52,width=60,height=60)
        
        #============Row2=================
        btn_4=Button(Cal_Frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=0,y=112,width=60,height=60)
        btn_5=Button(Cal_Frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=61,y=112,width=60,height=60)
        btn_6=Button(Cal_Frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=122,y=112,width=60,height=60)
        btn_mul=Button(Cal_Frame,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold",),bg="orange",fg="white").place(x=183,y=112,width=60,height=60)
        
        #============Row3=================
        btn_1=Button(Cal_Frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=0,y=172,width=60,height=60)
        btn_2=Button(Cal_Frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=61,y=172,width=60,height=60)
        btn_3=Button(Cal_Frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold"),bg="black",fg="white").place(x=122,y=172,width=60,height=60)
        btn_sub=Button(Cal_Frame,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=183,y=172,width=60,height=60)
        
        #============Row 4=================
        btn_0=Button(Cal_Frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold"),bg="grey",fg="white").place(x=0,y=232,width=60,height=60)
        btn_dot=Button(Cal_Frame,text='C',command=clear_cal,font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=61,y=232,width=60,height=60)
        btn_add=Button(Cal_Frame,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=122,y=232,width=60,height=60)
        btn_equal=Button(Cal_Frame,text='=',command=result,font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=183,y=232,width=60,height=60)

#==================== Bill Frame ========================================================
        self.bill_frame = LabelFrame(self.win,text="Bill Area",font=("arial",18),bg="yellow",bd=8,relief=GROOVE)
        self.bill_frame.place(x=585,y=420,width=650,height=320)

        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt= Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()


if __name__ == '__main__':
    main()
