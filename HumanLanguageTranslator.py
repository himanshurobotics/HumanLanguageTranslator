########################################## Importing libraries ########################################
from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import Combobox
import googletrans
from textblob import TextBlob
from tkinter import scrolledtext
#------------------------------------------------------------------------------------------------------

###################################### Translation/Exit Functions #####################################
def translation():
    if inputBox.compare("end-1c", "==", "1.0"):
        outputBox.config(state='normal')
        outputBox.delete("1.0", "end")
        outputBox.config(state='disabled')
        invalidEntry.config(text='Please write something\nto translate...')

    else:
        invalidEntry.config(text=' ')
        input = inputBox.get("1.0", "end-1c")
        
        words = TextBlob(input)
        currentLanguage = words.detect_language()

        for i in languages.items():
            if(languages[i[0]]==currentLanguage):
                detectedLanguage.set(i[0])

        toLanguageKey = selectedLanguage.get()
        toLanguage = languages[toLanguageKey]
        words = words.translate(from_lang=currentLanguage, to=toLanguage)
        outputBox.config(state='normal')
        outputBox.delete("1.0", "end")
        outputBox.insert(1.0, words)
        outputBox.config(state='disabled')

def main_exit():
    quit = messagebox.askyesno('Notification', 'Do you want to exit?', parent=window)
    if(quit==TRUE):
        window.destroy()
#------------------------------------------------------------------------------------------------------

########################################## Translator Window ##########################################
window = Tk()
window.title('Language Translator')
window.iconbitmap(r'C:\Users\varsh\Desktop\Translator\translator.ico') 
window.geometry('830x500')
window.resizable(False,False)
#window.configure(bg='dim gray')
#------------------------------------------------------------------------------------------------------

################################ Translator Window Input/Output Labels ################################
welcomeLabel = Label(window, text ="Welcome to Language Translator", font = ("Times New Roman", 25), background = 'green', foreground = "white")
welcomeLabel.place(x=200, y=0)

nameLabel = Label(window, text ="by Himanshu Varshney", font = ("Times New Roman", 15), background = 'green', foreground = "white")
nameLabel.place(x=323, y=40)

invalidEntry = Label(window, text=' ', font=('Helvetica',10,'italic bold'))
invalidEntry.place(x=337, y=120)

detectedLanguageLabel1 = Label(window, text='Detected Language', font=('Helvetica',11))
detectedLanguageLabel1.place(x=345, y=170)

detectedLanguage = StringVar()
detectedLanguageLabel = Label(window, textvariable=detectedLanguage, font=('Helvetica',15,'bold'))
detectedLanguageLabel.place(x=374, y=190)

selectedLanguageLabel1 = Label(window, text='Selected Language', font=('Helvetica',11))
selectedLanguageLabel1.place(x=345, y=225)

inputLabel = Label(window, text='Input Text', font=('Helvetica',25,'bold'), bg='snow3')
#inputLabel.place(x=90, y=50)
inputLabel.place(x=80, y=70)

outputLabel = Label(window, text='Translated Text', font=('Helvetica',25,'bold'), bg='snow3')
#outputLabel.place(x=530, y=50)
outputLabel.place(x=527, y=70)
#------------------------------------------------------------------------------------------------------

################################ Translator Window Input/Output Fields ################################
inputBox = scrolledtext.ScrolledText(window, width=30, height=10, font=('calibri',15), wrap='word') 
inputBox.grid(column = 0, pady = 10, padx = 10)
inputBox.place(x=15, y=120)
inputBox.focus()

outputBox = scrolledtext.ScrolledText(window, width=30, height=10, font=('calibri',15), wrap='word', bg='grey85', state='disabled') 
outputBox.grid(column = 0, pady = 10, padx = 10)
outputBox.place(x=500, y=120)
#------------------------------------------------------------------------------------------------------

###################################### Translator Window Buttons ######################################
TranslateButton = Button(window, text='Translate >>', font=('Helvetica',15), width=10, command=translation, relief='raised')
TranslateButton.place(x=350, y=300)

ExitButton = Button(window, text='Exit', font=('Helvetica',10), width=4, command=main_exit, relief='raised')
ExitButton.place(x=390, y=400)
#------------------------------------------------------------------------------------------------------


######################################### Languages Combo Box #########################################
languages={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 
'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 
'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 
'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
selectedLanguage=StringVar()
languageBox = Combobox(window, font=('Helvetica',11), width=16, textvariable=selectedLanguage, state='readonly')
languageBox['values'] = [e for e in languages.keys()]
languageBox.current(37)
languageBox.place(x=335, y=250)
#------------------------------------------------------------------------------------------------------

window.mainloop()