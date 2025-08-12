from langdetect import detect, LangDetectException
from gtts import gTTS
import os

def text_to_speech_save():
    text = input("Enter your text: ").strip()
    if not text:
        print("[!] The input text is empty.")
        return

    try:
        lang = detect(text)
        print(f"زبان شناسایی شده: {lang}")
    except LangDetectException:
        print("[!] Error in language detection, assuming English.")
        lang = "en"

    # زبان‌های پشتیبانی شده توسط gTTS
    supported_langs = ['af', 'ar', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de',
                       'el', 'en', 'eo', 'es', 'et', 'fi', 'fr', 'gu', 'hi',
                       'hr', 'hu', 'id', 'is', 'it', 'ja', 'jw', 'ka', 'km',
                       'kn', 'ko', 'la', 'lv', 'ml', 'mr', 'ms', 'my', 'ne',
                       'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'si', 'sk', 'sq',
                       'sr', 'su', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'tr',
                       'uk', 'ur', 'vi', 'zh-cn', 'zh-tw', 'fa']

    if lang not in supported_langs:
        print(f"[!] Language {lang} is not supported by gTTS, we are using English.")
        lang = "en"

    try:
        tts = gTTS(text=text, lang=lang)
        filename = "output.mp3"
        tts.save(filename)
        print(f"[+] Converted audio saved to file '{filename}'.")
    except Exception as e:
        print(f"[!] Error in text-to-speech conversion: {e}")

if __name__ == "__main__":

    text_to_speech_save()
