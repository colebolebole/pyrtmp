import vlc

def play_rtmp(url):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    player.set_media(media)
    player.play()
    
    while True:
        continue

url = "rtmp://your-rtmp-url.com/live/stream_name"
play_rtmp(url)
