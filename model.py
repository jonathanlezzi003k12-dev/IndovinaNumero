import random

class Model(object):
    def __init__(self):
        self._Nmax=100
        self._Tmax= 6
        self._T= self._Tmax#dobbiamo ricordarci di aggiornarlo
        self._segreto=random.randint(0,self._Nmax) #scelta randomica che faremo più in la


    #questo metodo serve per resettare lo stato del gioco
    #imposta il segreto ad un valore randomico fra 0 e nmax

    def reset(self):
        #ripristino il mio numero segreto
        self._segreto=random.randint(0,self._Nmax)
        #ripristino il numero di tentativi
        self._T=self._Tmax

        #questo mi serve solo per testare la classe
        print (self._segreto)





    #questo metodo ci permette di giocare:
    #riceve come argomento un numero intero dal giocatore
    #e lo confronta con il segreto
    #restituisce -1 se il segreto è più piccolo del tentativo
    #0 se il tentativo è uguale al segreto
    #1 se il segreto è più grande del tentativo
    #2 se non ho più tentativi disponibili
    def play(self,tentativo):




        #questo mi serve per dire che ogni volta che provo
        #ad indovinare devo togliere una vita
        self._T-=1
        if tentativo==self._segreto:
            """ho vinto"""
            return 0
        #ho ancora vite per giocare?
        if self._T==0:
            """non ho più vite """
            return 2

        elif(tentativo>self._segreto):
            """il tentativo dell'utente è più grande del segreto"""
            return -1
        else:
            """il tentativo è più piccolo del segreto"""
            return 1


    #questo mi serve per la return di nmax per il controller
    #questo perchè è poco elegante passare dei dati con l'under score
    #perchè sono dati privati quindi creando una properti faccio
    #in modo che nMax sia attributo della classe così che io
    #lo possa passare tranquillamente

    @property
    def Nmax (self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax


    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto



#come faccio a testarlo?
if __name__=="__main__":
    m= Model()
    m.reset()
    print(m.play(50))
    print(m.play(20))
    print(m.play(30))
    print(m.play(40))
    print(m.play(50))
    print(m.play(30))
    print(m.play(40))
    print(m.play(50))
    #l'interfaccia grafica dovrà disabilitare la possibilità di giocare dopo che abbiamo finito
    #le vite


