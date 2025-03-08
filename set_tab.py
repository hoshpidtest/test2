import customtkinter
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import hupper

def start_reloader():
    reloader=hupper.start_reloader('set_tab.py')

app = customtkinter.CTk()
app.title("my app")


tabview = customtkinter.CTkTabview(master=app,width=0.98*1080,height=0.82*720,corner_radius=20,fg_color="#dcdedd",segmented_button_fg_color="#808080"
                   ,segmented_button_selected_color="#b2ffd8",segmented_button_unselected_color="#8eccac",
                   text_color="black")
tabview.pack(padx=20, pady=20)

tab_Register=tabview.add("نام ثبت")
tab_Work=tabview.add(" عملکرد")
tab_report=tabview.add("گیری گزارش")
tab_setting=tabview.add("تنظیمات")

tree_frame_persons=customtkinter.CTkFrame(master=tab_setting,fg_color="#eeeeee",border_color="#000000",border_width=2)
tree_frame_persons.place(relx=0.47,rely=0.001,anchor='nw')

tree_scroll_persons=tk.Scrollbar(tree_frame_persons)
tree_scroll_persons.pack(side="right",fill="y")

font2=('Arial',12,'bold')
style=ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview',fount=font2,foreground='black',background='#D3D3D3',rowheight=25,fieldbackground='#D3D3D3')
style.map('Treeview',background=[('selected','#1A8F2D')])

tree_persons=ttk.Treeview(tree_frame_persons,height=5,yscrollcommand=tree_scroll_persons.set,selectmode='extended')
tree_persons['columns']=('hrs','title','post')
tree_persons.column('#0',width=0,stretch=tk.NO)


tree_persons.column('post',anchor=tk.CENTER,width=90)
tree_persons.column('title',anchor=tk.CENTER,width=90)
tree_persons.column('hrs',anchor=tk.CENTER,width=90)

tree_persons.heading("post",text="کد")
tree_persons.heading("title",text="عنوان")
tree_persons.heading("hrs",text="ساعت")




tree_persons.pack()
tree_scroll_persons.config(command=tree_persons.yview)

def button_event():
    print("registered")



frame_entry_register=customtkinter.CTkFrame(master=tab_setting,fg_color="#eeeeee",border_color="#000000",border_width=2,width=int(1080/4.7),height=int(720/4.5))
frame_entry_register.place(relx=0.999,rely=0,anchor="ne")

entry_title=tk.Entry(master=frame_entry_register,width=int(1080/60),bd=5, justify='right')
entry_title.place(relx=0.1,rely=0.2,anchor="nw")
label_title=tk.Label(master=frame_entry_register,text="عنوان",font=("B zar",14))
label_title.place(relx=0.95,rely=0.2,anchor="ne")
entry_title.insert(0,1)

entry_post=tk.Entry(master=frame_entry_register,width=int(1080/60),bd=5, justify='right')
entry_post.place(relx=0.1,rely=0.03,anchor="nw")
label_post=tk.Label(master=frame_entry_register,text="کد ",font=("B zar",14))
label_post.place(relx=0.95,rely=0.03,anchor="ne")
label_post=tk.Label(master=frame_entry_register,text="",font=("B zar",14))
label_post.place(relx=0.4,rely=0.03,anchor="ne")

label_clock=tk.Label(master=frame_entry_register,text="ساعت",font=("B zar",14))
entry_clock=tk.Entry(master=frame_entry_register,width=int(1080/60),bd=5, justify='right')
label_clock.place(relx=0.95,rely=0.4,anchor="ne")
entry_clock.place(relx=0.1,rely=0.4,anchor="nw")



btn_Take_Picture=customtkinter.CTkButton(master=frame_entry_register, text="حذف",width=1080/15,font=("B zar",14),corner_radius=35,text_color="#000000",fg_color="#bdb3db",hover_color="#dfbcbb",border_color="#000000",border_width=2,command=button_event)
btn_Take_Picture.place(relx=0.48,rely=0.7,anchor="ne")
btn_Take_Picture=customtkinter.CTkButton(master=frame_entry_register, text="ثبت",width=1080/15,font=("B zar",14),corner_radius=35,text_color="#000000",fg_color="#bdb3db",hover_color="#dfbcbb",border_color="#000000",border_width=2)
btn_Take_Picture.place(relx=0.88,rely=0.7,anchor="ne")


if __name__ ==  "__main__":
    start_reloader()
    
app.mainloop()