from pytube import YouTube
import moviepy.editor as mp
import re
import os

# links para download
diretorio = './videos'
dir_music = './musics'

with open("lista_de_musicas.txt", "r") as music_list:
    line = music_list.readlines()

for url in line:
    link = url
    yt = YouTube(link)
    print("Baixando......")
    ys = yt.streams.filter(only_audio=True).first().download(diretorio)
    print("Dowload Completo")
    print('Convertendo arquivo...')
    for file in os.listdir(diretorio):
        if re.search('mp4', file):
                mp4_path = os.path.join(diretorio, file)
                mp3_path = os.path.join(dir_music, os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
    print('Music MP3 Complete! ')




