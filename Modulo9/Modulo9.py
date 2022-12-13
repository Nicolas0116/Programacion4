import requests

i = 1
c = 200
lista = []
l_wookies = []
while c < 404:
    response = requests.get("https://swapi.dev/api/films/" + str(i) + "/")
    data = response.json()
    x = response.status_code
    if x == 200:
        planetas = data['planets']
        for planeta in planetas:
            p = requests.get(planeta)
            d = p.json()
            if str(d["climate"]) == 'arid':
                lista.append(str(data["title"]))
            break
    if i == 6:
        personajes = data['characters']
        for personaje in personajes:
            p = requests.get(personaje)
            d = p.json()
            especies = d["species"]
            for especie in especies:
                p2 = requests.get(especie)
                d2 = p2.json()
                if str(d2["name"]) == "Wookie":
                    l_wookies.append(str(d["name"]))

    if x == 200:
        naves = data['starships']
        lt = 0.0
        nave_name = ""
        url = ""
        for nave in naves:
            p3 = requests.get(nave)
            d3 = p3.json()
            if float(str(d3["length"]).replace(",","")) >= lt:
                lt = float(str(d3["length"]).replace(",",""))
                nave_name = str(d3["name"])
                url = str(d3["url"])
    i = i+1
    c = x

## Respuesta pregunta a)
print("La cantidad de peliculas en donde aparecen planetas cuyo clima sea arido son: "+ str(len(lista)))
## Respuesta pregunta b)
print("La cantidad de Wookies que aparecen en la sexta pelicaula son: "+ str(len(l_wookies)))
## Respuesta pregunta b)
print("la nave mas grande de toda la saga es "+ str(nave_name) + " con un largo de "+str(lt))

