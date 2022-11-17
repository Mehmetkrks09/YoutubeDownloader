import pytube as py
import time
print("----Made By Mehmet-Karakas-----")
while(True):
    url=input(" Url giriniz : ")
    try:
        yt=py.YouTube(url)
        break
    except:
        print(" Url Geçersiz")
        
video = yt.streams.get_highest_resolution()
print()
print(" Video is Finding..")
print("-----------------------------")
print(yt.title)
print("-----------------------------")
print(" I Started to Download")
video.download()
print("Finish")
print(" I'm Gonna Close in 5 Seconds. See You Later ")
time.sleep(5)
exit()

