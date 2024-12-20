from abc import ABC, abstractmethod
import pandas as pd


class SaveStrategy(ABC): #Definisco la class strategy che permette di salvare il dataframe in differenti formati

    @abstractmethod
    def save(self, df: pd.DataFrame, filename: str):
        pass

class CsvSaveStrategy (SaveStrategy): # implementa una startegia di salvataggio dei dati in CSV utilizzando il Pattern strategy
    def save (self, df:pd.DataFrame, filename:str):
        df.to_csv(filename, index = False)#non viene incluso l'indice del Data Frame
        print (f"DataFrame salvato in formatoc CSV: {filename}")

class JsonSaveStrategy (SaveStrategy):
    def save (self, df:pd.DataFrame, filename:str):
        df.to_json(filename, index = False)
        print (f"DataFrame salvato in formatoc Json: {filename}")

class ExcelSaveStrategy (SaveStrategy):
    def save (self, df:pd.DataFrame, filename:str):
        df.to_excel(filename, index = False)
        print (f"DataFrame salvato in formatoc Excel: {filename}")


if __name__ == "__main__":

    filename = './OutPut/'

    #leggiamo un esempio di file excel e lo trasformo in dataframe
    df = pd.read_excel('./OutPut/output_test.xlsx')

    #si verifica con il print ch eeffettivamente recupero i dati corretti
    #print(df.head())

    # Creiamo un'istanza della strategia di salvataggio CSV
    csv_strategy = CsvSaveStrategy()
    csv_strategy.save(df, filename + "output.csv")



    # Creiamo un'istanza della strategia di salvataggio Json
    json_strategy = JsonSaveStrategy()
    json_strategy.save(df, filename + "output.json")


    # Creiamo un'istanza della strategia di salvataggio Excel
    excel_strategy = ExcelSaveStrategy()
    excel_strategy.save(df, filename + "output.xlsx")
