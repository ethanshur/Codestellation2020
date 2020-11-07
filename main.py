import bs4 as bs;
from urllib.request import Request, urlopen;


def parse_plant(url):
    plant_parse = Request(url)
    plant_page = urlopen(plant_parse).read()
    plant_soup = bs.BeautifulSoup(plant_page, "lxml")
    mydivs = plant_soup.findAll("div", {"class": "infobox-subsection"})
    csv = ""
    csvkey = ""
    for i in mydivs:
        arr = (i.text.split("\n"))
        csvkey = csvkey + arr[1] + ","
        if arr[2] == "" or arr[2] == "?":
            csv = csv + "None Listed." + ","
        else:
            csv = csv + arr[2] + ","
    print(csvkey)
    print(csv)

def search(string):
    url = "https://practicalplants.org/w/index.php?title=Special%3ASearch&profile=all&search="
    string = string.replace(" ", "+")
    url = url + string + "&fulltext=Search"
    search_parse = Request(url)
    search_page = urlopen(search_parse).read()
    search_soup = bs.BeautifulSoup(search_page, "lxml")
    results = search_soup.findAll("div", {"class": "mw-search-result-heading"})
    results1 = search_soup.findAll("a", href = True)
    for i in results:
        curr = i.text
        response = input("Did you mean " + curr + "? (Y/N)")
        bool = False
        if (response.lower().startswith("y")):
            for j in results1:
                curr1 = curr.replace(" ", "_")
                curr1 = curr1[:-1]
                if curr1 in j["href"]:
                    print(j["href"])
                    temp = j["href"]
                    URL = "https://practicalplants.org" + temp
                    parse_plant(URL)
                    bool = True
                    break
        if bool:
            break
    if (not (bool)):
        print("No proper result found. Please try again.")

def main():
    search("ocimum basilicum")

main()