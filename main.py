from tkinter import*

# import pillow
from PIL import Image, ImageTk

import speedtest



co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue

# Logica


def testingNet():
    speed = speedtest.Speedtest()
    donwload = f'{'{:.2f}'.format(speed.download() / 1024 / 1024)}'
    upload = f'{'{:.2f}'.format(speed.upload() / 1024 / 1024)}'
    
    label_download['text'] = donwload
    label_upload['text'] = upload
    
    button['text'] = 'Testar novamente'
    button.place(x=100,y=100)


# ? Criação da janela

janela = Tk()
janela.title ("")
janela.geometry("350x200")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


frame_logo = Frame(janela, width=350, height=60, background=co1)
frame_logo.grid(row=0, column=0, pady=2, padx=0, sticky=NSEW)

frame_body = Frame(janela, width=350, height=140, background=co1)
frame_body.grid(row=1, column=0, pady=2, padx=0, sticky=NSEW)

# configurando o header do frame

imagem = Image.open('./img/fast.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

label_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), background=co1, fg=co3)
label_logo_imagem.place(x=20,y=0)

label_logo_title = Label(frame_logo, text='Teste de rede', padx=10, anchor=NE, font=('Ivy 19 bold'), background=co1, fg=co4)
label_logo_title.place(x=75,y=10)

divider = Label(frame_logo, width=350,  padx=10, anchor=NW, font=('Ivy 1 bold'), background=co5)
divider.place(x=0,y=57)

# Body do frame


# download

label_download = Label(frame_body, text='', anchor=NW, font=('arial 20'), background=co1, fg=co4)
label_download.place(x=44, y=25)

label_download_mb = Label(frame_body, text='Mbps download', anchor=NW, font=('Ivy 10'), background=co1, fg=co4)
label_download_mb.place(x=35, y=70)

imagem_down = Image.open('./img/down.png')
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)

label_logo_down = Label(frame_body, height=60, image=imagem_down, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), background=co1, fg=co3)
label_logo_down.place(x=130,y=15)

# upload

label_upload = Label(frame_body, text='', anchor=NW, font=('arial 20'), background=co1, fg=co4)
label_upload.place(x=235, y=25)

label_upload_up = Label(frame_body, text='Mbps upload', anchor=NW, font=('Ivy 10'), background=co1, fg=co4)
label_upload_up.place(x=230, y=70)

imagem_up = Image.open('./img/up.png')
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)

label_logo_up = Label(frame_body, height=60, image=imagem_up, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), background=co1, fg=co3)
label_logo_up.place(x=180,y=15)

# button

button = Button(frame_body, text='Iniciar', compound=LEFT, padx=10, relief=RAISED, font=('Ivy 10 bold'), background=co5, fg=co1, overrelief=RIDGE, command=testingNet)
button.place(x=145,y=100)





janela.mainloop()