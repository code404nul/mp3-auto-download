import urllib.request
import re
import youtube_dl
file = open('file.txt', "r")
lines = file.readlines()
file.close()
for line in lines:

    mot = line.strip()
    if mot == "fin":
        print ("telechargement terminé ! ")
        quit()
    else:
        search_keyword=mot
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        yt_link = ("https://www.youtube.com/watch?v=" + video_ids[0])
        print(yt_link)
        video_url = yt_link
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print(mot)