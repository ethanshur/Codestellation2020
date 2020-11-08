import bs4 as bs
from urllib.request import Request, urlopen


def parse_plant(url):
    plant_parse = Request(url)
    plant_page = urlopen(plant_parse).read()
    plant_soup = bs.BeautifulSoup(plant_page, "lxml")
    mydivs = plant_soup.findAll("div", {"class": "infobox-subsection"})
    csv = "Binomial name,Genus,Family,Edible uses,Medicinal uses,Material uses & Functions,Botanic,Propagation," \
          "Cultivation,Environment,Cultivation,Edible uses,Material uses,Medicinal uses,Functions," \
          "Provides forage for,Provides shelter for,Hardiness Zone,Heat Zone,Water,Sun,Shade,Soil PH," \
          "Soil Texture,Soil Water Retention,Environmental Tolerances,Native Climate Zones,Adapted Climate Zones," \
          "Native Geographical Range,Native Environment,Ecosystem Niche,Root Zone Tendancy," \
          "Deciduous or Evergreen,Herbaceous or Woody,Life Cycle,Growth Rate,Mature Size," \
          "Fertility,Pollinators,Flower Colour,Flower Type,\n"
    for i in mydivs:
        print(i.text)
        arr = (i.text.split("\n"))
        for j in range(2, len(arr)):
            if arr[j] == "" or arr[j] == "?":
                csv = csv + ""
            else:
                csv = csv + arr[j].replace(",", ";")
        csv = csv + ","
    print(csv)
    return csv[:-1]

def search(string):
    url = "https://practicalplants.org/w/index.php?title=Special%3ASearch&profile=all&search="
    string = string.replace(" ", "+")
    url = url + string + "&fulltext=Search"
    search_parse = Request(url)
    search_page = urlopen(search_parse).read()
    search_soup = bs.BeautifulSoup(search_page, "lxml")
    results = search_soup.findAll("div", {"class": "mw-search-result-heading"})
    results1 = []
    for j in range(len(results)):
        if results[j] != None:
            (results1.append(results[j].text.replace(" ", "_")[0:-1]))
    return results1


def main():
    bool = True
    num = 0
    output = "ID,Binomial name,Genus,Family,Edible uses,Medicinal uses,Material uses & Functions,Botanic," \
             "Propagation,Cultivation,Environment,Cultivation,Edible uses,Material uses,Medicinal uses,Functions," \
             "Provides forage for,Provides shelter for,Hardiness Zone,Heat Zone,Water,Sun,Shade,Soil PH," \
             "Soil Texture,Soil Water Retention,Environmental Tolerances,Native Climate Zones,Adapted Climate Zones," \
             "Native Geographical Range,Native Environment,Ecosystem Niche,Root Zone Tendancy,Deciduous or Evergreen," \
             "Herbaceous or Woody,Life Cycle,Growth Rate,Mature Size,Fertility,Pollinators,Flower Colour,Flower Type\n"
    while bool:
        num = num + 1
        plantsearch = input("What is the scientific name of the plant you are looking for?")
        output = output + str(num) + "," + search(plantsearch)
        print(output)
        repeat = input("Would you like to find another plant? (y/n)")
        if repeat.lower().startswith("n"):
            #text_file = open("codestellation2020output.txt", "w")
            #n = text_file.write(output)
            #text_file.close()
            return output
        output = output + "\n"
