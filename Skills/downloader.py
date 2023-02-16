import os

from pytube import Search, YouTube
from Skills.BFunction import *


class Downloader(BFunction):
    def __init__(self, text_data):
        super().__init__(text_data)
        self.video_obj = None
        self.file_path = None
        self._title_video = None
        self._res_search = None
        
    def download(self):
        path_file = '/home/dmytro/Desktop/Mykola/Bot_Mykola'
        print(f'{self.request} - запит у ф-ї скачування')
        self._res_search = [i.watch_url for i in Search(self.request).results] # get all found links
        self.video_obj = YouTube(f"http://youtube.com/watch?v={self._res_search}") # create YouTube object
        self._title_video = self.video_obj.title # get video title
        to_download = self.video_obj.streams.filter(only_audio=True)[0] # get stream with filter
        to_download.download(filename=f"{self._title_video.replace('/','')}.mp3") # download received stream
        self.file_path = f"{path_file}/{self._title_video.replace('/','')}.mp3"
        return self.file_path

    def del_file(self):
        print('start delete')
        os.remove(f"{self.file_path}.mp3")
        print(f"removed {self._title_video}")


# text_data = 'Коля скачай пісню червона рута'
#
# Searcher(text_data)