import vlc
temp = "D:/download/music/qwe.mp3"
player = vlc.MediaPlayer(temp)
player.play()


# import vlc
# import time

# url = "listen.di.fm/premium_high/vocaltrance.pls?38af6c59409db3cfade9e2ed"

# Instance = vlc.Instance()
# player = Instance.media_player_new()
# Media = Instance.media_new(url)
# #Media_list = Instance.media_list_new([url])
# Media.get_mrl()
# player.set_media(Media)
# player.play()