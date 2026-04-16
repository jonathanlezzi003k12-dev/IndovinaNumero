import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)
        #la view e il modello non si devono palare in mezzo ci deve SEMPRE
        #essere il controller
        #quindi la classe view attraverso questo metoo CHEIDE  al c
        #controller chi è questo nmax attraverso il metodo getNmax
        self._txtNmax=ft.TextField(label ="Numero max",value=self._controller.getNmax(),disabled=True)
        self._txtTmax=ft.TextField(label="Numero tentativi massimo",value=self._controller.getTmax(),disabled=True)



        self._txtT=ft.TextField(label="Tentativi rimanenti",disabled=True)



        self._row1=ft.Row(controls=[self._txtNmax,self._txtTmax,self._txtT])



        #aggiungo questa riga alla pagina
        #self._page.add(self._row1)#add fa sia aggiunta degli oggettigrafici che l'update
        self._txtInterattivo=ft.TextField(label="valore",disabled=False)
        self._binReset=ft.ElevatedButton(text="Nuova Partita",on_click=self._controller.Reset)#dobbiamo passare il nome del metodo e non la chiamata del metodo quindi va senza tonde
        self.btnPlay=ft.ElevatedButton(text="indovina",on_click=self._controller.Play)


        self._row2=ft.Row(controls=[self._txtInterattivo,self._binReset,self.btnPlay])



        #contenitore di stringhe
        self._lvOut=ft.ListView(expand=True)#expand ugule true così possiamo scrollarlo




        self._page.add(self._row1,self._row2, self._lvOut)


        self._page.update()

    def setController(self,controller):
        self._controller = controller



    #questo metodo è un metodo d'appoggio che aggiorna l'interfaccia grafica
    def update(self):
        self._page.update()
