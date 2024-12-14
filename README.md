# Estrazione di feature da una lista di log

Scrivere un programma Python che legge una lista di log anonimizzati da un file. 
Il file in ingresso può essere in diversi formati (per es. JSON, csv, Excel, testo con 
campi di lunghezza fissa, ecc.).

Ciascun elemento della lista di log è costituito dalle seguenti otto informazioni:

- Data/Ora
- Identificativo unico dell’utente
- Contesto dell’evento
- Componente
- Evento
- Descrizione
- Origine 
- Indirizzo IP

L'obiettivo è quello di calcolare per ogni utente un vettore di feature e salvare i dati in un file.
Il file di uscita può essere in diversi formati (per es. JSON, csv, Excel, testo con campi di lunghezza fissa, ecc.).

possibili feature (per ciascun utente)

numero totale di eventi
media e varianza del numero eventi in una settimana (da lunedì a domenica)
quante volte si è verificato ciascun evento 
data primo evento
data ultimo evento
numero di giorni tra il primo e l'ultimo evento
altre features a piacere
