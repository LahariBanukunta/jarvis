import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
from googletrans import Translator
from gtts import gTTS





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   
    else:
        speak("good evening")

    speak("hello lucky I am Jarvis. Please tell me how can I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


language_codes = {
    'afrikaans': 'af',
    'albanian': 'sq',
    'amharic': 'am',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinese': 'zh-CN',  # Simplified Chinese
    'corsican': 'co',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'frisian': 'fy',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hawaiian': 'haw',
    'hebrew': 'iw',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'kinyarwanda': 'rw',
    'korean': 'ko',
    'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar (burmese)': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'punjabi': 'pa',
    'romanian': 'ro',
    'russian': 'ru',
    'samoan': 'sm',
    'scots gaelic': 'gd',
    'serbian': 'sr',
    'sesotho': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'sinhala': 'si',
    'slovak': 'sk',
    'slovenian': 'sl',
    'somali': 'so',
    'spanish': 'es',
    'sundanese': 'su',
    'swahili': 'sw',
    'swedish': 'sv',
    'tajik': 'tg',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uyghur': 'ug',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'xhosa': 'xh',
    'yiddish': 'yi',
    'yoruba': 'yo',
    'zulu': 'zu'
}

def translate_text(text, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text, translated_text.src

def get_language_code(lang_name):
    return language_codes.get(lang_name.lower())

def speak_text(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")





def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except Exception as e:
        return f"Sorry, I couldn't evaluate the expression: {e}"


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open camera' in query:
            speak('opening camera')
            os.system("start microsoft.windows.camera:")


        elif 'open' in query:
            sites = [["youtube","https://www.youtube.com"],["google","https://www.google.com"],["chatbot","https://www.chatgpt.com"]]
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    speak(f"opening {site[0]}...")
                    webbrowser.open(site[1])

        elif "hello" in query or 'hi' in query:
            speak("Hello there!")
        elif "how are you" in query:
            speak("hi I'm doing great, thank you for asking!")
        
        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Lucky, the time is {strTime}")

        elif 'thank you' in query:
            speak('my pleasure, i am happy that i am able to help you. can i do anything else for you?')
      
        elif 'yourself' in query:
            speak("My name is Jarvis which stands for Just a Rather Very Intelligent System.i am named after an artificial intelligence created by Tony Stark, who later controls his Iron Man and Hulkbuster armor for him. In Avengers: Age of Ultron, after being partially destroyed by Ultron, Jarvis is given physical form as Vision, physically portrayed by Bettany. Different versions of the character also appear in comics published by Marvel Comics, depicted as AI designed by Iron Man and Nadia van Dyne, thank you for listeing to me! is there any other thing that i can do for you?")
        
        elif 'whatsapp' in query:
            speak('opening whatsapp')
            webbrowser.open()
        elif 'quit' in query or 'by' in query or 'go' in query or 'bye' in query:
            speak('Bye lucky. Have a nice day')
            print('quitting')
            break 
        elif 'calculate' in query:
            speak('evaluating')
            query=query.replace('calculate','')
            query=query.replace('plus','+')
            query=query.replace('minus','-')
            query=query.replace('by','/')
            query=query.replace('into','*')
            query=query.replace('point','.')

            result = calculate(query)
            speak(result)
        elif 'translate' in query:
            speak("please tell me the text to translate: ")
            text = takeCommand()
            speak("okay..!Now tell me the language you want to translate it to.")
            dest_lang = takeCommand()

    # Get the language code from language name
            lang_code = get_language_code(dest_lang)
            if lang_code is None:
                print("Invalid language name.")
                

            translated_text, detected_lang = translate_text(text, lang_code)
            print(f"Translated text: {translated_text}")

            speak_text(translated_text, lang_code)

    

       
        

        

            

            
    
