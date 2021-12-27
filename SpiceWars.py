import tkinter, random
#------------------------------------
#------- Beginnvariablen-------------
#------------------------------------
Geld = 1000
Laderaum = 100
Gewuerze = ["Pfeffer", "Muskat", "Nelken", "Vanille", "Zimt"]

aktKosten = [100, 30, 50 , 20 ,10]
KostenMin = [50, 5 , 20 , 100, 60]
KostenMax = [150, 35 , 170 , 450, 300]
EigeneLadung = [0,0,0,0,0]
Ort = "Tatooine"
HP = 100
MaxHP = 100
SchiffeListe = ["X-Wing", "Y-Wing", "A-Wing"]
LaderaumSchiffe =[100,120,150]
hpschiffe=[150,150,200]
schiffpreis=[10000,20000,50000]
Info = ["Zurzeit keine Infos"]
Farbe = "bisque2"
FarbePlanet = ["green2","bisque2","LightCyan2","Deepskyblue4","forestgreen","SpringGreen4"]
#-----------------------------------------------------------
#------- Spielinhalte --- (Hintergrundfunktionen) ----------
#-----------------------------------------------------------

def LebenSchiff():
  global HP
  x = random.randint(1,100)
  if HP > 0:
    HP = HP - 1
  if x == 17 or x == 53:
    HP = HP - random.randint(20,60)
    tkinter.messagebox.showwarning("- SONNENSTURM -","Ihr Schiff hat Schaden genommen.\n")
  if HP <= 0:
    tkinter.messagebox.showerror("- G A M E  O V E R -","Sie wurden zerstÃ¶rt.\n\nDas Spiel ist vorbei...")
    exit()

  
def Piraten():
  global HP
  global EigeneLadung
  h = random.randint(1,40)
  if h == 17:
    HP = HP - random.randint(50,90)
    tkinter.messagebox.showinfo("  - P I R A T E N ! -  ", "Du wurdest von Piraten Ã¼berfallen und hast Schaden genommen.\n Alle deine Waren wurden gestohlen!")
    EigeneLadung = [0,0,0,0,0]
  if HP <= 0:
    tkinter.messagebox.showerror("- G A M E  O V E R -","Sie wurden zerstÃ¶rt.\n\nDas Spiel ist vorbei...")
    exit()


#def Zeit(): #Epochen oder ablaufende Zeit?
  

def DisplayAktualisieren():
  global Gewuerze
  global aktKosten
  global EigeneLadung
  global Geld
  global Laderaum
  global SchiffeListe, LaderaumSchiffe, hpschiffe, schiffpreis, Laderaum
  global Info
  global Farbe
  Fenster.configure(bg=str(Farbe))
  
  Liste.delete("0","end")
  Liste.insert("end", Gewuerze[0] + "  " + str(aktKosten[0]))
  Liste.insert("end", Gewuerze[1] + "  " + str(aktKosten[1]))
  Liste.insert("end", Gewuerze[2] + "  " + str(aktKosten[2]))
  Liste.insert("end", Gewuerze[3] + "  " + str(aktKosten[3]))
  Liste.insert("end", Gewuerze[4] + "  " + str(aktKosten[4]))
  
  ListeLaderaum.delete("0","end")
  ListeLaderaum.insert("end", str(EigeneLadung[0]) + " Einheiten: " + str(Gewuerze[0])) 
  ListeLaderaum.insert("end", str(EigeneLadung[1]) + " Einheiten: " + str(Gewuerze[1]))
  ListeLaderaum.insert("end", str(EigeneLadung[2]) + " Einheiten: " + str(Gewuerze[2]))                     
  ListeLaderaum.insert("end", str(EigeneLadung[3]) + " Einheiten: " + str(Gewuerze[3]))
  ListeLaderaum.insert("end", str(EigeneLadung[4]) + " Einheiten: " + str(Gewuerze[4]))
  ListeLaderaum.insert("end", "-------")
  ListeLaderaum.insert("end", "Goldtaler: " + str(Geld))
  ListeLaderaum.insert("end", "Platz im Laderaum: " + str(Laderaum))
  ListeLaderaum.insert("end", "HP: " + str(HP))

  ListeSchiffe.delete("0","end")
  ListeSchiffe.insert("end", str(SchiffeListe[0]) + " - " + "Laderaum: " + str(LaderaumSchiffe[0]) + " - " + " HP: " + str(hpschiffe[0]) + " - " + "Preis: " + str(schiffpreis[0]))
  ListeSchiffe.insert("end", str(SchiffeListe[1]) + " - " + "Laderaum: " + str(LaderaumSchiffe[1]) + " - " + " HP: " + str(hpschiffe[1]) + " - " + "Preis: " + str(schiffpreis[1]))
  ListeSchiffe.insert("end", str(SchiffeListe[2]) + " - " + "Laderaum: " + str(LaderaumSchiffe[2]) + " - " + " HP: " + str(hpschiffe[2]) + " - " + "Preis: " + str(schiffpreis[2]))

  
  ListeStaedte.delete("0","end")
  ListeStaedte.insert("end", "Alderaan")
  ListeStaedte.insert("end", "Tatooine")
  ListeStaedte.insert("end", "Naboo")
  ListeStaedte.insert("end", "Kamino")
  ListeStaedte.insert("end", "Kashyyyk")
  ListeStaedte.insert("end", "Yavin IV")

  LabelOrt.config(text ="aktueller Ort: " + str(Ort))
  LabelInfo.config(text ="Info: " + str(Info))


