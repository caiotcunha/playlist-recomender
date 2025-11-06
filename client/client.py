import requests
import json

print("as musicas que você quer encontrar recomendações proximas separadas por virgula")
input = input("Músicas: ")

songs = input.strip().split(",")

songs = set(songs)
songs = list(songs)

payload = {
    "songs" : songs
}

response = requests.post("http://localhost:50033/api/recommend",json=payload)

print(response.text)
