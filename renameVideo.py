import os

# a la primera part el video amb el nom original, a la segona el video a renombrar.
# comprobar que els directoris siguin correctes

os.rename('bbb_10s.mp4', 'Original.mp4')
os.rename('bbb_720.mp4', 'Quality720.mp4')
os.rename('bbb_480.mp4', 'Quality480.mp4')
os.rename('bbb_360.mp4', 'Quality360.mp4')
os.rename('bbb_120.mp4', 'Quality120.mp4')