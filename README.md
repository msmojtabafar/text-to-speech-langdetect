# Text-to-Speech with Language Detection 🎤🗣️

A simple Python script that converts input text to speech audio (`mp3`) using Google Text-to-Speech (gTTS). The script automatically detects the language of the input text and generates an audio file in the appropriate language. If the detected language is not supported, it defaults to English. 🌍✨

## Features 🚀

- **Automatic language detection** using `langdetect` 🔍
- Text-to-speech conversion using `gTTS` 🎧
- Supports multiple languages (see supported list below) 🌐
- Saves output as `output.mp3` 💾
- Simple and easy to use via command line 🖥️

## Supported Languages 🌎

The script supports all languages supported by `gTTS`, including but not limited to:

`af`, `ar`, `bn`, `bs`, `ca`, `cs`, `cy`, `da`, `de`, `el`, `en`, `eo`, `es`, `et`, `fi`, `fr`, `gu`, `hi`, `hr`, `hu`, `id`, `is`, `it`, `ja`, `jw`, `ka`, `km`, `kn`, `ko`, `la`, `lv`, `ml`, `mr`, `ms`, `my`, `ne`, `nl`, `no`, `pl`, `pt`, `ro`, `ru`, `si`, `sk`, `sq`, `sr`, `su`, `sv`, `sw`, `ta`, `te`, `th`, `tl`, `tr`, `uk`, `ur`, `vi`, `zh-cn`, `zh-tw`

## Prerequisites 📋

- Python 3.x 🐍
- Internet connection 🌐 (gTTS requires access to Google’s TTS API)

## Installation 🛠️

1. Clone the repository or download the script.

```bash
git clone https://github.com/msmojtabafar/text-to-speech-langdetect.git
cd text-to-speech-langdetect
```

2. Install required packages:

```bash
pip install gTTS langdetect
```

## Usage ▶️

Run the script:

```bash
python main.py
```

You will be prompted to enter the text. The script will detect the language and generate an audio file named `output.mp3`. 🎶

## Example 💡

```
Enter your text: Hello, how are you?
Detected language: en
[+] Audio saved to 'output.mp3'.
```
