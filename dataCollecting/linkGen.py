def linkGen():
    url = "https://en.wikipedia.org/wiki/Billboard_year-end_top_50_singles_of_1956"
    specifier = "Billboard_year-end_top_50_singles_of_1956"
    spec = specifier.split("_")


    yearString = spec[len(spec) - 1]
    yr = int(yearString)

    #generate years 
    years = []
    for i in range(1956, 2021): 
        years.append(i)
    yrString = list(map(str, years))

    links = []
    for x in range(len(yrString)):
        newYear = yrString[x]
        spec[len(spec) - 1] = newYear
        specJoin = "_".join(spec)

        linkJoin = "https://en.wikipedia.org/wiki/" + specJoin
        links.append(linkJoin)
    
    return links

print(linkGen())