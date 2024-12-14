
import pandas as pd

from abc import ABC,abstractmethod

class middle_fattore:



    def numero_totale_eventi_per_utente(self,df)->int:
        pass

    def occorrenze_evento(self,df)-> int:
        pass

    def prima_e_ultima_occorrenza(self,df):
        pass

    def numero_giorni_tra_primo_e_ultimo_evento(self,df)->int:
        pass

    def statistiche_numero_eventi_settimana(self,df)->tuple:
        pass




