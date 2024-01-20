'''
from pytube import Playlist


playlist = Playlist('https://www.youtube.com/playlist?list=PLIWddFTtxpLiotTcG4iDSo7VX53ppSuhG')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
'''

a = 10
b = 12
if (a and b):
 print("yes")