import os
import tempfile
import time
from pytube import YouTube
import ffmpeg

n = int(input("Enter number of videos : "))

# Below line read inputs from user using map() function
link = list(map(str, input("\nEnter the links : ").strip().split()))[:n]

path = input("Enter the path where you want to save the video/s\ne.g.'{}' ".format(r"C:\\Users\\"))

tempPath = tempfile.gettempdir()
print("Got Temp Folder Successfully")

resolution = input("Enter Resolution \n e.g '720p' , '1080p' ")

for i in link:
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
    ffmpeg.output(audio_stream, video_stream, '{}{}[rahulbagdi].mp4'.format(path, yt.title)).run()
    print("Deleting Temp Files")
    time.sleep(2)
    os.remove(r"{}\\video.mp4".format(videoPath))
    os.remove(r"{}\\audio.mp4".format(audioPath))
    print("Download Finished at {}".format(path))
