import argparse
import os, sys, subprocess, shlex, re
from subprocess import call

parser = argparse.ArgumentParser(description='Get video information')
parser.add_argument('in_filename', help='Input filename')
args = parser.parse_args()


def probe_file(filename):
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


probe_file(args.in_filename)
#probe_file('bbb_10s.mp4')