#Fukcja umożliwiająca przygotowanie plik.data na plik.csv
#----------------------------------------------------------

def load_data(plik):
    with open(plik, 'r') as in_file, open('zmodyfikowany.csv', 'w') as out_file:
        for line in in_file:
            out_file.write(line.replace('\t', ','))

#Funkcja która już pracuje na plik.csv i wczytuje dane całe lub podzielone(start,stop):
#-----------------------------------------------------

def load_file(path, header=False,start=None,stop=None ):    
    
    import csv
    path = path
    
    with open (path,'r') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')      

#wczytanie nagłówków jeśli header=True:
        if header == True:
                naglowki = next(csvreader)
                print('DATASET LABELS:')
                print(naglowki)           
        else:
            print('\nDATASET LABELS = EMPTY \n')    

#wczytanie datasetu całego lub o określonej liczbie wierszy(start=(),stop=()):
        print('DATASET:')
        start = start
        stop = stop
        for i,row in enumerate(csvreader):
            if(start is None or int(start)<= i) and(stop is None or i < int(stop)):
                print(row)
        csvfile.close()  
        
#-----------------Przykad użycia---------------------------------------------------
#----------------------------------------------------------------------------------

# 1. ładujemy plik do dalszej obróbki
plik = 'iris.data'
path = 'zmodyfikowany.csv'
load_data(plik) 
# 2.  ładujemy dane z etykietami lub bez
load_file(path, header=False, start=0, stop=10)