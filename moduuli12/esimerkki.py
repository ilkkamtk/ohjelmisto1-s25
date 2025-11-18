import requests

hakusana = input("Anna hakusana: ")

pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:
    vastaus = requests.get(pyyntö)

    if not vastaus.ok:
        raise Exception("jokin meni pieleen")

    sarjat = vastaus.json()

    if len(sarjat) == 0:
        raise Exception("Hakusanalla ei tuloksia")

    for sarja in sarjat:
        print(sarja["show"]["name"])

except requests.exceptions.RequestException as e:
    print("Haussa tapahtui virhe")
except Exception as e:
    print(e)
