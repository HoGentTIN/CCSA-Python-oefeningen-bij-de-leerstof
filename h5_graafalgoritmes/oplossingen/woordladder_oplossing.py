from collections import deque
import itertools

def precies_een_verschillend(w1, w2):
    """ Controleert of twee strings even lang zijn en op precies 1 plaats verschillen.
    """
    if len(w1) != len(w2):
        return False
    
    num_verschillend = 0
    for (c1,c2) in zip(w1,w2):
        if c1 != c2:
            num_verschillend += 1
    
    return num_verschillend == 1


def maak_graaf(woordenlijst):
    """ Maakt een graaf aan op basis van een lijst van woorden.

        woordenlijst: lijst van string
        returns: een dictionary met als sleutels alle woorden in de woordenlijst en als waarde
        een verzameling van alle woorden die op precies één plaats verschillen
    """
    graaf = {w : set() for w in woordenlijst}     
    for (w1, w2) in itertools.combinations(woordenlijst, 2):
        if precies_een_verschillend(w1, w2):                           
            graaf[w1].add(w2)
            graaf[w2].add(w1)
    
    return graaf


def kortste_pad(graaf, start):
    """ Bepaal kortste pad van <code>start</code> naar alle knopen van de graaf.

    graaf: een dictionary met als sleutels de knopen van de graaf en als waarden de verzamelingen 
           van de buren
    start: een knoop van de graaf

    returns: een dictionary <code>pred</code> waarbij <code>pred[w]</code> de voorganger geeft
    van <code>w</code> op het (gevonden) kortste pad van <code>start</code> naar <code>w</code>. 
    Bijzondere gevallen: <code>pred[start] = start</code>. Wanneer er geen pad is naar <code>w</code>
    dan is <code>pred[w]</code> gelijk aan None.

    AssertionError wanneer <code>start</code> geen knoop is van de graaf.

    """
    assert start in graaf.keys(), "Ongeldig startwoord"   

    pred = { w :  None for w in graaf.keys()}

    q = deque()
    q.append(start)
    pred[start] = start
    while len(q) > 0:
        v = q.popleft()
        for w in sorted(graaf[v]): ## Steeds gesorteerd doorlopen voor uniciteit oplossing            
            if pred[w] is None:
                pred[w] = v
                q.append(w)

    return pred

def geef_pad(pred, stop):
    """ Berekent een (expliciet) pad op basis een dictionary <code>pred</code>.

        pred: een dictionary met voorgangers. Het startwoord kan je herkennen aan het feit
        dat <code>pred[start]=start</code>.
        stop: het doelwoord van het pad

        returns: - None als er geen pad is van startwoord naar stop.
                 - een lijst van knopen beginnend bij het startwoord en eindigend in stop, zoals aangegeven door 
                   de dictionary `pred`

    """
    if pred[stop] is None:
        return None
    pad = []
    current = stop
    while pred[current] != current:
        pad.append(current)
        current = pred[current]
    pad.append(current)
    return pad[::-1]