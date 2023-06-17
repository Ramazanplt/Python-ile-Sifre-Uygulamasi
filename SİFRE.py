import tkinter as tk

arayuz = tk.Tk()
arayuz.title("Sifre")
arayuz.geometry("300x200")
a1 = 'Ramazan Polat'
a2 = '3112567'

kullanıcı = tk.Label(text="KULLANICI ADI: ")
kullanıcı.place(x=10, y=10)

y = tk.StringVar()
kullanıcı_girişi = tk.Entry(textvariable=y)
kullanıcı_girişi.place(x=100, y=10)


kullanıcı = tk.Label(text="SIFRE GIRISI: ")
kullanıcı.place(x=20, y=35)

x = tk.StringVar()
kullanıcı_girişi = tk.Entry(textvariable=x)
kullanıcı_girişi.place(x=100, y=35)

dogru_yanlıs = tk.Label(font='verdana 30 bold')
dogru_yanlıs.place(x=70, y=95)


def gırıs_komut():
    kullan = y.get()
    sif = x.get()
    print(kullan, "\n"+sif)
    if kullan == a1 and sif == a2:
        print("doğru")
        dogru_yanlıs.config(text="DOĞRU", fg="green")
    else:
        print("yanlıs")
        dogru_yanlıs.config(text="YANLIŞ", fg="red")


Gırıs = tk.Button(text="GIRIS", command=gırıs_komut)
Gırıs.place(x=186, y=55)

arayuz.mainloop()
