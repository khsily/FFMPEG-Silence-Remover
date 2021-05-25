# Python FFMPEG Silence Remover
ffmpeg를 활용한 오디오 공백 제거

## Preoare
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
1. 변환할 오디오 파일 선택 (다중선택 가능)
2. 결과를 저장할 폴더 선택
3. 오디오 변환 (공백 제거, 앞뒤 짧은 공백 추가, 볼륨 2.5배)
4. [오디오이름]H.wav / [오디오이름]S.wav 로 저장