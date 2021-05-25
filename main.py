from tkinter import *
from tkinter import filedialog
from unsilence import unsilence

inputs = filedialog.askopenfilenames(title="변환할 음원 선택", filetypes=[("Audio Files", ".mp3 .wav .ogg")])
outPath = filedialog.askdirectory(title="저장 경로 선택")

for idx, input in enumerate(inputs):
  unsilence(input, outPath)
