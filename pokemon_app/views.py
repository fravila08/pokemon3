from django.shortcuts import render
from django.http import HttpResponse
import requests
import random

# Create your views here.
def home(request):
    data={
        "types":['fire', 'water', 'ground', 'electric', 'dragon']
    }
    return render(request, "pages/index.html", data)

def poketype(request, indivType):
    answer=[]
    pokemon=requests.get(f"https://pokeapi.co/api/v2/type/{indivType}/")
    pokemon=pokemon.json()
    def getUrl():
        rand_num=random.randint(1, 35)
        url=pokemon["pokemon"][rand_num]["pokemon"]["url"]
        return url
    def indivPoke(url):
        almost={}
        newPokemon=requests.get(f"{url}")
        newPokemon=newPokemon.json()
        # print(newPokemon["name"])
        # print(newPokemon["sprites"]["front_default"])
        almost["name"]=newPokemon["name"]
        almost["picture"]=newPokemon["sprites"]["front_default"]
        return almost
    for i in range(6):
        myUrl=getUrl()
        answer.append(indivPoke(myUrl))
    data={
        "information":indivType,
        "pokemons": answer
    }
    # print(answer)
    # print(len(answer))
    return render(request, "pages/poketype.html", data)