#----------------------------------------------------------
#----- Buttons --------------------------------------------
#----------------------------------------------------------
def NeuesSpiel():
  global aktKosten
  global EigeneLadung
  global Geld
  global Laderaum
  global Ort
  global SchiffeListe, LaderaumSchiffe, hpschiffe, schiffpreis
  global Info
  global Farbe
  aktKosten = [100, 30, 50 , 20 ,10]
  EigeneLadung = [0,0,0,0,0]
  Geld = 1000
  Laderaum = 100
  DisplayAktualisieren()
  Ort = "Tatooine"
  Farbe = "bisque2"
  HP = 100
  SchiffeListe = ["X-Wing", "Y-Wing", "A-Wing"]
  LaderaumSchiffe =[100,120,150]
  hpschiffe=[150,150,200]
  schiffpreis=[10000,20000,50000]
  Info = ["Zurzeit keine Infos"]

def kaufen():
  global Geld
  global aktKosten
  global EigeneLadung
  global Laderaum
  Anzahl = int(EingabeMenge.get())
  Nummer = int(Liste.curselection()[0])
  if (Laderaum >= Anzahl) and (Geld >= aktKosten[Nummer]*Anzahl):
      Laderaum = Laderaum - Anzahl
      Geld = Geld - int(aktKosten[Nummer])*Anzahl
      EigeneLadung[Nummer] = EigeneLadung[Nummer]+Anzahl
  DisplayAktualisieren()


def verkaufen():
  global Geld
  global aktKosten
  global EigeneLadung
  global ListeLaderaum
  global Laderaum
  Anzahl = int(EingabeMenge.get())
  Nummer = int(ListeLaderaum.curselection()[0])
  if (Anzahl <= EigeneLadung[Nummer]):
      Laderaum = Laderaum + Anzahl
      Geld = Geld + int(aktKosten[Nummer])*Anzahl
      EigeneLadung[Nummer] = EigeneLadung[Nummer] - Anzahl
  DisplayAktualisieren()

def Weitersegeln():
  global Farbe
  global FarbePlanet
  global Ort
  global ListeStaedte
  global aktKosten
  global KostenMin
  global KostenMax
  Nummer = int(ListeStaedte.curselection()[0])
  Stadt = ListeStaedte.get(Nummer)
  Farbe = FarbePlanet[Nummer]
  Ort = str(Stadt)
  tkinter.messagebox.showinfo("- R E I S E I N F O -","Ihre Reise geht nach " + Stadt )
  for i in range (5):
    aktKosten[i] =  random.randint(KostenMin[i],KostenMax[i])
  Piraten()
  LebenSchiff()
  DisplayAktualisieren()

