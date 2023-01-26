#Fukcja umożliwiająca przygotowanie plik.data na plik.csv
#----------------------------------------------------------

def load_data(plik):
    with open(plik, 'r') as in_file, open('zmodyfikowany.csv', 'w') as out_file:
        for line in in_file:
            out_file.write(line.replace('\t', ','))

#Funkcja która już pracuje na plik.csv i wczytuje dane całe lub podzielone(start,stop):
#-----------------------------------------------------

def load_file(path, header=False,start=None,stop=None, save=False, bundle='new.csv' ):    
    
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
        if save is True:
            with open(bundle, 'a+') as out_file:
                for i,row in enumerate(csvreader):
                    if(start is None or int(start)<= i) and(stop is None or i < int(stop)):
                        print(row,file=out_file)
        else:
            for i,row in enumerate(csvreader):
                    if(start is None or int(start)<= i) and(stop is None or i < int(stop)):
                        print(row)
            csvfile.close()  

#Funkcja która dzieli dataset na część treningową, testową i walidacyjną
#-----------------------------------------------------------------------
def split_dataset(dataset, train_percent, val_percent, test_percent, save=False, bundle='new.csv'):
    def load_csv(path):
        import csv 
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
        
    dataset = load_csv(path)
    # obliczamy sumę procentów
    total_percent = train_percent + val_percent + test_percent
    
    # sprawdzamy, czy suma procentów jest równa 100
    if total_percent != 100:
        raise ValueError("Procenty nie dają sumy 100")
    
    # obliczamy liczbę próbek w każdym podzbiorze
    train_size = int(len(dataset) * train_percent / 100)
    val_size = int(len(dataset) * val_percent / 100)
    test_size = int(len(dataset) * test_percent / 100)
    
    # dzielimy zbiór na podzbiory
    train_set = dataset[:train_size]
    val_set = dataset[train_size:train_size+val_size]
    test_set = dataset[train_size+val_size:]
    
    # zwracamy podzbiory jako tuple
    print('\nZbiór treningowy:')
    print(train_size)
    print('Zbiór walidacyjny:')
    print(val_size)
    print('Zbiór testowy:')
    print(test_size)
    
    if save is True:
        with open(bundle, 'a+') as out_file:
            print(train_set, file=out_file)
            print(val_set, file=out_file)
            print(test_set, file=out_file)
    
            return train_set, val_set, test_set
 #Funkcja zliczająca klasy i liczbę jej wystąpień:
 # ---------------------------------------------- 
def class_sum(path, save=False, bundle='new.csv'):
    import csv
    from collections import defaultdict
    class_counts = defaultdict(int)

    print('\n(Klasy, Ich_liczebność)\n')

    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in filter(lambda row: row, reader):
            class_counts[row[-1]] += 1

    for cls, count in class_counts.items():
        if save is True:
            with open(bundle, 'a+') as out_file:
                print((cls,count), file=out_file)
        else: 
            print((cls, count))
        

# Funkcja wypisuje dane dla podanej wartości klasy decyzyjnej 
#  wypisuje wiersze z zadaną wartością klasy decyzyjnej
#-----------------------------------------------------------
def class_name(path='zmodyfikowany.csv', name='Iris-virginica', save=False, bundle='new.csv'):
    import csv
    class_value = name
    print(f'\n{name}:\n')
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in filter(lambda x: x, reader):
            if row[-1] == class_value:
                if save is True:
                    with open(bundle, 'a+') as out_file:
                        print(row, file=out_file)
                else: 
                    print(row)
          
#-----------------Przykad użycia---------------------------------------------------
#----------------------------------------------------------------------------------

# 1. ładujemy plik do dalszej obróbki
plik = 'iris.data'
path = 'zmodyfikowany.csv'
load_data(plik) 
# 2.  ładujemy dane z etykietami lub bez
load_file(path, header=False, start=0, stop=10)
# 3. dzielimy dataset na cześć treningową i testową:
split_dataset(path,80,0,20)  
# 4. zliczamy klasy i liczbę wystąpień :
class_sum(path)
# 5. wypisuje wiersze z podaną nazwą wierszy:
class_name(name='Iris-versicolor')
# 6. (można również wyniki zapisywać do pliku podając parametry funkcji:save=True, bundle='name.csv')