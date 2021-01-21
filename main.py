from tkinter import *
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import socket

confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']

def check_host():
   global confiaveis
   for host in confiaveis:
     a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     a.settimeout(.5)
     try:
       b=a.connect_ex((host, 80))
       if b==0:
         return True
     except:
       pass
     a.close()
   return False

conexao = check_host()
if conexao == True:
   try:
      html = urlopen("https://www.cptec.inpe.br/ap/macapa")
   except HTTPError as e:
      print(e)
   except URLError:
      janela = Tk()
      janela.iconbitmap("teste.ico")
      janela["bg"] = "#FFFF00"
      janela.geometry("200x150+200+200")
      janela.title("AVISO")
      lb = Label(janela, text="Destino inoperante", background="#FFFF00", foreground="red", font = "Verdana 12 bold")
      lb.place(x=15, y=35)
      btclose = Button(janela, text="Sair", background="#DAA520", foreground="black")
      btclose.place(x=85, y=100)
      btclose.configure(command=janela.destroy)
   else:
       janela = Tk()
       janela.iconbitmap("teste.ico")
       janela["bg"] = "green"
       janela.geometry("300x300+200+200")
       janela.title("Temperatura")

       def bt_click():
           page = requests.get('https://www.cptec.inpe.br/ap/macapa')
           soup = BeautifulSoup(page.content, 'html.parser')
           tempe = soup.find(class_="bloco-previsao d-flex flex-column text-center")
           temp_max = tempe.find('label').get_text()
           lb = Label(janela, text="Temperatura máxima: "+str(temp_max)+str("C"), background="green", foreground="#00FA9A", font = "Helvetica 12 bold italic")
           lb.place(x=40, y=20)

       
       bt = Button(janela, width=20, text="Verifcar",background="#32CD32", foreground="#006400", command=bt_click)
       bt.place(x=80, y=120)
       btclose = Button(janela, text="Sair", background="#32CD32", foreground="#006400")
       btclose.place(x=140, y=150)
       btclose.configure(command=janela.destroy)

       lb2 = Label(janela, text="Erick Ximenes Vasconcelos", background="green", foreground="#00FA9A", font = "Verdana 10 bold")
       lb2.place(x=50, y=280)

       janela.mainloop()
else:
    janela = Tk()
    janela.iconbitmap("teste.ico")
    janela["bg"] = "#FFFF00"
    janela.geometry("200x150+200+200")
    janela.title("AVISO")
    lb = Label(janela, text="SEM CONEXAO", background="#FFFF00", foreground="red", font = "Verdana 12 bold")
    lb.place(x=35, y=35)
    btclose = Button(janela, text="Sair", background="#DAA520", foreground="black")
    btclose.place(x=85, y=70)
    btclose.configure(command=janela.destroy)
