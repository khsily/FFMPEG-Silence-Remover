import os

this_script_dir = os.path.dirname(os.path.realpath(__file__))
ffmpeg_path = this_script_dir + '\\ffmpeg.exe'

def unsilence(input, outPath):
  filename = input.split('/')[-1]
  name = filename.split('.')[0]
  ext = filename.split('.')[-1]
  outputName = outPath + '/' + name
  outH = outputName + 'H' + '.wav'
  outS = outputName + 'S' + '.wav'

  commands = [
    f'mkdir .ffmpeg-tmp',
    f'copy {input} .ffmpeg-tmp/input.{ext}'.replace('/', '\\'),
    f'{ffmpeg_path} -i .ffmpeg-tmp/input.{ext} -af silenceremove=stop_periods=-1:stop_threshold=0.0005:start_mode=all .ffmpeg-tmp/tmp.wav -y', # Remove Slience
    f'{ffmpeg_path} -i .ffmpeg-tmp/tmp.wav -af apad=pad_dur=0.4 .ffmpeg-tmp/tmp2.wav -y', # Add 0.4s slience at the end
    f'{ffmpeg_path} -i .ffmpeg-tmp/tmp2.wav -af adelay=200:all=true .ffmpeg-tmp/tmp3.wav -y', # Add 0.2s slience at the beginning
    f'{ffmpeg_path} -i .ffmpeg-tmp/tmp3.wav -filter:a volume=2.5 {outH} -y', # Volume 2.5 times up
    f'copy {outH} {outS}'.replace('/', '\\'),
    'rmdir /s /q .ffmpeg-tmp',
  ]

  for command in commands:
      if os.system(command) == 0:
          continue
      else:
          print("ERROR")
          break