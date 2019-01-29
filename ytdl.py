from __future__ import unicode_literals
import youtube_dl

link = str(input("Paste your youtube link: "))

a = int(input("Please select a format. Press 1 for video or 2 for audio: "))

if a == 1:
    video = input("What video format would you like to download (avi,mp4,...): ")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'videoformat' : video,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': video,
        }],
    }
    
elif a == 2:
    audio = input("What audio format would you like to download (flac,mp3,...): ")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio,
            'preferredquality': '192',
        }],
    }


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
