# Python FFMPEG Silence Remover
Python Silence remover using ffmpeg.
Only works on windows

## Getting started
1. Download ffmpeg: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z
2. Move bin/ffmpeg.exe to project root

## Run program
```
$ python ./main.py
```

## Packaging
```
$ start package.bat
```

## Working process
1. Select audio files
2. Select fold to save results
3. Convert audios (remove Silence, Add Short silence at the beginning and the end, volume up 2.5 times)
4. Save audio as [audio_name]H.wav and [audio_name]S.wav