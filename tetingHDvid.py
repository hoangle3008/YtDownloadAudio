
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.editor import *
import os
import glob

#https://www.youtube.com/watch?v=okz5RIZRT0U
#C:\Users\huy\Downloads\YtVidDl

VLink=input("enter video link: ")
dir_name= input("enter directory path: ")
#NewName=input("New name for file: ")

def VideoDLandExtract():
    #VLink=input("enter the link: ")
    #dir_name= input("enter directory path: ")
    #folder=os.listdir(dir_name)
    #yt_playlist= Playlist(PlLink)
    yt_video= YouTube(VLink)

    yt_video.streams.get_lowest_resolution().download(dir_name)#part of pytube library to download to the destination folder
    print ("video downloaded: ", yt_video.title) #just printing to make see evrytime a video finish

        #not sure what this does here but im setting this into a variable and the /*.mp4 part select and go through the mp4 fi
    folderglob= glob.glob(dir_name+'/*.mp4') 

    for video in folderglob:

        print(video.title)
        #now this part is using moviepy to do the extracting mp3 out of the video
        videoclip=VideoFileClip(video)
        audioclip=videoclip.audio
        # print("im here")
        audioclip.write_audiofile(video[:-3]+'.mp3')
        print("converted to mp3, Mp4 deleted")

        
            #os.remove(os.path.join(dir_name,file))

            #here we have to close the file, because when we are extracting, the file is open and it wont let us delete
            #if we dont .close()
        videoclip.close()
        os.remove(os.path.join(dir_name,video))
        return audioclip

        

def downloadYTHD():
    #VLink=input("enter the link: ")
    #dir_name= input("enter directory path: ")


    yt=YouTube(VLink)
    print(yt.title)
    # stream= yt.streams.filter(file_extension='mp4')
    # print(stream)

    getitag=399

    stream=yt.streams.get_by_itag(getitag)
    stream.download(dir_name)
    print('HD video download finished')

    return stream

    



# VideoDLandExtract()
# downloadYTHD()
#"C:/Users\huy\Downloads\YtVidDl\Tình Yêu Hoa Gió  Trương Thế Vinh  Official MV" 

def combine():
    clip=VideoFileClip(VideoDLandExtract.audioclip.title)

    mp3=AudioFileClip(downloadYTHD.stream.title)

    videoclip= clip.set_audio(mp3)


VideoDLandExtract()
downloadYTHD()
combine()



