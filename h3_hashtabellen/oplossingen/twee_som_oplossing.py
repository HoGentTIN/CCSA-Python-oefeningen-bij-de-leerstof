
def two_sum(getallen, doel):
    """ Zoekt twee getallen in de input die als som doel hebben 
    """
    for i,getal1 in enumerate(getallen):
        for j,getal2 in enumerate(getallen):
            if i!=j :
                if getal1 + getal2 == doel : 
                    return (min(i,j),max(i,j))
    return None

# alternatief met itertools.combinations --> altijd i != j
# import itertools
# for (i,getal1),(j,getal2) in itertools.combinations(enumerate(getallen),2):
#     if getal1 + getal2 == doel:
#         return (min(i,j),max(i,j))


def two_sum_hash(getallen,doel):
    indexVanGetal = {}
    for i,getal in enumerate(getallen):
        zoekGetal = doel-getal
        if (zoekGetal) in indexVanGetal:
            return (min(i,indexVanGetal[zoekGetal]),max(i,indexVanGetal[zoekGetal]))
        indexVanGetal[getal] = i 
    return None
if __name__ == "__main__":
    doel = 10
    getallen = [1, 4, 5, 7, 8, 9]
    print(two_sum(getallen,doel))

    print(two_sum_hash(getallen,doel))
    doel = 50
    getallen = [ 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,49]
    print(two_sum(getallen,doel))

    print(two_sum_hash(getallen,doel))
