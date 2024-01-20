from tkinter import *
import requests

def get_quote():
    url_link = 'https://api.kanye.rest'
    response = requests.get(url=url_link)
    response.raise_for_status()
    data = response.json()
    qoute = data['quote']
    canvas.itemconfig(quote_text,text=qoute)
    

windows =Tk()
windows.title('Auto Quotes Generator')
windows.config(padx=60,pady=50)

canvas = Canvas(width=470,height=450)
bg_img = PhotoImage(file='Yellow-removebg-preview.png')
canvas.create_image(235,250,image=bg_img)
quote_text = canvas.create_text(340,365,text="Hari's Quote Goes Here",width=250,font=('Helvetica',18,'italic'))
quote_text = canvas.create_text(235,220,text="Quote Here",width=250,font=('Arial',15,'italic'))
canvas.grid(row=0,column=0)

photo_img = PhotoImage(file='HariImg-removebg-preview.png')
img_button = Button(image=photo_img,highlightthickness=0,height=200,width=150,command=get_quote)
img_button.grid(row=1,column=0)
label = Label(windows,text='Click On Me, to Get Quote..!',font=('Helvetica',12,'italic'),fg='red')
label.grid(row=2,column=0)

windows.mainloop()