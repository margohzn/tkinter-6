from tkinter import * 

window = Tk()
window.geometry("500x500")
window.title("My favrioute ice-ceams")


#creating list box 
list_box1 = Listbox(window, height = 2, width = 20, font = "Helvetica", fg = "pink", bg = "grey", activestyle = "dotbox")

#inserting items into a listbox
list_box1.insert(1, "banana_ice-cream")
list_box1.insert(2, "pistachio_ice-cream")
list_box1.insert(3, "caramel_ice-cream")
list_box1.insert(4, "mango_ice-cream")
list_box1.insert(5, "strawberry_ice-cream")
list_box1.insert(6, "rasberry_ice-cream")

for i in range(7, 20):
    list_box1.insert(END, "ice-cream"+ str(i))


list_box1.place(x = 10, y = 10)


scrollbar1 = Scrollbar(list_box1)
scrollbar1.place(relheight = 1, relx = 1)


scrollbar1.config(command = list_box1.yview)

window.mainloop()