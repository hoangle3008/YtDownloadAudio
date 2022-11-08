from pytube import Playlist
from pytube import YouTube

from moviepy.editor import VideoFileClip
import os
import glob

#dir_name= input("enter directory path: ")


#dir_name="C:\\Users\huy\Downloads\ytvids"

#folderglob= glob.glob(dir_name+'/*.mp4')

VideoOrPlaylist= input("video or playlist? enter V or P: ")


def PlayListDLandExtract():
    PlLink=input("enter the link: ")
    dir_name= input("enter directory path: ")
    folder=os.listdir(dir_name)
    yt_playlist= Playlist(PlLink)

#for loop to go through the youtube playlist and download
    for video in yt_playlist.videos:
        video.streams.get_lowest_resolution().download(dir_name) #part of pytube library to download to the destination folder
        print ("video downloaded: ", video.title) #just printing to make see evrytime a video finish

        #not sure what this does here but im setting this into a variable and the /*.mp4 part select and go through the mp4 files in the folde
        folderglob= glob.glob(dir_name+'/*.mp4') 

        for video in folderglob:
            #print(video)
            #now this part is using moviepy to do the extracting mp3 out of the video
            videoclip=VideoFileClip(video)
            audioclip=videoclip.audio
            audioclip.write_audiofile(video[:-3]+'.mp3')
            print("converted to mp3")

        
            #os.remove(os.path.join(dir_name,file))

            #here we have to close the file, because when we are extracting, the file is open and it wont let us delete
            #if we dont .close()
            videoclip.close()
            os.remove(os.path.join(dir_name,video))


def VideoDLandExtract():
    VLink=input("enter the link: ")
    dir_name= input("enter directory path: ")
    #folder=os.listdir(dir_name)
    #yt_playlist= Playlist(PlLink)
    yt_video= YouTube(VLink)


#for loop to go through the youtube playlist and dowvnload
    
    yt_video.streams.get_lowest_resolution().download(dir_name)#part of pytube library to download to the destination folder
    print ("video downloaded: ", yt_video.title) #just printing to make see evrytime a video finish

        #not sure what this does here but im setting this into a variable and the /*.mp4 part select and go through the mp4 fi
    folderglob= glob.glob(dir_name+'/*.mp4') 

    for video in folderglob:

        print(video.title)
        #now this part is using moviepy to do the extracting mp3 out of the video
        videoclip=VideoFileClip(video)
        audioclip=videoclip.audio
        audioclip.write_audiofile(video[:-3]+'.mp3')
        print("converted to mp3")

        
            #os.remove(os.path.join(dir_name,file))

            #here we have to close the file, because when we are extracting, the file is open and it wont let us delete
            #if we dont .close()
        videoclip.close()
        os.remove(os.path.join(dir_name,video))



if VideoOrPlaylist=="p":
    print("playlist")
    PlayListDLandExtract()
    print("Playlist download Completed")

elif VideoOrPlaylist=="v":
   
    print("video")
    VideoDLandExtract()
    print("Video download Completed")


