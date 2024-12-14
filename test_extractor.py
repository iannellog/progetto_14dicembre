# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:32:09 2024

@author: ianne
"""

import unittest

from pandas import DataFrame
from extractor import Extractor
from numpy import var


class Test_Extractor(unittest.TestCase):
    
    __df: DataFrame = None
    
    def setUp(self):
        log_list = {
            "Data-Ora"        : ["4/11/2024 18:42"],
            "Utente"          : [1],
            "Contesto-evento" : [],
            "Componente"      : [],
            "Evento"          : ["Visualizzato report log"],
            "Descrizione"     : [],
            "Origine"         : [], 
            "Indirizzo-IP"    : []             
            }
        # riempie le liste non inizializzate
        n_logs = len(log_list["Data-Ora"])
        for k in log_list:
            if len(log_list[k]) != n_logs:
                log_list[k] = [None]*n_logs
        # crea il DataFrame per i test
        self.__df = DataFrame(log_list)
        
    def test_CreaExtractor(self):
        extractor = Extractor(self.__df)
        self.assertIsInstance(extractor, Extractor)
        
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
        extractor = Extractor(self.__df)
        mean, variance = extractor.computeWeekFeatures(1)  # compute week features of user 1
        self.assertEqual(mean, 6/3)
        self.assertEqual(variance, var([2, 3, 1]))

        
if __name__ == "__main__":
    unittest.main()
        