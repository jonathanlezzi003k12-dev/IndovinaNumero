from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    #fa da tramite dal modello a n max quindi chiede al modello
    #chi è nmax?

    def getNmax(self):
        return self._model.Nmax


    def getTmax(self):
        return self._model.Tmax

    #tutti i metodi che sono chiamati con i pulsanti devono avere un
    #parametro che chiamo e che è l'evento che ha generato la pressione
    #di quel pulsante

    def Reset(self,e):
        self._model.reset()#resetto lo stato del gioco lato modello
                          #e resetto anche l'interfaccia grafica
        self._view._txtT.value=self._model._T #dico quanti tentativi mi rimangono
        #inoltre devo pulire il mio listview
        #quindi scrivo:
        self._view._lvOut.controls.clear()
        #dico inoltre all'utente che può giocare
         #controls è una lista di controlli quindi dentro ci dobbiamo scrivere un controllo es ft.text
        self._view._lvOut.controls.append(ft.Text("inizia il gioco indovina a quale numero sto pensando"))
        self._view.update()






    def Play(self,e):
        #legge il tentativo del giocatore;
        # poi lo passa al modello
        # prende il valore return del modello
        # aggiorna l'interfaccia grafica
        tentativoStr= self._view._txtInterattivo.value
        try:
            tentativo= int(tentativoStr)#prendo l'imput dell'utente e provo a convertirlo in intero
            #se questo try fallisce mando l'exception
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore devi inserire un valore numerico"))
            self._view.update()
            return #questo perchè non ha più senso continuare


        res=self._model.play(tentativo)
        #ora ho un valore numerico come faccio a giocare?
        #lo devo chiedere al modello

        if res==0:
            """ho vinto!"""
            self._view._lvOut.controls.append(
                ft.Text(f"hai vinto il valore corretto era :{tentativo}" ,color="green")
            )
            self._view.update()
            return
        elif res==2:
            """non ho più vite"""
            self._view._lvOut.controls.append(ft.Text(f"hai perso il valore corretto era{self._model.segreto}"))

            self._view.update()
            return


        elif res==-1:
            """allora il segreto è più piccolo del tentativo"""
            self._view._lvOut.controls.append(ft.Text(f"ritenta il segreto è più piccolo di tentativo"))

            self._view.update()
            return
        else:
            """allora il segreto è più grande del tentativo"""
            self._view._lvOut.controls.append(ft.Text(f"ritenta il segreto è più grande di tentativo"))
            self._view.update()
            return
