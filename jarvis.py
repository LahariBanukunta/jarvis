#jarvis\Scripts\activate
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from gtts import gTTS
from translate import Translator

engine = pyttsx3.init('espeak')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def translate_text(text, dest_lang):
    translator = Translator(to_lang=dest_lang)
    translated_text = translator.translate(text)
    return translated_text

def speak_text(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("Hello, I am Jarvis. Please tell me how I can help you")

def takeCommand():
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
        print("Say that again please...")
        speak("Say that again please...")
        return None
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
    'chinese': 'zh-CN',
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

def get_language_code(lang_name):
    return language_codes.get(lang_name.lower())

def recite_tongue_twister():
    tongue_twisters = [
        "Peter Piper picked a peck of pickled peppers.",
        "She sells sea shells by the sea shore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Betty Botter bought some butter, but she said the butter’s bitter.",
        "I scream, you scream, we all scream for ice cream."
    ]
    twister = random.choice(tongue_twisters)
    print(twister)
    return twister

def recite_motivational_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
        "Your time is limited, don’t waste it living someone else’s life. - Steve Jobs",
        "The best revenge is massive success. - Frank Sinatra",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson"
    ]
    quote = random.choice(quotes)
    print(quote)
    speak(quote)

def tell_fun_fact():
    fun_facts = [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
        "A single cloud can weigh more than a million pounds.",
        "There are more stars in the universe than grains of sand on all the beaches on Earth.",
        "A day on Venus is longer than a year on Venus.",
        "Bananas are berries, but strawberries are not."
    ]
    fact = random.choice(fun_facts)
    print(fact)
    speak(fact)
def search_wikipedia(query):
    try:
        search_results = wikipedia.search(query)
        if search_results:
            first_article = search_results[0]
            speak(f"Showing results for {first_article} on Wikipedia.")
            result_summary = wikipedia.summary(first_article, sentences=2)
            print(result_summary)
            speak(result_summary)
        else:
            speak("No results found on Wikipedia.")
    except Exception as e:
        speak("Sorry, I encountered an error while searching Wikipedia.")
        print(e)
def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except Exception as e:
        return f"Sorry, I couldn't evaluate the expression: {e}"

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query:
            query = query.lower()

            print(f"User said: {query}")  # Debugging line

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            search_wikipedia(query)
        elif 'open camera' in query:
            speak('Opening camera')
            os.system("start microsoft.windows.camera:")
        elif 'open' in query:
            sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"], ["chatbot", "https://www.chatgpt.com"]]
            for site in sites:
                if f"open {site[0]}" in query:
                    speak(f"Opening {site[0]}...")
                    webbrowser.open(site[1])
        elif "hello" in query or 'hi' in query:
            speak("Hello there!")
        elif "how are you" in query:
            speak("Hi, I'm doing great, thank you for asking!")
        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break
        elif 'time' in query:  # Fixed the condition here
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'thank you' in query:
            speak('My pleasure. I am happy that I am able to help you. Can I do anything else for you?')
        elif 'yourself' in query:
            speak("My name is Jarvis. I was created by Lahari Banukunta. She is a fan of Tony Stark AKA Iron Man. Jarvis stands for Just a Rather Very Intelligent System. I am named after an artificial intelligence created by Tony Stark. Thank you for listening to me! Is there anything else that I can do for you?")
        elif 'whatsApp' in query:
            speak('Opening WhatsApp')
            webbrowser.open()
        elif 'quit' in query or 'exit' in query or 'shut down' in query:
            speak('Bye! Have a nice day')
            print('Quitting')
            break
        elif 'calculate' in query:
            speak('Evaluating')
            query = query.replace('calculate', '')
            query = query.replace('plus', '+')
            query = query.replace('minus', '-')
            query = query.replace('by', '/')
            query = query.replace('into', '*')
            query = query.replace('point', '.')
            result = calculate(query)
            speak(result)
        elif 'translate' in query:
            speak("What do you want to translate?")
            text = takeCommand()
            speak("Which language do you want to translate to?")
            dest_lang = takeCommand().lower()
            lang_code = get_language_code(dest_lang)
            if lang_code:
                translated_text = translate_text(text, lang_code)
                print(f"Translated Text: {translated_text}")
                speak_text(translated_text, lang_code)
            else:
                speak("Sorry, I don't support that language.")
        elif 'tongue twister' in query:
            twister = recite_tongue_twister()
            speak(twister)
        elif 'motivate me' in query or 'quote' in query:
            recite_motivational_quote()
        elif 'fun fact' in query:
            tell_fun_fact()
        else:
            speak("Sorry, I didn't understand that.")
