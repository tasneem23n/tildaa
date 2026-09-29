#testa binärsökning för kattis
#Skapa klass som representerar en låt
class Song:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn


# Läs in filen och skapa Song-objekt
songs = []
with open("unique_quarter.txt", encoding="latin1") as f:
    for line in f:
        parts = line.strip().split("<SEP>")
        songs.append(Song(*parts))

# Prova utskrift
print("låtnamn: " , songs[0].artistnamn,",",  "låttitel:" , songs[0].låttitel)



#sökning 
import timeit
import random 

# --- Läs in filen ---
def readfile(filename):
    songs = []
    with open(filename, encoding="latin1") as f:
        for line in f:
            parts = line.strip().split("<SEP>")
            songs.append(parts[2])  # artistnamn
    return songs


# --- Linjärsökning ---
def linsok(lista, key):
    for item in lista:
        if item == key:
            return item
    return None


# --- Binärsökning ---
def binsok(lista, key):
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == key:
            return lista[mid]
        elif lista[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return None


# --- Hashtabell ---
def hash_sok(hashtabell, key):
    return hashtabell.get(key, None)


# --- Huvudprogram ---
def main():
    filename = "unique_quarter.txt"
    storLista = readfile(filename)

    # Lista med olika storlekar
    storlekar = [250000, 500000, 1000000]

    for n in storlekar:
        lista = storLista[:n]
        testartist = random.choice(lista)
        sorterad_lista = sorted(lista)
        hashtabell = {artist: True for artist in lista}

        linjtid = timeit.timeit(lambda: linsok(lista, testartist), number=10)
        bintid = timeit.timeit(lambda: binsok(sorterad_lista, testartist), number=10)
        hashtid = timeit.timeit(lambda: hash_sok(hashtabell, testartist), number=10)

        print(f"\nn = {n}")
        print(f"Linjärsökning tog {round(linjtid, 4)} sekunder")
        print(f"Binärsökning tog {round(bintid, 4)} sekunder")
        print(f"Sökning i hashtabell tog {round(hashtid, 4)} sekunder")


if __name__ == "__main__":
    main()



#sortering 
import timeit
import random

#Exempeldata
def skapa_lista(n):
    return [random.randint(0, 1000000) for _ in range(n)]

#Långsam sorteringsmetod: Bubble Sort 
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Snabbare sorteringsmetod: Python's inbyggda sort (Timsort) 
def snabb_sort(lista):
    return sorted(lista)

#Tidtagning 
def main():
    for n in [1000, 10000, 100000, 1000000]:
        lista = skapa_lista(n)

        # Kopior för rättvis jämförelse
        lista1 = lista.copy()
        lista2 = lista.copy()

        print(f"\nAntal element: {n}")

        # Långsam sortering
        tid_bubble = timeit.timeit(lambda: bubble_sort(lista1), number=1)
        print(f"Långsam sortering (Bubble Sort): {round(tid_bubble, 4)} sekunder")

        # Snabb sortering
        tid_snabb = timeit.timeit(lambda: snabb_sort(lista2), number=1)
        print(f"Snabbare sortering (Timsort): {round(tid_snabb, 4)} sekunder")


if __name__ == "__main__":
    main()


