def zoek_binair(zoekItem, rij):
    links = 0
    rechts = len(rij) - 1
    while links != rechts:
        print(f"{links}, {rechts}")
        midden = (links + rechts) // 2
        if rij[midden] < zoekItem:
            links = midden + 1
        else:
            rechts = midden
            
    if rij[links] == zoekItem:
        index = links
    else:
        index = -1
        
    return index 