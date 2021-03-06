import moviepy.editor
from pytube import YouTube
from youtube_search import YoutubeSearch

import config


def get_search_list(string):
    result = YoutubeSearch(string, max_results=10).to_dict()
    options = ""
    options_dict = []
    counter = 0
    for option in result:
        if len(option['duration']) == 7 and int(option['duration'][:-6]) <= 3 or len(option['duration']) <= 7:
            options += '*' + str(counter + 1) + '* ► ' + option['title'] + ' *[' + option['duration'] + ']*\n'
            options_dict.append(option['id'])
            counter += 1
    return options, options_dict

def download_audio(id):
    vid = YouTube('http://youtube.com/watch?v=' + id)
    stream = vid.streams.first()
    stream.download(output_path=config.TEMP_AUDIO_FOLDER, filename='audio')
    video = moviepy.editor.VideoFileClip(config.TEMP_AUDIO_FOLDER + 'audio.mp4')
    audio = video.audio
    audio.write_audiofile(config.TEMP_AUDIO_FOLDER + 'audio.mp3')
    audio.close()
    video.close()
