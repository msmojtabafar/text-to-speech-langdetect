from langdetect import detect, LangDetectException
from gtts import gTTS
import os

def text_to_speech_save():
    text = input("متن خود را وارد کنید: ").strip()
    if not text:
        print("[!] متن ورودی خالی است.")
        return

    try:
        lang = detect(text)
        print(f"زبان شناسایی شده: {lang}")
    except LangDetectException:
        print("[!] خطا در تشخیص زبان، فرض می‌کنیم انگلیسی است.")
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
        print(f"[!] زبان {lang} توسط gTTS پشتیبانی نمی‌شود، از انگلیسی استفاده می‌کنیم.")
        lang = "en"

    try:
        tts = gTTS(text=text, lang=lang)
        filename = "output.mp3"
        tts.save(filename)
        print(f"[+] صدای تبدیل شده در فایل '{filename}' ذخیره شد.")
    except Exception as e:
        print(f"[!] خطا در تبدیل متن به صدا: {e}")

if __name__ == "__main__":
    text_to_speech_save()