def Schiffe():
  global Geld
  global schiffpreis
  global LaderaumSchiffe
  global EigeneLadung
  global ListeSchiffe
  global Laderaum
  Nummer = int(ListeSchiffe.curselection()[0])
  if (Geld >= schiffpreis[Nummer]):
      Laderaum = int(LaderaumSchiffe[Nummer])
      MaxHP = int(hpschiffe[Nummer])
      Geld = Geld - int(schiffpreis[Nummer])
      EigeneLadung = [0,0,0,0,0]
  DisplayAktualisieren()

def Reparatur():
  global HP
  global MaxHP
  global Geld
  if Geld>= 50 and HP != MaxHP:
    HP = MaxHP
    Geld = Geld - 50
  DisplayAktualisieren()
#------------------ GUI -------------------------------------------------------------------------------------
#----------------- Hauptfenster -----------------------------------------------------------------------------

  
Fenster = tkinter.Tk()
Fenster.title("SpiceWars")
#Fenster.background=("100")
Fenster.configure(bg=str(Farbe))


#---------------------------------------------------------------
#--------------- Label -----------------------------------------
#---------------------------------------------------------------

LabelInfo = tkinter.Label(Fenster, text = "Info: " + str(Info))
LabelInfo.grid (padx = 5, pady=5, row = 0, column = 5)

LabelMenge = tkinter.Label(Fenster, text = 'Menge: ')
LabelMenge.grid (padx = 5, pady=5, row = 0, column = 2)

LabelOrt = tkinter.Label(Fenster, text = 'aktueller Ort: '+ str(Ort))
LabelOrt.grid (padx = 5, pady=5, row = 11, column = 8)

LabelOrt2 = tkinter.Label(Fenster, text = 'Bereisbare Orte: ')
LabelOrt2.grid (padx = 5, pady=5, row = 0, column = 8)

LabelSchiffe = tkinter.Label(Fenster, text = 'Schiffe: ')
LabelSchiffe.grid (padx = 5, pady=5, row = 0, column = 10)



#-------------------------------------------------------------
#------------ Listbox & Eingabe ------------------------------
#-------------------------------------------------------------


Liste = tkinter.Listbox (width=30, height = 20)
Liste.grid(padx = 5, pady = 5, row = 1, column = 1, columnspan = 1, rowspan=9)

ListeStaedte = tkinter.Listbox (width=30, height = 20)
ListeStaedte.grid(padx = 5, pady = 20, row = 1, column = 8, columnspan = 1, rowspan=9)

ListeLaderaum = tkinter.Listbox (width=30, height = 20)
ListeLaderaum.grid(padx = 5, pady = 5, row = 1, column = 5, columnspan = 2, rowspan=9)

ListeSchiffe = tkinter.Listbox (width=60, height = 20)
ListeSchiffe.grid(padx = 5, pady = 5, row = 1, column = 10, columnspan = 1, rowspan=9)

EingabeMenge = tkinter.Entry(Fenster, width = 4)
EingabeMenge.grid(padx = 5, pady = 5, row = 0, column = 3)


#-----------------------------------------------------------
#------------ Buttons --------------------------------------
#-----------------------------------------------------------


ButtonKaufen = tkinter.Button(Fenster, text=' kaufen  >>> ', command = kaufen)
ButtonKaufen.grid(padx=5, pady = 5, row =2, column = 2, columnspan=2)

ButtonReperatur = tkinter.Button(Fenster, text=' Reperatur ', command = Reparatur)
ButtonReperatur.grid(padx=5, pady = 5, row =7, column = 2, columnspan=2)

ButtonVerkaufen = tkinter.Button(Fenster, text=' <<< verkaufen ', command = verkaufen)
ButtonVerkaufen.grid(padx=5, pady = 5, row =3, column = 2, columnspan=2)

ButtonBewegen = tkinter.Button(Fenster, text = ' Sprung in den Hyperraum ', command = Weitersegeln)
ButtonBewegen.grid(row=4, column=2, padx=5, pady=25, columnspan = 2)

ButtonNeustart = tkinter.Button(Fenster, text = ' neues Spiel ', command = NeuesSpiel)
ButtonNeustart.grid(row=0, column=1, padx=5, pady=10)

NeuesSpiel()
# ---------------------
Fenster.mainloop()

