from dataclasses import replace
import os
import shutil
import tempfile
import time
from pytube import YouTube
from pytube import Playlist
import ffmpeg
import pyfiglet


print(pyfiglet.figlet_format("YTVD by codingsenpi"))
print("Thank You for using my program :)\n")

method = int(input("Enter 1 to Download Videos\nEnter 11 to Download Complete Playlist\n"))

if method == 1:
        
    n = int(input("Enter number of videos : \n"))

    # Below line read inputs from user using map() function
    link = list(map(str, input("\nEnter the links : ").strip().split()))[:n]

    path = input("Enter the path where you want to save the video/s\ne.g.'{}' \n".format(r"C:\\anyfolder\\"))

    tempPath = tempfile.gettempdir()
    print("Got Temp Folder Successfully")

    resolution = input("Enter Resolution \n e.g '720p' , '1080p' \n")

    for i in link:

        # Deleting last downloaded files
        if os.path.isdir(r"{}\\video".format(tempPath)):
            shutil.rmtree("{}\\video".format(tempPath))
        if os.path.isdir(r"{}\\audio".format(tempPath)):
            shutil.rmtree("{}\\audio".format(tempPath))

        yt = YouTube(i)
        print("Downloading {}".format(yt.title))
        time.sleep(2)
        video = yt.streams.filter(res=resolution).first().download('{}\\video'.format(tempPath))
        print("Got Video Stream Successfully")
        # Renaming video to video.mp4
        videoPath = r"{}\\video\\".format(tempPath)
        videoName = os.listdir(r"{}\\video".format(tempfile.gettempdir()))[0]
        os.rename("{}{}".format(videoPath, videoName), "{}video.mp4".format(videoPath))
        time.sleep(2)
        audio = yt.streams.filter(only_audio=True)
        audio[0].download('{}\\audio'.format(tempPath))
        print("Got Audio Stream Successfully")
        # Renaming audio to audio.mp4
        audioPath = r"{}\\audio\\".format(tempPath)
        audioName = os.listdir(r"{}\\audio".format(tempfile.gettempdir()))[0]
        os.rename("{}{}".format(audioPath, audioName), "{}audio.mp4".format(audioPath))
        time.sleep(2)
        print("Initializing Conversion: Combing Audio and Video")
        audio_stream = ffmpeg.input('{}\\audio\\audio.mp4'.format(tempPath))
        video_stream = ffmpeg.input('{}\\video\\video.mp4'.format(tempPath))
        ffmpeg.output(audio_stream, video_stream, '{}{}.mp4'.format(path, yt.title.replace('/', ""))).run()
        print("Deleting Temp Files")
        time.sleep(2)
        os.remove(r"{}\\video.mp4".format(videoPath))
        os.remove(r"{}\\audio.mp4".format(audioPath))
    print("Download(s) Finished at {}".format(path))

if method == 11:
            
    link = Playlist(input("Enter Playlist URL\n"))

    path = input("Enter the path where you want to save the video/s\ne.g.'{}' \n".format(r"C:\\anyfolder\\"))

    tempPath = tempfile.gettempdir()
    print("Got Temp Folder Successfully")

    resolution = input("Enter Resolution \n e.g '720p' , '1080p' \n")
    for i in link.video_urls:
        # Deleting last downloaded files
        if os.path.isdir(r"{}\\video".format(tempPath)):
            shutil.rmtree("{}\\video".format(tempPath))
        if os.path.isdir(r"{}\\audio".format(tempPath)):
            shutil.rmtree("{}\\audio".format(tempPath))

        yt = YouTube(i)
        print("Downloading {}".format(yt.title))
        time.sleep(2)
        video = yt.streams.filter(res=resolution).first().download('{}\\video'.format(tempPath))
        print("Got Video Stream Successfully")
        # Renaming video to video.mp4
        videoPath = r"{}\\video\\".format(tempPath)
        videoName = os.listdir(r"{}\\video".format(tempfile.gettempdir()))[0]
        os.rename("{}{}".format(videoPath, videoName), "{}video.mp4".format(videoPath))
        time.sleep(2)
        audio = yt.streams.filter(only_audio=True)
        audio[0].download('{}\\audio'.format(tempPath))
        print("Got Audio Stream Successfully")
        # Renaming audio to audio.mp4
        audioPath = r"{}\\audio\\".format(tempPath)
        audioName = os.listdir(r"{}\\audio".format(tempfile.gettempdir()))[0]
        os.rename("{}{}".format(audioPath, audioName), "{}audio.mp4".format(audioPath))
        time.sleep(2)
        print("Initializing Conversion: Combing Audio and Video")
        audio_stream = ffmpeg.input('{}\\audio\\audio.mp4'.format(tempPath))
        video_stream = ffmpeg.input('{}\\video\\video.mp4'.format(tempPath))
        ffmpeg.output(audio_stream, video_stream, '{}{}.mp4'.format(path, yt.title.replace('/', ""))).run()
        print("Deleting Temp Files")
        time.sleep(2)
        os.remove(r"{}\\video.mp4".format(videoPath))
        os.remove(r"{}\\audio.mp4".format(audioPath))
    print("Download(s) Finished at {}".format(path))
