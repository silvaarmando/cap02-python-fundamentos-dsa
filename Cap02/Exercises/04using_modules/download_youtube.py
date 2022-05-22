from pytube import YouTube

url = str(input('YouTube URL for download: '))
video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path = 'wb')