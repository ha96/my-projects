#this code currently not working dut to youtube contenuasly update 
from pytube import YouTube
import os
User=(os.getlogin( ) )

url=input("please enter the URL here:")

vid=YouTube(url)

print("**************video info***********\n")
print("the video title :",vid.title)
print("the thumbnail url :",vid.thumbnail_url)
print("the number of viwes :",vid.views)
print("the video length :",vid.length/60,"minutes")
print("The video Size  is : ",round(vid.streams.get_highest_resolution().filesize/1024000),"MB")
print("The video will be downloaded by resolution : ",(vid.streams.get_highest_resolution().resolution))

choice=input("please enter 1 for video and 2 audio : ")

if choice =="1":
    vid.streams.get_highest_resolution().download(f"C:\\Users\\{User}\\Desktop\\Youtube-Download\\{vid.title}", filename=f"{vid.title} Video.mp4")
    
if choice =="2":
    vid.streams.get_audio_only().download(f"C:\\Users\\{User}\\Desktop\\Youtube-Download\\{vid.title}", filename=f"{vid.title} Audio.mp3")
    
print("*******dawonload completed********")

