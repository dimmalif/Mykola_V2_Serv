from Skills.skills import BFunction

import fileinput
import os
import re
import webbrowser
import youtube_dl
from moviepy.editor import *
from ytmusicapi import YTMusic

req = 'гимн панков'

class Search_music():
    """This class accepts a path to a download folder and a query (the name of a music group).
        It is possible to search for the album of the specified group using "search_music_albums" and
        open the result in the browser.
        It is the parent class for the "Download_music" class, which is currently under development"""

    # change description

    def __init__(self, requests):
        super().__init__()
        self.to_open = None
        self.top_result = None
        self.all_links = []
        self.requests = requests
        self.options = {'keepvideo': False}

    def search_music_albums(self):
        self.all_links = []
        yt = YTMusic()
        search_results_albums = yt.search(self.requests,
                                          filter='albums')  # search result for request with a given filter
        ids = [search_results_albums[i]['browseId'] for i in range(len(search_results_albums))]
        albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]  # getting a name albums
        audio_playlist_id = [i['audioPlaylistId'] for i in albums]

        # getting a link to the first album
        self.to_open = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'
        print(self.to_open)
        # getting a link to the all albums
        lst = [i for i in range(len(audio_playlist_id))]
        audio_playlist_dictionary = dict(zip(audio_playlist_id, lst))
        for i in range(len(list(audio_playlist_dictionary))):
            self.all_links.append(f'https://music.youtube.com/watch?v=&list={list(audio_playlist_dictionary)[i]}')

    def search_top_result(self):
        yt = YTMusic()
        search_results = yt.search(self.requests)
        result = search_results
        self.top_result = f'https://music.youtube.com/watch?v={result[0]["videoId"]}'
        self.to_open = self.top_result
        print(self.to_open)

    def browser_open(self):
        webbrowser.open(self.to_open)


# 1)перевести перевірку та реформатування у окремий клас 2) оптимізувати клас(постійно прописується схожий код)
class Downloader_music(Search_music):
    def __init__(self, requests, save_link):
        super().__init__(requests)
        self.save_link = save_link
        self.not_found_file = None
        self.file_list = []
        self.name = []
        self.VIDEO_FILE_PATH = "/home/dmytro/Desktop/Mykola/Mykola_V2_Serv/Skills/downloader_music"
        self.AUDIO_FILE_PATH = "/home/dmytro/Desktop/Mykola/Mykola_V2_Serv/Skills/downloader_music/mp3_files"

    def download_first_albums(self):
        self.search_music_albums()

        self.video_info = youtube_dl.YoutubeDL().extract_info(url=self.to_open, download=False)

        if not self.check_file():
            self.renamed_downloads_file()
            return 0

        with youtube_dl.YoutubeDL(self.options) as ydl:
            ydl.download([self.video_info['webpage_url']])
        self.renamed_downloads_file()

    def download_all_albums(self):
        self.search_music_albums()
        self.check_file()
        for i in self.all_links:
            # print(f"'Download albums:'{}") НЕ В ТОПКУ!
            self.video_info = youtube_dl.YoutubeDL().extract_info(url=i, download=True)
            with youtube_dl.YoutubeDL(self.options) as ydl:
                ydl.download([self.video_info['webpage_url']])
        self.renamed_downloads_file()

    def download_music(self):
        # self.video_info = youtube_dl.YoutubeDL().extract_info(url=i, download=True)
        pass

    def check_file(self):
        print('checked')
        for i in range(len(self.video_info['entries'])):
            self.name.append(f"{self.video_info['entries'][i]['title']}-{self.video_info['entries'][i]['id']}")

        try:
            for i in range(len(self.name)):
                f = open(f"{self.name[i]}.mp4")
                f.close()
                self.file_list.append(self.name[i])
            return False
        except FileNotFoundError:
            self.not_found_file = list(set(self.name).difference(self.file_list))
            return True

    def renamed_downloads_file(self):
        for i in range(len(self.name)):
            video_path = f"{self.VIDEO_FILE_PATH}/{self.name[i]}.mp4"
            audio_path = f"{self.AUDIO_FILE_PATH}/{self.name[i]}.mp3"

            FILETOCONVERT = AudioFileClip(video_path)
            FILETOCONVERT.write_audiofile(audio_path)
            FILETOCONVERT.close()

        return print('renamed is successful')

    def delete_mp4(self):
        print('start delete')
        for i in range(len(self.name)):
            fileinput.close()
            os.remove(f"{self.name[i]}.mp4")
            print(f"removed {self.name[i]}")


# class Work_with_file(Downloader_music):
#     def __init__(self, requests, save_link):
#         super().__init__(requests, save_link)


r = Downloader_music(req)

r.download_first_albums()
