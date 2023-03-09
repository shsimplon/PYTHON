from pytube import YouTube


baseurl="https://www.youtube.com"


while  True:
    url= input("donner votre url : ")
    print("voir", url [:len(baseurl) ])
    if url [:len(baseurl) ]== baseurl:

        break               
    else:
        print("try with url youtube")

youtube= YouTube(url)
print(youtube.title)
def register_on_progress(stream, chunk, bytes_remaining):
    bytes_total=stream.filesize - bytes_remaining
    bytes_remaining_pers = bytes_total*100 /stream.filesize 
    
    print("progression de telechargement: " ,int (bytes_remaining_pers), "%")
    
#/// add video progresse 
youtube.register_on_progress_callback(register_on_progress)
#/// downloading 
stream = youtube.streams.get_highest_resolution()
print("....telechargement")
stream.download()
print("....ok")