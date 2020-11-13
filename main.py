import tkinter as tk
import pickle

#--------pickel list------
filename = 'betalinger.pk'
infile = open(filename, 'rb')
dict = pickle.load(infile)
infile.close()

def save():
    # vi åbner pickel filen med open(filename) som vi giver en variabel
    outfile = open(filename, 'wb')
    # men filen er åben lægger vi infomtion i den med .dump
    pickle.dump(dict, outfile)
    # så lukker vi filen og det er gemt.
    outfile.close()


def top3():
    # her laver vi et vinduet for vores liste.
    top3_window = tk.Toplevel()
    top3_window.title("top 3 værste")

    # her har vi en liste som kommer fra vores pickel. som vi sotere efter størelse (kv 1, 2, og 3)
    top3_mindst = list(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))[:3]

    # vi laver et label som kan vise vores liste.
    top3_display = tk.Label(top3_window, text= top3_mindst)
    # her pakker vi vores label ind i winduet
    top3_display.pack()



#---main_window---
# laver en variabel window
window = tk.Tk()
# giver vores windo en titel
window.title("Fodboldtur.py")

window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=700, weight=0)

menu_frame = tk.Frame(window)
display_frame = tk.Frame(window)

#-----funktioner-----

def betal():
    # vi laver et vindue.
    betal=tk.Toplevel()
    # vi giver en titel til vinduet
    betal.title("betal")

    #overfør
    # for at betale skal vi have noget at betale til. vi bruger .get til at hent keys og values fra vores safefile.
    overfør = tk.Button(betal, text = "betal", command = lambda: overførsler(variabel.get(), overførsel.get()))
    overfør.pack()

    gemmer = tk.Button(betal, text="gem", command = save)
    gemmer.pack()

    #Værdi liste
    overførsel = tk.Spinbox(betal, values=(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500,
                                                 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000))

    overførsel.pack()

    #bruger liste
    variabel = tk.StringVar(betal)

    # variablen
    #variablen bestemmes af brugeren med .set
    variabel.set("vælg bruger")
    betal_nu = tk.OptionMenu(betal, variabel, *dict.keys())
    betal_nu.pack()


def overførsler(navn, værdi):

    dict[navn] += int(værdi)
    overfør_liste()


def overfør_liste():
    Of_liste = tk.Toplevel()
    Of_liste.title("betal")

    #listbox laver en liste over
    bruger_keys = tk.Listbox(Of_liste)

    #enumerate tæller hver key i listen så de får en værdi
    #
    for index, navn in enumerate(dict.keys()):
        bruger_keys.insert(index + 1, navn)

    #her placere vi vores liste af keys med .pack = left
    bruger_keys.pack(side = tk.LEFT)
    Key_værdi = tk.Listbox(Of_liste)


    for index, value in enumerate(dict.values()):
        Key_værdi.insert(index + 1, value)

    Key_værdi.pack(side = tk.RIGHT)


def menu():

    # ideen var at indele GUIen i en menu/knappe del og en display/skærm del.
    # vi tilknytter en variabel til vores frame.
    # vi tilknytter en master hvilket er vores window.
    buttons_frame = tk.Frame(window,bg="black")
    display_frame = tk.Frame(window, bg = "grey", borderwidth=5, relief="ridge")

    #--------knapper------
    # .button er en funktion fra tkinter som laver en knap.
    # alle knapperne har en variabel som skal bruges til at placere dem på vores window.
    btn_menu = tk.Label(buttons_frame, text="Menu", bg="red", font=("Times New Roman", 15))
    btn_save = tk.Button(buttons_frame, text="Gem",command=save)
    btn_top3 = tk.Button(buttons_frame, text="top3", command=top3)
    btn_liste = tk.Button(buttons_frame, text="Delgere", command=overfør_liste)
    btn_betal = tk.Button(buttons_frame, text="Betal", command=betal)
    btn_dinliste = tk.Button(buttons_frame, text="Din liste")#, command= nåede ikke at lave.)
    btn_sluk = tk.Button(buttons_frame, text="Sluk", command=window.destroy)

    #.grid indeler vinduet i et koordinatsystem.
    # row er række/y koordinat. column er liste/x koordinat.
    # padx er mellemrum fra en widget på dens x-akse
    # pady er mellemrum fra en widget på dens y-akse
    btn_menu.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=6, column=0, sticky="ew", padx=5, pady=2)
    btn_top3.grid(row=2, column=0, sticky="ew", padx=5, pady=2)
    btn_liste.grid(row=3, column=0, sticky="ew", padx=5, pady=2)
    btn_betal.grid(row=4, column=0, sticky="ew", padx=5, pady=2)
    btn_dinliste.grid(row=5, column=0, sticky="ew", padx=5, pady=2)
    btn_sluk.grid(row=6, column=2, sticky="ew", padx=5, pady=10)

    # har bruges .grid til at placere vores frames.
    buttons_frame.grid(row=0, column=0, sticky="nw",)
    # sticky indikere hvor på window frame skal ligge. n = nord, s = syd, e = øst, w = west.
    display_frame.grid(row=1, column=0, sticky="ne")

menu()


window.mainloop()
