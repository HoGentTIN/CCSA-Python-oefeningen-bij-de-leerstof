import heapq

class AchtPuzzel:

    BUREN = {0 : {("R", 1),("O", 3)},   1 : {("L", 0),("R", 2),("O", 4)},   2 : {("L",1),("O",5)},
             3 : {("B",0),("R",4),("O",6)}, 4 : {("B",1),("L", 3),("R", 5),("O",7)}, 5 : {("B",2),("L", 4),("O",8)},
             6 : {("B",3),("R",7)},   7 : {("B",4),("L",6),("R",8)},   8 : {("B",5),("L",7)} 
            }

    def __init__(self, bord="123456780"):
        self.bord = bord


    def __str__(self):
        return self.bord[:3] +  "\n" + self.bord[3:6] + "\n" + self.bord[6:]

    def __repr__(self):       
        return f"AchtPuzzel(bord='{self.bord}')"
        
    def __eq__(self, other):
        if isinstance(other, AchtPuzzel):
            return self.bord == other.bord
        return False

    def __hash__(self):
        return hash(self.bord)
    
    def opvolgers(self):
        index_0 = self.bord.find('0')
        succ = set()
        for (actie, index) in AchtPuzzel.BUREN[index_0]:
            i1 = min(index_0, index)
            i2 = max(index_0, index)

            # Kan misschien wel wat eleganter
            new_puzzle = self.bord[:i1] + self.bord[i2] + self.bord[i1+1:i2] + self.bord[i1] + self.bord[i2+1:]
            succ.add((actie, AchtPuzzel(new_puzzle)))

        return succ

    def doe_actie(self, actie):       
        for (a, toestand) in self.opvolgers():
            if a == actie:
                return toestand
        
        return self
    
    ## Lege plaats mag je niet meerekenen
    def aantal_verkeerd(self, other):
        aantal = 0
        for i, c in enumerate(self.bord):
            if c != '0' and c != other.bord[i]:
                aantal += 1
        return aantal

    def manhattan_heuristiek(self, other):
        afstand = 0
        for i, c in enumerate(self.bord):
            if c != '0':
                i2 = other.bord.find(c)
                afstand += AchtPuzzel._manhattan(i, i2)

        return afstand
    
    @staticmethod
    def _manhattan(i1, i2):
        x1, y1 = i1 // 3, i1 % 3
        x2, y2 = i2 // 3, i2 % 3
        return abs(x1-x2) + abs(y1-y2)


class Plan:

    def __init__(self, toestand, voorganger=None, actie=None, kost=0, h_waarde=float("inf")):
        self.toestand = toestand
        self.voorganger = voorganger
        self.actie = actie
        self.kost = kost
        self.h_waarde = h_waarde

    ## Vergelijk op basis van cost + heuristic
    def __lt__(self, other):
        return self.kost + self.h_waarde < other.kost + other.h_waarde

    def geef_actie_sequentie(self):
        acties = []
        huidig = self
        while huidig.actie:
            acties.append(huidig.actie)
            huidig = huidig.voorganger
    
        return acties[::-1]

def a_ster_zoeken(start_toestand, is_doel, heuristiek, kost= lambda s,a : 1):
    closed = set()
    open_list = []
    heapq.heappush(open_list, Plan(start_toestand))
    while len(open_list) > 0:        
        current = heapq.heappop(open_list)
        if is_doel(current.toestand):            
            return current.geef_actie_sequentie(), current.kost
        if current.toestand not in closed:
            closed.add(current.toestand)
            for (action, succ) in sorted(current.toestand.opvolgers()):
                new_plan = Plan(toestand=succ, voorganger=current, 
                                actie=action, kost=current.kost + kost(current.toestand, action),   
                                h_waarde=heuristiek(succ))
                heapq.heappush(open_list, new_plan) 
    
    return None    