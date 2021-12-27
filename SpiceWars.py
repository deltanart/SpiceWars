import tkinter, random
#------------------------------------
#------- Beginnvariablen-------------
#------------------------------------
Geld = 1000
Laderaum = 10
Gewuerze = ["Gewürze", "Ersatzteile", "Kyber-Kristalle", "Astromechs", "Raketenteile", "Treibstoff", "Sensorkomponenten", "Steuerungseinheiten","KI-Systeme","Werkzeuge","Durastahl","Energiedroiden","Rezeptoren","Nahrungsmittel"]

aktKosten = [30, 60, 300 , 150 ,800,500,60,50,80,30,90,300,20,40]
KostenMin = [25, 50 , 300 , 100, 600,400,40,50,70,10,70,250,13,20]
KostenMax = [100, 180 , 1700 , 450, 2000,1000,100,90,122,200,120,600,70,250]
EigeneLadung = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Ort = "Tatooine"
HP = 1
MaxHP = 100
SchiffeListe = ["A-Wing", "X-Wing", "BTL-A4 Y-Wing", "Slave I", "kleiner SternenjÃ¤ger", "AR-170", "P-38","T-2c Theta-Klasse Transporter", "Tantive IV", "Millenium Falke", "YT-1200", "TIE-X1", "T-4a Lambda-Klasse Transporter", "U-Wing", "SternenzerstÃ¶rer"]
LaderaumSchiffe =[100,120,150,300,150,180,200,500,1200,555,400,200,600,400,100000000]
hpschiffe=[150,150,200,500,200,250,250,400,1000,1500,900,300,500,400,100000000]
schiffpreis=[10000,20000,50000,100000,50000,60000,50000,110000,500000,200000,220000,30000,150000,100000,100000000]
Info = ["Zurzeit keine Infos"]
Farbe = "navajowhite2"
FarbePlanet = ["green2","navajowhite2","LightCyan2","Deepskyblue4","forestgreen","SpringGreen4","Slateblue4","orange","greenyellow","springgreen","deepskyblue","forestgreen","olivedrab","deepskyblue4","darkgoldenrod1","snow","linen","navajowhite2","chartreuse2","cadetblue4","gold","LightCyan2","gray60","gray32"]
#-----------------------------------------------------------
#------- Spielinhalte --- (Hintergrundfunktionen) ----------
#-----------------------------------------------------------
def LebenSchiff():
  global HP
  x = random.randint(1,100)
  if Geld <=0 and EigeneLadung == [0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
    tkinter.messagebox.showerror("- G A M E  O V E R -","Sie sind pleite.\n\nDas Spiel ist vorbei...")
    NeuesSpiel()
  if HP > 0:
    HP = HP - 1
  if x == 17 or x == 53:
    HP = HP - random.randint(20,60)
    tkinter.messagebox.showwarning("- SONNENSTURM -","Ihr Schiff hat Schaden genommen.\n")
  if HP <= 0:
    tkinter.messagebox.showerror("- G A M E  O V E R -","Sie wurden zerstört.\n\nDas Spiel ist vorbei...")
    NeuesSpiel()

  
def Piraten():
  global HP
  global EigeneLadung
  h = random.randint(1,40)
  if h == 17:
    HP = HP - random.randint(50,90)
    tkinter.messagebox.showinfo("  - P I R A T E N ! -  ", "Du wurdest von Piraten überfallen und hast Schaden genommen.\n Alle deine Waren wurden gestohlen!")
    EigeneLadung = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  if HP <= 0:
    tkinter.messagebox.showerror("- G A M E  O V E R -","Sie wurden zerstört.\n\nDas Spiel ist vorbei...")
    NeuesSpiel()


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
  LabelMenge.configure(bg=str(Farbe))
  LabelOrt.configure(bg=str(Farbe))
  LabelSchiffe.configure(bg=str(Farbe))
  
  Liste.delete("0","end")
  Liste.insert("end", Gewuerze[0] + "  " + str(aktKosten[0]))
  Liste.insert("end", Gewuerze[1] + "  " + str(aktKosten[1]))
  Liste.insert("end", Gewuerze[2] + "  " + str(aktKosten[2]))
  Liste.insert("end", Gewuerze[3] + "  " + str(aktKosten[3]))
  Liste.insert("end", Gewuerze[4] + "  " + str(aktKosten[4]))
  Liste.insert("end", Gewuerze[5] + "  " + str(aktKosten[5]))
  Liste.insert("end", Gewuerze[6] + "  " + str(aktKosten[6]))
  Liste.insert("end", Gewuerze[7] + "  " + str(aktKosten[7]))
  Liste.insert("end", Gewuerze[8] + "  " + str(aktKosten[8]))
  Liste.insert("end", Gewuerze[9] + "  " + str(aktKosten[9]))
  Liste.insert("end", Gewuerze[10] + "  " + str(aktKosten[10]))
  Liste.insert("end", Gewuerze[11] + "  " + str(aktKosten[11]))
  Liste.insert("end", Gewuerze[12] + "  " + str(aktKosten[12]))
  Liste.insert("end", Gewuerze[13] + "  " + str(aktKosten[13]))
  
  ListeLaderaum.delete("0","end")
  ListeLaderaum.insert("end", str(EigeneLadung[0]) + " Einheiten: " + str(Gewuerze[0])) 
  ListeLaderaum.insert("end", str(EigeneLadung[1]) + " Einheiten: " + str(Gewuerze[1]))
  ListeLaderaum.insert("end", str(EigeneLadung[2]) + " Einheiten: " + str(Gewuerze[2]))                     
  ListeLaderaum.insert("end", str(EigeneLadung[3]) + " Einheiten: " + str(Gewuerze[3]))
  ListeLaderaum.insert("end", str(EigeneLadung[4]) + " Einheiten: " + str(Gewuerze[4]))
  ListeLaderaum.insert("end", str(EigeneLadung[5]) + " Einheiten: " + str(Gewuerze[5]))
  ListeLaderaum.insert("end", str(EigeneLadung[6]) + " Einheiten: " + str(Gewuerze[6]))
  ListeLaderaum.insert("end", str(EigeneLadung[7]) + " Einheiten: " + str(Gewuerze[7]))
  ListeLaderaum.insert("end", str(EigeneLadung[8]) + " Einheiten: " + str(Gewuerze[8]))
  ListeLaderaum.insert("end", str(EigeneLadung[9]) + " Einheiten: " + str(Gewuerze[9]))
  ListeLaderaum.insert("end", str(EigeneLadung[10]) + " Einheiten: " + str(Gewuerze[10]))
  ListeLaderaum.insert("end", str(EigeneLadung[11]) + " Einheiten: " + str(Gewuerze[11]))
  ListeLaderaum.insert("end", str(EigeneLadung[12]) + " Einheiten: " + str(Gewuerze[12]))
  ListeLaderaum.insert("end", str(EigeneLadung[13]) + " Einheiten: " + str(Gewuerze[13]))
  ListeLaderaum.insert("end", "-------")
  ListeLaderaum.insert("end", "Credits: " + str(Geld))
  ListeLaderaum.insert("end", "Platz im Laderaum: " + str(Laderaum))
  ListeLaderaum.insert("end", "HP: " + str(HP))

  ListeSchiffe.delete("0","end")
  ListeSchiffe.insert("end", str(SchiffeListe[0]) + " - " + "Laderaum: " + str(LaderaumSchiffe[0]) + " - " + " HP: " + str(hpschiffe[0]) + " - " + "Preis: " + str(schiffpreis[0]))
  ListeSchiffe.insert("end", str(SchiffeListe[1]) + " - " + "Laderaum: " + str(LaderaumSchiffe[1]) + " - " + " HP: " + str(hpschiffe[1]) + " - " + "Preis: " + str(schiffpreis[1]))
  ListeSchiffe.insert("end", str(SchiffeListe[2]) + " - " + "Laderaum: " + str(LaderaumSchiffe[2]) + " - " + " HP: " + str(hpschiffe[2]) + " - " + "Preis: " + str(schiffpreis[2]))
  ListeSchiffe.insert("end", str(SchiffeListe[3]) + " - " + "Laderaum: " + str(LaderaumSchiffe[3]) + " - " + " HP: " + str(hpschiffe[3]) + " - " + "Preis: " + str(schiffpreis[3]))
  ListeSchiffe.insert("end", str(SchiffeListe[4]) + " - " + "Laderaum: " + str(LaderaumSchiffe[4]) + " - " + " HP: " + str(hpschiffe[4]) + " - " + "Preis: " + str(schiffpreis[4]))
  ListeSchiffe.insert("end", str(SchiffeListe[5]) + " - " + "Laderaum: " + str(LaderaumSchiffe[5]) + " - " + " HP: " + str(hpschiffe[5]) + " - " + "Preis: " + str(schiffpreis[5]))
  ListeSchiffe.insert("end", str(SchiffeListe[6]) + " - " + "Laderaum: " + str(LaderaumSchiffe[6]) + " - " + " HP: " + str(hpschiffe[6]) + " - " + "Preis: " + str(schiffpreis[6]))
  ListeSchiffe.insert("end", str(SchiffeListe[7]) + " - " + "Laderaum: " + str(LaderaumSchiffe[7]) + " - " + " HP: " + str(hpschiffe[7]) + " - " + "Preis: " + str(schiffpreis[7]))
  ListeSchiffe.insert("end", str(SchiffeListe[8]) + " - " + "Laderaum: " + str(LaderaumSchiffe[8]) + " - " + " HP: " + str(hpschiffe[8]) + " - " + "Preis: " + str(schiffpreis[8]))
  ListeSchiffe.insert("end", str(SchiffeListe[9]) + " - " + "Laderaum: " + str(LaderaumSchiffe[9]) + " - " + " HP: " + str(hpschiffe[9]) + " - " + "Preis: " + str(schiffpreis[9]))
  ListeSchiffe.insert("end", str(SchiffeListe[10]) + " - " + "Laderaum: " + str(LaderaumSchiffe[10]) + " - " + " HP: " + str(hpschiffe[10]) + " - " + "Preis: " + str(schiffpreis[10]))
  ListeSchiffe.insert("end", str(SchiffeListe[11]) + " - " + "Laderaum: " + str(LaderaumSchiffe[11]) + " - " + " HP: " + str(hpschiffe[11]) + " - " + "Preis: " + str(schiffpreis[11]))
  ListeSchiffe.insert("end", str(SchiffeListe[12]) + " - " + "Laderaum: " + str(LaderaumSchiffe[12]) + " - " + " HP: " + str(hpschiffe[12]) + " - " + "Preis: " + str(schiffpreis[12]))
  ListeSchiffe.insert("end", str(SchiffeListe[13]) + " - " + "Laderaum: " + str(LaderaumSchiffe[13]) + " - " + " HP: " + str(hpschiffe[13]) + " - " + "Preis: " + str(schiffpreis[13]))
  ListeSchiffe.insert("end", str(SchiffeListe[14]) + " - " + "Laderaum: " + str(LaderaumSchiffe[14]) + " - " + " HP: " + str(hpschiffe[14]) + " - " + "Preis: " + str(schiffpreis[14]))

  
  ListeStaedte.delete("0","end")
  ListeStaedte.insert("end", "Alderaan")
  ListeStaedte.insert("end", "Tatooine")
  ListeStaedte.insert("end", "Naboo")
  ListeStaedte.insert("end", "Kamino")
  ListeStaedte.insert("end", "Kashyyyk")
  ListeStaedte.insert("end", "Yavin IV")
  ListeStaedte.insert("end", "Ahch-to")
  ListeStaedte.insert("end", "Bespin")
  ListeStaedte.insert("end", "Carida")
  ListeStaedte.insert("end", "Cato Neimoidia")
  ListeStaedte.insert("end", "Corellia")
  ListeStaedte.insert("end", "Dagobah")
  ListeStaedte.insert("end", "Dantooine")
  ListeStaedte.insert("end", "Eadu")
  ListeStaedte.insert("end", "Geonosis")
  ListeStaedte.insert("end", "Hoth")
  ListeStaedte.insert("end", "Ilum")
  ListeStaedte.insert("end", "Jakku")
  ListeStaedte.insert("end", "Kuat")
  ListeStaedte.insert("end", "Mon Calamari")
  ListeStaedte.insert("end", "Mustafar")
  ListeStaedte.insert("end", "Scarif")
  ListeStaedte.insert("end", "Sullust")
  ListeStaedte.insert("end", "Todesstern")

  LabelOrt.config(text ="aktueller Ort: " + str(Ort))
  


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
  global FarbePlanet
  FarbePlanet = ["green2","navajowhite2","LightCyan2","Deepskyblue4","forestgreen","SpringGreen4","Slateblue4","orange","greenyellow","springgreen","deepskyblue","forestgreen","olivedrab","deepskyblue4","darkgoldenrod1","snow","linen","navajowhite2","chartreuse2","cadetblue4","gold","LightCyan2","gray60","gray32"]
  aktKosten = [30, 60, 300 , 150 ,800,500,60,50,80,30,90,300,20,40]
  EigeneLadung = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  Geld = 1000
  Laderaum = 100
  DisplayAktualisieren()
  Ort = "Tatooine"
  Farbe = "navajowhite2"
  HP = 1
  SchiffeListe = ["A-Wing", "X-Wing", "BTL-A4 Y-Wing", "Slave I", "kleiner SternenjÃ¤ger", "AR-170", "P-38","T-2c Theta-Klasse Transporter", "Tantive IV", "Millenium Falke", "YT-1200", "TIE-X1", "T-4a Lambda-Klasse Transporter", "U-Wing", "SternenzerstÃ¶rer"]
  LaderaumSchiffe =[100,120,150,300,150,180,200,500,1200,555,400,200,600,400,100000000]
  schiffpreis=[10000,20000,50000,100000,50000,60000,50000,110000,500000,200000,220000,30000,150000,100000,100000000]
  hpschiffe=[150,150,200,500,200,250,250,400,1000,1500,900,300,500,400,100000000]
  Info = ["Zurzeit keine Infos"]
  DisplayAktualisieren()

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
  for i in range (14):
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
  global MaxHP
  global HP
  Nummer = int(ListeSchiffe.curselection()[0])
  if (Geld >= schiffpreis[Nummer]):
      Laderaum = int(LaderaumSchiffe[Nummer])
      MaxHP = int(hpschiffe[Nummer])
      HP = MaxHP
      Geld = Geld - int(schiffpreis[Nummer])
      EigeneLadung = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
Fenster.title("SpiceWars: Star Wars Edition")
Fenster.configure(bg=str(Farbe))


#---------------------------------------------------------------
#--------------- Label -----------------------------------------
#---------------------------------------------------------------


LabelMenge = tkinter.Label(Fenster, text = 'Menge: ')
LabelMenge.grid (padx = 5, pady=5, row = 0, column = 2)

LabelOrt = tkinter.Label(Fenster, text = 'aktueller Ort: '+ str(Ort))
LabelOrt.grid (padx = 5, pady=5, row = 0, column = 8)

LabelSchiffe = tkinter.Label(Fenster, text = 'Schiffe: ')
LabelSchiffe.grid (padx = 5, pady=5, row = 0, column = 10)



#-------------------------------------------------------------
#------------ Listbox & Eingabe ------------------------------
#-------------------------------------------------------------


Liste = tkinter.Listbox (width=23, height = 24)
Liste.grid(padx = 5, pady = 5, row = 1, column = 1, columnspan = 1, rowspan=9)

ListeStaedte = tkinter.Listbox (width=15, height = 24)
ListeStaedte.grid(padx = 5, pady = 20, row = 1, column = 8, columnspan = 1, rowspan=9)

ListeLaderaum = tkinter.Listbox (width=30, height = 24)
ListeLaderaum.grid(padx = 5, pady = 5, row = 1, column = 5, columnspan = 2, rowspan=9)

ListeSchiffe = tkinter.Listbox (width=75, height = 24)
ListeSchiffe.grid(padx = 5, pady = 5, row = 1, column = 10, columnspan = 1, rowspan=9)

EingabeMenge = tkinter.Entry(Fenster, width = 4)
EingabeMenge.grid(padx = 5, pady = 5, row = 0, column = 3)


#-----------------------------------------------------------
#------------ Buttons --------------------------------------
#-----------------------------------------------------------


ButtonKaufen = tkinter.Button(Fenster,fg= "lightgreen",bg="gray17", text=' kaufen  >>> ', command = kaufen)
ButtonKaufen.grid(padx=5, pady = 5, row =2, column = 2, columnspan=2)

ButtonReperatur = tkinter.Button(Fenster,fg="snow",bg="gray17", text=' Reperatur ', command = Reparatur)
ButtonReperatur.grid(padx=5, pady = 5, row =7, column = 2, columnspan=2)

ButtonVerkaufen = tkinter.Button(Fenster,fg = "red",bg="gray17",text=' <<< verkaufen ', command = verkaufen)
ButtonVerkaufen.grid(padx=5, pady = 5, row =3, column = 2, columnspan=2)

ButtonBewegen = tkinter.Button(Fenster,fg="cyan",bg="gray17", text = ' Sprung in den Hyperraum ', command = Weitersegeln)
ButtonBewegen.grid(row=4, column=2, padx=5, pady=25, columnspan = 2)

ButtonSchiffe = tkinter.Button(Fenster,fg="snow",bg="gray17", text = ' Schiff kaufen ', command = Schiffe)
ButtonSchiffe.grid(row=5, column=2, padx=5, pady=25, columnspan = 2)

ButtonNeustart = tkinter.Button(Fenster,fg="snow",bg="gray17" ,text = ' neues Spiel ', command = NeuesSpiel)
ButtonNeustart.grid(row=0, column=1, padx=5, pady=10)

NeuesSpiel()
# ---------------------
Fenster.mainloop()

