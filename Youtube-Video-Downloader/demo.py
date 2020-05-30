# from pytube import *
#
# ob = YouTube("https://www.youtube.com/watch?v=gLa9nxZNI-g&list=RDgLa9nxZNI-g")
# path_to_save_video = "C:\\Users\\Bablu\\Desktop"
#strm = ob.streams.all() # to get all the streams of the video
# print(type(strm))
# print(ob.title)
# print(ob.description)
# (strm.filesize)
# print(strm[2].filesize)
# for s in strm:
#     print(s)
strm = ob.streams.first()
print(strm,strm.filesize)
# Downloading the Youtube :--> we need the path to download
# ob.download(path_to_save_video)

