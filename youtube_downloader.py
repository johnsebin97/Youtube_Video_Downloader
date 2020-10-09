from pytube import YouTube


print("Enter Youtube video url : ")
url = input()
yt = YouTube(url)
videos = yt.streams.all()
s = 1



for v in videos:
    print(str(s)+ ". "+str(v))
    s += 1
    

print("Enter the video number from the above list: ")
n = int(input())
vid = videos[n-1]


print("Enter the destination folder location: ")
destination = input()
vid.download(destination)


print("Your File has been downloaded successfully!!")
    
