import random
import pyttsx3
import tkinter as tk

# Define the text to be used in each language
paragraphs = {
    "French": "Le ciel est bleu. Les oiseaux chantent dans les arbres. C'est une belle journée.",
    "Spanish": "El cielo está azul. Los pájaros cantan en los árboles. Es un día hermoso.",
    "German": "Der Himmel ist blau. Die Vögel singen in den Bäumen. Es ist ein schöner Tag.",
    "Japanese": "空は青いです。鳥は木々で歌います。今日はいい天気です。",
    "Chinese": "天空是蓝色的。鸟儿在树上唱歌。今天是美好的一天。",
    "Italian": "Il cielo è blu. Gli uccelli cantano nei rami. È una bella giornata.",
}

# Define the engine for text-to-speech
engine = pyttsx3.init()

# Define the function to read out the paragraph with adjustable speed
def read_paragraph(paragraph, speed):
    # Set the engine properties for speed
    rate = engine.getProperty('rate')
    engine.setProperty('rate', speed)
    # Read out the paragraph
    engine.say(paragraph)
    engine.runAndWait()

# Define the function to handle the button click
def button_click():
    # Get the selected language and paragraph from the dropdown menus
    selected_language = language_var.get()
    selected_paragraph = str(paragraph_var.get())
    # Get the speed value from the scale
    speed = speed_scale.get()
    # Read out the selected paragraph with the selected speed
    read_paragraph(paragraphs[selected_language][selected_paragraph], speed)

# Create the GUI window
window = tk.Tk()
window.title('Sonify')
window.geometry('400x300')
window.configure(bg='#3399FF')

# Create the language dropdown menu
language_label = tk.Label(window, text='Select a language:', bg='#3399FF', fg='white')
language_label.pack(pady=10)
language_var = tk.StringVar()
language_dropdown = tk.OptionMenu(window, language_var, *paragraphs.keys(), command=lambda _: update_paragraph_dropdown())
language_dropdown.pack()

# Create the paragraph dropdown menu
paragraph_label = tk.Label(window, text='Select a paragraph:', bg='#3399FF', fg='white')
paragraph_label.pack(pady=10)
paragraph_var = tk.StringVar()
paragraph_dropdown = tk.OptionMenu(window, paragraph_var, *range(len(paragraphs[language_var.get()])))
paragraph_dropdown.pack()

# Create the speed scale
speed_label = tk.Label(window, text='Adjust speed:', bg='#3399FF', fg='white')
speed_label.pack(pady=10)
speed_scale = tk.Scale(window, from_=50, to=250, orient='horizontal', length=200)
speed_scale.pack()

# Create the read button
read_button = tk.Button(window, text='Read Paragraph', command=button_click, bg='#FFD633', fg='white')
read_button.pack(pady=20)

# Run the GUI window
window.mainloop()
