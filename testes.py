# read arquivos
from os import lseek


with open("lista_de_musicas.txt", "r") as music_list:
    line = music_list.readlines()

for url in line:
     print(url)
