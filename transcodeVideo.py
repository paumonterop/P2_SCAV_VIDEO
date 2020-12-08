import sys
import subprocess

# executar des de terminal amb l'input i l'output
# EXEMPLE:
# python3 transcodeVideo.py 'inputVideo.mp4' 'outputVideo.mp4'

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

subprocess.call(['ffmpeg', '-i', sys.argv[1], '-acodec', 'copy', '-vcodec', out_codec, sys.argv[2]])