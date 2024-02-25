# ========================================== Youtube video downloader ==========================================
# import libraries + clear the terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')
import sys
import time
import subprocess
from pytube import YouTube
from pytube.cli import on_progress

# function to print progress bar
def progress_bar(stream, bytes_remaining):
    contentSize = stream.filesize
    size = contentSize
    p = 0
    while p <= 100:
        progress = p
        print(f"Downloaded {progress}%")
        p = percent(bytes_remaining, size)

# function to calculate percentage
def percent(tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc

# function to download video with audio
def download_video(url, path):
    # download the video
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(path)
    print("Download completed")


# function call the download function
def download(url, path, audio=True):
    if not os.path.exists(path):
        os.makedirs(path)

    if audio:
        download_video(url, path)
    else:
        # download the audio
        yt = YouTube(url, on_progress_callback=on_progress)
        yt.streams.filter(only_audio=True).first().download(path)
        print("Download completed")

    # ask if the user wants to open the file
    if input("Do you want to open the file? (y/n): ").lower() == "y":
        if sys.platform == "win32":
            os.startfile(f"{path}/{url.split('=')[1]}.mp4")
        else:
            print("Can't open the file")

# main function
def main():
    # ask for the url, path and audio
    url = input("Enter the video url: ") #https://www.youtube.com/watch?v=UmtmkMrFFRI TEST URL
    path = "downloads"
    audio = True if input("Do you want to download audio? (y/n): ").lower() == "y" else False

    # check if the file name doens't exist, change the name if it does
    if os.path.exists(f"{path}/{url.split('=')[1]}.mp4"):
        url = f"{url.split('=')[0]}={url.split('=')[1]}"
        print("File already exists, changing the name")

    # call download function
    download(url, path, audio)

# call main function
if __name__ == '__main__':
    main()