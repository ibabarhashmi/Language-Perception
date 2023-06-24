from tkinter import *
from tkinter import ttk
from langdetect import detect
from googletrans import Translator, LANGUAGES

translator = Translator(service_urls=['translate.google.com'], user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')


def detect_language():
    input_text = Input_text.get(1.0, END).strip()
    print(input_text)
    print(detect)
    if input_text:
        detected_lang = detect(input_text)
        print(detected_lang)
        print(LANGUAGES.get(detected_lang, 'auto'))
        if(LANGUAGES.get(detected_lang, 'auto') == 'dutch'):
            Output_text.insert(END, 'English')
            return
        Output_text.insert(END,LANGUAGES.get(detected_lang, 'auto') )
        return LANGUAGES.get(detected_lang, 'auto')
    
    return 'auto'

def translate():
    translator = Translator()
    input_text = Input_text.get(1.0, END).strip()
    if input_text:
        src_language = src_lang.get()
        dest_language = dest_lang.get()
        
        if src_language == 'auto':
            src_language = detect_language()
        if dest_language == 'auto':
            dest_language = detect_language()
            
        translated = translator.translate(text=input_text, src=src_language, dest=dest_language)
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.title("LANGUAGE PERCEPTION")

# Background image
background_image = PhotoImage(file="D:\\Project\\background_image.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Heading
Label(root, text="* 언어-ಭಾಷೆ -语言- لغة-שפה *", font="Georgia 20 bold", bg='white smoke').pack()
Label(root, text="1MJ20AI009", font='Georgia 15 bold', bg='white smoke', width='10').pack(side='bottom')

# Input and Output Text Widgets
Label(root, text="Input Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)
Input_text = Text(root, font='Constantia 15', height=10.2, wrap=WORD, padx=5, pady=5, width=40)
Input_text.place(x=30, y=100)

Label(root, text="Output Text", font='arial 13 bold', bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='Constantia 15 bold', height=10.2, wrap=WORD, padx=5, pady=5, width=35)
Output_text.place(x=600, y=100)

# Language Selection Comboboxes
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values=language, width=22)
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('choose output language')

# Translate Button
trans_btn = Button(root, text='Translate', font='Georgia 12 bold', pady=5, command=translate, bg='yellow', activebackground='sky blue')
trans_btn.place(x=490, y=180)

# Language Detection Button
detect_btn = Button(root, text='Not Sure?', font='Georgia 10 bold', pady=5, command=detect_language, bg='white', activebackground='white smoke')
detect_btn.place(x=495, y=230)  

root.mainloop()
