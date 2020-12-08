import argparse
import os, sys, subprocess, shlex, re


def videoData():
    print('Introduiu el nom del video:')
    print('\nEXEMPLE: input.mp4')
    filename = input()
    cmnd = ['ffprobe', '-show_format', '-show_streams', '-loglevel', 'quiet', filename]
    p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(filename)
    out, err = p.communicate()
    print("==========output==========")
    #out_string = bytes(out, encoding='utf-8')
    out_string = out.decode()
    outstring = out_string.split('\n')
    print(out_string)

    if err:
        print("========= error ========")
        print(err)

def renameVideo():
        print("Introduiu el nom de l'arxiu i l'ubicació")
        print('EXEMPLE: /Desktop/input.mp4')
        input_rename = input()
        print("Introduiu el nom de l'arxiu de sortida i l'ubicació:")
        print('EXEMPLE: /Desktop/output.mp4')
        output_rename = input()
        os.rename(input_rename, output_rename)


def resizeVideo():
    print("Introduiu el nom de l'arxiu i l'ubicació")
    print('EXEMPLE: /Desktop/input.mp4')
    input_resize = input()
    print("Introduiu el nom de l'arxiu de sortida i l'ubicació:")
    print('EXEMPLE: /Desktop/output.mp4')
    output_resize = input()
    print('Resolució de sortida:\n')
    print('\t 1. 720p \n\t 2. 480p \n\t 3. 360p \n\t 4. 120p')
    resize = input('\nEscull la resolució:')

    if resize == '1':
        out_resolution = 'scale=-1:720'
    elif resize == '2':
        out_resolution = 'scale=852:480'
    elif resize == '3':
        out_resolution = 'scale=-1:360'
    elif resize == '4':
        out_resolution = 'scale=160:120'
    else:
        print("Aquesta opció no existeix")

    subprocess.call(['ffmpeg', '-i', input_resize, '-vf', out_resolution, output_resize])


def transcodeVideo():
    print("Introduiu el nom de l'arxiu i l'ubicació")
    print('EXEMPLE: /Desktop/input.mp4')
    input_trans = input()
    print("Introduiu el nom de l'arxiu de sortida i l'ubicació:")
    print('EXEMPLE: /Desktop/output.mp4')
    output_trans = input()
    print('Resolució de sortida:\n')
    print('\t 1. MPEG4 \n\t 2. MPEG2 \n\t 3. H264')
    codec = input('\nEscull la resolució:')

    if codec == '1':
        out_codec = 'mpeg4'
    elif codec == '2':
        out_codec = 'mpeg2video'
    elif codec == '3':
        out_codec = 'h264'
    else:
        print("Aquesta opció no existeix")

    subprocess.call(['ffmpeg', '-i', input_trans, '-acodec', 'copy', '-vcodec', out_codec, output_trans])


def index():  # index menu inicial
    print('---- PRACTICA 2 ----')
    print('\n')
    print("Seleccioneu l'exercici:")
    print('\n')
    print("\t 1. Mostrar Informació d'un video.")
    print("\t 2. Canviar el nom d'un video.")
    print("\t 3. Canviar la resolució del video.")
    print("\t 4. Canviar el codec d'un video")
    print('\n')
    option = input("Escolliu l'exercici: ")
    return option

def switch(exer):  # switch per triar l'opcio

    print(exer)

    if exer == '1':
        videoData()
    elif exer == '2':
        renameVideo()
    elif exer == '3':
        resizeVideo()
    elif exer == '4':
        transcodeVideo()
    else:
        print("Aquesta opció no existeix. Torna a seleccionar l'exercici (1, 2 ,3, 4):")
        index()

# -------------- MAIN ---------------------


exer = index()

switch(exer)

