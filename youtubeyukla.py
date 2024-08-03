from pytube import YouTube

def download_youtube_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        print(f"Yuklanmoqda: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        print("Yuklab olish tugadi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# Video URL'sini kiriting
video_url = 'https://youtu.be/WbyhzuzYlFw?si=HAx0t9wSo34ulVGE'
download_youtube_video(video_url)
