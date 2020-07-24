print("Before you run the rest of this program, make sure you downloaded the FFmpeg and add it into the System Path.")
import requests
import json
import os
import shutil
nes_id = input("Id:")
true_urls_noredirect = "http://music.163.com/song/media/outer/url?id={}.mp3".format(nes_id)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/35.0.1916.138 Safari/537.36'}
location = requests.head(true_urls_noredirect, headers=headers, allow_redirects=False).headers['location']
true_url = location
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
     
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
     
    # 判断结果
    if not isExists:
        os.makedirs(path) 
    else:
        pass
print("Downloading with requests...")    
r = requests.get(true_url)
username = input("Your user name:")
path_make = "C:/Users/{}/Desktop/temp".format(username)
mkdir(path_make)
filename_pre = r"C:/Users/{}/Desktop/temp".format(username)
filename = filename_pre  + "/" + nes_id + ".mp3"
with open(filename , "w") as f:
    f.close()
with open(filename, "wb") as code:
  code.write(r.content)
lyric_true_src = "http://music.163.com/api/song/media?id={}".format(nes_id)
lyric_pre = json.loads(requests.get(lyric_true_src).text)
lyric = lyric_pre["lyric"]
with open(r"C:\\Users\{}\Desktop\temp\read.txt".format(username),"w",encoding = "UTF-8") as wri:
    wri.write(lyric)
with open(r"C:\\Users\{}\Desktop\temp\read.txt".format(username), "r",encoding = "UTF-8") as f:
    data = f.read()
pre = data.replace("[","")
fin = pre.replace("]","|")
finally_da = fin.split("\n")
lyric = []
time = []
for i in range(len(finally_da)):
    mid = finally_da[i].split("|")
    try:
        lyric.append(mid[1])
        time.append(mid[0])
    except IndexError:
        pass
del lyric[0]
del time[0]

with open(r"C:\\Users\{}\Desktop\temp\Test.srt".format(username) ,"w",encoding = "UTF-8") as file:
    for j in range(len(lyric)):
        try:
            file.write(str(j + 1) + "\n")
            file.write("00:" + time[j].replace(".",",") + "0" + " --> " + "00:" + time[j + 1].replace(".",",") + "0\n")
            file.write(lyric[j] + "\n\n")
        except IndexError:
            pass
from mutagen.mp3 import MP3
audio = MP3(r"C:\\Users\{}\Desktop\temp\{}.mp3".format(username,nes_id))
secs = audio.info.length
command = r"cd C:\Users\{}\Desktop\temp".format(username)
command_1 = r"ffmpeg -ss 0 -t {} -f lavfi -i color=c=0x000000:s=1920x1080:r=25  -i C:\Users\Maxwang\Desktop\pixiv\82836234_p0.jpg -filter_complex  [1:v]scale=1920:1080[v1];[0:v][v1]overlay=0:0[outv]  -map [outv] -c:v libx264 out.mp4 -y".format(secs)
command_2 = "ffmpeg -i {}.mp3 -i out.mp4 -y BGM.mp4".format(nes_id)
command_3 = "ffmpeg -i BGM.mp4 -vf subtitles=Test.srt {}.mp4".format(nes_id)
print(command)
print(command_1)
print(command_2)
print(command_3)
os.system(command_1)
os.system(command_2)
os.system(command_3)
shutil.copyfile(r"C:/Users/{}/Desktop/temp/{}.mp4".format(username,nes_id), r"C:/Users/{}/Desktop/{}.mp4".format(username,nes_id))
shutil.rmtree(r"C:/Users/{}/Desktop/temp".format(username))
