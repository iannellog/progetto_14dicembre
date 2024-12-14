# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:32:09 2024

@author: ianne
"""

import unittest

from pandas import DataFrame
from middle_fattore import middle_fattore
from numpy import var


class Test_Extractor(unittest.TestCase):
    
    __df: DataFrame = None
    
    def setUp(self):
        log_list = {
            "data"        : ["4/11/2024 18:42"],
            "utente"          : [1],
            "contesto" : [],
            "componente"      : [],
            "evento"          : ["Visualizzato report log"],
            "descrizione"     : [],
            "origine"         : [],
            "indirizzo IP"    : []
            }
        # riempie le liste non inizializzate
        n_logs = len(log_list["data"])
        for k in log_list:
            if len(log_list[k]) != n_logs:
                log_list[k] = [None]*n_logs
        # crea il DataFrame per i test
        self.__df = DataFrame(log_list)
        
    def test_CreaExtractor(self):
        extractor = middle_fattore()
        self.assertIsInstance(extractor, middle_fattore)
        
    def test_CheckWeekFeatures(self):
        # populate the dataframe
        self.__df.loc[len(self.__df)] = \
            ["12/11/2024 18:42", 1, None, None, "event1", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["5/11/2024 18:42", 1, None, None, "event2", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["13/11/2024 18:42", 1, None, None, "event1", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["14/11/2024 18:42", 1, None, None, "event2", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["20/11/2024 18:42", 1, None, None, "event3", None, None, None]
        extractor = middle_fattore()
        mean, variance = extractor.computeWeekFeatures(self-__df, 1)  # compute week features of user 1
        self.assertEqual(mean, 6/3)
        self.assertEqual(variance, var([2, 3, 1]))

    def test_CheckNumeroEventi(self):
        # populate the dataframe
        self.__df.loc[len(self.__df)] = \
            ["12/11/2024 18:42", 1, None, None, "event1", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["5/11/2024 18:42", 1, None, None, "event2", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["13/11/2024 18:42", 1, None, None, "event1", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["14/11/2024 18:42", 1, None, None, "event2", None, None, None]
        self.__df.loc[len(self.__df)] = \
            ["20/11/2024 18:42", 1, None, None, "event3", None, None, None]
        extractor = middle_fattore()
        self.assertEqual(extractor.numero_totale_eventi_per_utente(self.__df, 1), 6)
        
if __name__ == "__main__":
    unittest.main()
        