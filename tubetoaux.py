import yt_dlp as youtube_dl

def download_youtube_audio(url, audio_format):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Get user input
video_url = input("Enter the YouTube video URL: ").strip()
while not video_url:
    print("You must enter a valid YouTube URL!")
    video_url = input("Enter the YouTube video URL: ").strip()

audio_format = input("Enter the desired audio format (mp3, wav, m4a, etc.): ").strip()

# Download the audio
try:
    download_youtube_audio(video_url, audio_format)
    print("Download complete!")
except Exception as e:
    print(f"An error occurred: {e}")
