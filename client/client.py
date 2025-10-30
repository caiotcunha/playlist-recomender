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

response = requests.post("http://127.0.0.1:5000/api/recommend",json=payload)

print(response.text)
