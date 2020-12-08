import sys
import subprocess

# transformar el tamany del video a traves del terminal.
# quan l¡executem hem de posar el nom del video d'entrada i el de sortida
# EXEMPLE:
# python3 resizeInput.py 'inputVideo.mp4' 'outputVideo.mp4'

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

subprocess.call(['ffmpeg', '-i', sys.argv[1], '-vf', out_resolution, sys.argv[2]])