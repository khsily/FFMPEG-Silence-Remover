from tkinter import *
from tkinter import filedialog
from unsilence import unsilence

def main():
  Tk().withdraw()
  inputs = filedialog.askopenfilenames(title="변환할 음원 선택", filetypes=[("Audio Files", ".mp3 .wav .ogg")])
  outPath = filedialog.askdirectory(title="저장 경로 선택")

  if (not inputs or not outPath):
    return

  for input in inputs:
    unsilence(input, outPath)


main()