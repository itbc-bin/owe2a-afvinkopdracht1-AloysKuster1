# Naam: Aloys Kuster
# Datum: 3 november
# Versie: 1.0

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestand = "Alpaca.fna"# Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    
        
    
    
    
    bestand = input("a")     

    if !(check(bestand)):
        print("err")
        return
    
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """

    try:
        headers, seqs = lees_inhoud(bestand) 
            
        zoekwoord = input("Geef een zoekwoord op: ")

        for woord in range(len(headers)):
            if zoekwoord in headers[woord]:
                is_dna(seqs[woord])
                knipt(seqs[woord])
            if zoekwoord not in headers:
                print('Zoekwoord staat niet in header')
                
    except IOError:
        print('Error het bestand bestaat niet')
    # schrijf hier de rest van de code nodig om de aanroepen te doen

def check(bestand):

    fasta = (".fasta",".fa","fna",".txt")
    checkje = False
    for fa in fasta:
        if bestand[-len(fa):] == fa:
            checkje = True
            
    return checkje
    
def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    seq = ''
    for line in bestand:
        line=line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
        seqs.append(seq)
        #bestand.close()
    
    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
     
    return headers, seqs

    
def is_dna(seqs):
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """

    check = 'true'

    bestand = open('Alpaca.fna', 'r')

    for nucl in seqs:
        if nucl == 'G' or 'A' or 'T' or 'C':
            check = 'true'

        
        if nucl != 'G' or 'A' or 'T' or 'C' or '/n' or ' ':
            check = 'false'
            print('Dit is geen DNA')

        else:
            print("ERROR: er klopt iets niet bij is_DNA")
            
        if check == 'true':
            print('Het is een DNA sequentie.')
        
        
    
 
def knipt(seq):
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken
    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
    enzymen = open('enzymen.txt', 'r')
    enzymenlijst = []

    for reg in enzymen:
        reg = reg.strip('/n')
        reg = reg.replace('^', '')
        enzymenlijst.append(reg)
        enzym = reg.split()[0]
        sequentie = reg.split()[1]

    for i in range(len(seqs)):
        stuk = seqs[i:i+len(sequentie)]
        if stuk == sequentie:
            print('Match met: ', enzym, 'Op plek: ', i)
    
main()
