# -*- coding: utf-8 -*-
import os
from pydub import AudioSegment
from lib_for_video import beat2msec
from FFM import FFmpeg
 
def audio2wav(path: str):
    extension = os.path.splitext(path)[1].replace(".","")
    audio = AudioSegment.from_file(path, format=extension)
    # 保存为 WAV 格式
    audio.export("tmp/music.wav", format="wav")
    
def PhiAudio(audioPath, hitsoundlist, bpm, hitsoundoffset, musicoffset, length,var,showframe):
    musicoffset = -musicoffset
    output = AudioSegment.silent(duration=length * 1000)
    music = AudioSegment.from_wav(audioPath)
    if(musicoffset < 0):
        music = music[-musicoffset: length * 1000]
        output = output.overlay(music, position=0)
    else:
        output = output.overlay(music, position=musicoffset)
    tap = AudioSegment.from_wav('Source/hitsound/HitSong0.wav')
    drag =  AudioSegment.from_wav('Source/hitsound/HitSong1.wav')
    flick = AudioSegment.from_wav('Source/hitsound/HitSong2.wav')
    
    # print(hitsoundlist)
    for i in range(0, len(hitsoundlist)):
        var.set("正在生成音频 "+str(round(100*i/len(hitsoundlist),0))+"%")
        showframe.update()
        currentNote = hitsoundlist[i][1]
        currentBeat = hitsoundlist[i][0]
        if(currentNote == 1 or currentNote == 3):
            sound = tap
        elif(currentNote == 2):
            sound = drag
        else:
            sound = flick
        
        output = output.overlay(sound, position=beat2msec(currentBeat, bpm, hitsoundoffset))
    
    print("音频生成成功")
    output.export("tmp/hitsound.wav", format="wav")  # 保存文件

def video_add_audio(video_path: str, audio_path: str, output_dir: str, videoname: str):

    _ext_audio = os.path.basename(audio_path).strip().split('.')[-1]
    if _ext_audio not in ['mp3', 'wav']:
        raise Exception('audio format not support')
    _codec = 'copy'
    if _ext_audio == 'wav':
        _codec = 'aac'
    result = os.path.join(output_dir, videoname)
    ff = FFmpeg(
        inputs={video_path: None, audio_path: None},
        outputs={result: '-map 0:v -map 1:a -c:v copy -c:a {} -y'.format(_codec)})
    ff.run()
    return result