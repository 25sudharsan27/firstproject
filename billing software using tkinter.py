from tkinter import *
import math,random
from tkinter import messagebox
import os
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",font=("times new roman",30,"bold"),pady=2,relief=GROOVE,bg=bg_color,bd=12,fg="white")
        title.pack(fill=X)

        #====================variables=================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #================grocery=======================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #===============cold drinks===================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        #=============Total Product Price & Tax Variable=======
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #==================Customer==============================
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #=======================Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",15,"bold"),bg=bg_color,fg="white")
        cname_lbl.grid(row=0,column=0,padx=20,pady=5)

        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font=("arial",15),bd=7,relief=SUNKEN)
        cname_txt.grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Customer Phone No.", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)

        cphn_txt = Entry(F1, width=15,textvariable=self.c_phon, font=("arial", 15), bd=7, relief=SUNKEN)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)

        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill, font=("arial", 15), bd=7, relief=SUNKEN)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=5,pady=10)
        #======Cosmetrics Frame +=============================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times  new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_labl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        bath_txt = Entry(F2, width=10,textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        Face_cream_labl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Face_wash_labl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Face_wash_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Hair_s_labl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Hair_s_txt = Entry(F2, width=10,textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Hair_g_labl = Label(F2, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        Hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        Body_labl = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky=W)
        Body_txt = Entry(F2, width=10,textvariable=self.loshan, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # ======Grocery Frame +=============================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times  new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)
        Rice_labl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Rice_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        Food_Oil_labl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Food_Oil_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        Daal_labl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                                fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Daal_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        Wheat_labl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Wheat_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=10)

        Sugar_labl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        Sugar_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        Tea_labl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky=W)
        Tea_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        # ======Drinks=============================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drinks", font=("times  new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=675, y=180, width=325, height=380)
        Maza_labl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Maza_txt = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        Cock_labl = Label(F4, text="Cock", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Cock_txt = Entry(F4, width=10,textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)

        Frooti_labl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Frooti_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                       column=1,
                                                                                                       padx=10,
                                                                                                       pady=10)

        Thumbs_Up_labl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Thumbs_Up_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                        column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

        Limca_labl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        Limca_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                        column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

        Sprite_labl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky=W)
        Sprite_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                      column=1,
                                                                                                      padx=10,
                                                                                                    pady=10)


        #===== Bill  Area=====================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1100, y=180, width=380, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=============Button Frame===============
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times  new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=20,pady=1,sticky=W)
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=20, pady=1, sticky=W)
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=20, pady=1, sticky=W)
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Total Cosmetic Tax", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=2, padx=20, pady=1, sticky=W)
        c1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Total Grocery Tax", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=2, padx=20, pady=1, sticky=W)
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Total Cold Drinks Tax", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=2, padx=20, pady=1, sticky=W)
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=800,width=580,height=105)
        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=10,font="arial 12 bold",bd=2).grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_F,command=self.bill_area, text="Generage Bill", bg="cadetblue", fg="white", pady=15, width=10, font="arial 12 bold",
                           bd=2).grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", pady=15, width=10, font="arial 12 bold",
                           bd=2).grid(row=0, column=2, padx=5, pady=5)
        Exit_btn= Button(btn_F,command=self.Exit_app, text="Exit", bg="cadetblue", fg="white", pady=15, width=10, font="arial 12 bold",
                           bd=2).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=(self.soap.get()*40)
        self.c_fc_p=(self.face_cream.get() * 120)
        self.c_fw_p=(self.face_wash.get() * 60)
        self.c_hs_p=(self.spray.get() * 180)
        self.c_hg_p=(self.gell.get() * 140)
        self.c_b1_p=(self.loshan.get() * 180)
        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_b1_p
        )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.c_tax =round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs."+str(self.c_tax))

        self.g_r_p=(self.rice.get()*180)
        self.g_f_p=((self.food_oil.get()*180))
        self.g_d_p=(self.daal.get()*60)
        self.g_w_p=(self.wheat.get()*40)
        self.g_s_p=(self.sugar.get()*45)
        self.g_t_p=(self.tea.get()*150)
        self.total_grocery_price=float(
            self.g_r_p+
            self.g_f_p+
            self.g_d_p+
            self.g_w_p+
            self.g_s_p+
            self.g_t_p

        )

        self.d_m_p=(self.maza.get() * 60)
        self.d_c_p=(self.cock.get() * 60)
        self.d_f_p=(self.frooti.get() * 50)
        self.d_t_p=(self.thumbsup.get() * 45)
        self.d_l_p=(self.limca.get() * 40)
        self.d_s_p=(self.sprite.get() * 60)

        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs."+str(self.g_tax))
        self.total_drinks_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p+
            self.d_l_p+
            self.d_s_p

        )
        self.cold_drink_price.set("Rs."+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drink_tax.set("Rs."+str(self.d_tax))
        self.Total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_drinks_price +self.c_tax+self.g_tax+self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Webcode Retail\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number :{self.c_phon.get()}")
        self.txtarea.insert(END, f"\n=======================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product purchased")
        else:
            self.welcome_bill()
            #===========cosmetics===============
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hari Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hari Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan \t\t{self.loshan.get()}\t\t{self.c_b1_p}")

            #=======Grocery================
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea \t\t{self.tea.get()}\t\t{self.g_t_p}")
            # ==========Drinks===================================
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.rice.get()}\t\t{self.d_m_p}")
            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\n Cocokola\t\t{self.food_oil.get()}\t\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumbsup\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite \t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END,f"\n------------------------------------------")
            if self.cosmetic_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Cool Drinks Tax\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END, f"\n Total Bill\t\t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END,f"\n------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no: {self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                self.txtarea.insert(END,f1)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            # ====================variables=================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            # ================grocery=======================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ===============cold drinks===================
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            # =============Total Product Price & Tax Variable=======
            self.cosmetic_price.set(0)
            self.grocery_price.set(0)
            self.cold_drink_price.set(0)

            self.cosmetic_tax.set(0)
            self.grocery_tax.set(0)
            self.cold_drink_tax.set(0)

            # ==================Customer==============================
            self.c_name.set(0)
            self.c_phon.set(0)

            self.bill_no.set(0)
            x = random.randint.set(0)
            self.bill_no.set(0)
            self.search_bill.set(0)
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()
root=Tk()
obj=Bill_App(root)
root.mainloop()