def zoek_binair(zoekitem, rij):
    links = 0
    rechts = len(rij) - 1
    while links != rechts:
        print(f"{links}, {rechts}")
        midden = (links + rechts) // 2
        if rij[midden] < zoekitem:
            links = midden + 1
        else:
            rechts = midden
            
    if rij[links] == zoekitem:
        index = links
    else:
        index = -1
    
    # alternatief met tertaire operator:
    # index = links if rij[links] == zoekitem else -1
        
    return index 