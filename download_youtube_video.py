from pytubefix import YouTube

#replace with your video address
video_link = "https://youtu.be/NMQVcvrKjfI"

#replace witu folder location where you want to save the video
save_folder = "/content/drive/MyDrive"


yt1 = YouTube(video_link)
video_stream = yt1.streams.get_highest_resolution()
video_stream.download(save_folder)
