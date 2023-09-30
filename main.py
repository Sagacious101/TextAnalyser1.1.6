import tkinter as tk
from tkinter import filedialog as fd
import tkinter.messagebox as mb
from tkinter.colorchooser import askcolor
from tkinter import ttk
import TextAnalyser


window = tk.Tk()
window.title('Text Analyser')
window.geometry('1920x1080')


# назначение функций
def create_checkbutton(parts_of_speech: list, grammemes: list) -> dict:
    for_parts_of_speech = {}
    row_check_buttom = len(packs)
    n = 1
    second_column = False
    for num in range(len(parts_of_speech)):
        for_parts_of_speech[parts_of_speech[num]] = tk.StringVar()
        n += 1
        if second_column:
            packs[parts_of_speech[num]] = [tk.Checkbutton(text=parts_of_speech[num], variable=for_parts_of_speech[parts_of_speech[num]], onvalue=grammemes[num], offvalue=''), (row_check_buttom, 1)]
        else:
            packs[parts_of_speech[num]] = [tk.Checkbutton(text=parts_of_speech[num], variable=for_parts_of_speech[parts_of_speech[num]], onvalue=grammemes[num], offvalue=''), (row_check_buttom, 0)]
        second_column = True
        if not n % 2 == 0:
            row_check_buttom += 1
            second_column = False

    return for_parts_of_speech


def checkbutton_morphy() -> list:
    parts_of_speech_checkbuttom = []
    for key in for_parts_of_speech.keys():
        if for_parts_of_speech[key].get():
            parts_of_speech_checkbuttom.append(for_parts_of_speech[key].get())
    return parts_of_speech_checkbuttom


def path_to_file():
    progressbar.grid(sticky='nw', padx=5)
    grammenes = checkbutton_morphy()
    try:
        if not packs['width_entry'][0].get().isdigit():
            raise Exception("Ошибка! Ширина картинки должна быть натуральным целым числом!")
        if not packs['height_entry'][0].get().isdigit():
            raise Exception("Ошибка! Высота картинки должна быть натуральным целым числом!")
        if not packs['file_name'][0]['text'][-4:] == '.txt':
            raise Exception("Ошибка! Выбранный вам файл должен быть формата txt!")
        destination_file = fd.asksaveasfile(mode='w', defaultextension='*.png', filetypes=[('PNG IMAGE', '*.png')])
        text_analyser = TextAnalyser.TextAnalyser(source_file=packs['file_name'][0]['text'], parts_of_speech=grammenes, wc_width=int(packs['width_entry'][0].get()), wc_height=int(packs['height_entry'][0].get()), destination_file=destination_file.name, wc_background=packs['color_canvas'][0]['bg'])
    except Exception as e:
        mb.showwarning(title="Error", message=e)
    packs['word_count'] = [tk.Label(text=f'Количество слов в этом тексте: {len(text_analyser.words)}', font=("Arial", 12)), (len(packs), 0)]
    packs['word_pos'] = [tk.Label(text=f'Количество слов выбранных частей речи: {len(text_analyser.pos_words)}', font=("Arial", 12)), (len(packs), 0)]
    for item in packs.items():
        item[1][0].grid(sticky='nw', padx=5, pady=3, row=item[1][1][0], column=item[1][1][1])
    global img
    img = tk.PhotoImage(file=destination_file.name)
    lable_worldcloud['image'] = img
    mb.showinfo(
        'Готово', 
        f'Картинка сохранена в {destination_file.name}' +
        f'\nСлов в тексте: {len(text_analyser.words)}' +
        f'\nСлов выбранный частей речи: {len(text_analyser.pos_words)}'
    )


def select_file():
    filename = fd.askopenfilename()
    if filename != '':
        packs['file_name'][0]['text'] = filename


def change_color():
    colors = askcolor(title="Выбор цвета фона")
    packs['color_canvas'][0]['bg'] = colors[1]


packs = {}
# ввод пути к файлу
packs['text_file_name'] = [tk.Label(text='Путь к файлу:', font=("Arial", 14)), (len(packs), 0)]
packs['file_name'] = [tk.Label(text='Не указан'), (len(packs), 0)]
packs['path_to_file_lable'] = [tk.Button(text='Выберете файл с текстом', command=select_file, font=("Arial", 11)), (len(packs), 0)]




# выбор частей речи

packs['morphy_lable'] = [tk.Label(text='Выберите части речи:', font=("Arial", 14)), (len(packs), 0)]
for_parts_of_speech = create_checkbutton([
    'Существительные',
    'Прилагательные(полное)',
    'Прилагательные(краткое)',
    'Компаративы',
    'Глаголы(личная форма)',
    'Глаголы(инфинитив)',
    'Причастия(полное)',
    'Причастия(кратко)',
    'Деепричастия',
    'Числительные',
    'Наречия',
    'Местоимения',
    'Предактивы',
    'Предлоги',
    'Союзы',
    'Частицы',
    'Междометия'
], [
    'NOUN',
    'ADJF',
    'ADJS',
    'COMP',
    'VERB',
    'INFN',
    'PRTF',
    'PRTS',
    'GRND',
    'NUMR',
    'ADVB',
    'NPRO',
    'PRED',
    'PREP',
    'CONJ',
    'PRCL',
    'INTJ'
])
packs['size_lable'] = [tk.Label(text='Размер:', font=("Arial", 14)), (len(packs), 0)]
packs['width'] = [tk.Label(text='Введите желаемую ширину картинки: ', font=("Arial", 12)), (len(packs), 0)]
packs['width_entry'] = [tk.Entry(), ((len(packs) - 1), 1)]
packs['height'] = [tk.Label(text='Введите желаемую высоту картинки: ', font=("Arial", 12)), (len(packs), 0)]
packs['height_entry'] = [tk.Entry(), ((len(packs) - 1), 1)]
packs['color_lable'] = [tk.Label(text='Цвет:', font=("Arial", 14)), (len(packs), 0)]
packs['color_canvas'] = [tk.Canvas(width=30, height=30, bg='#000000'), (len(packs), 0)]
packs['change_color_buttom'] = [tk.Button(text='Выбрать цвет фона', command=change_color), (len(packs), 0)]

packs['path_to_file_buttom'] = [tk.Button(text='Провести анализ текста', font=("Arial", 12), command=path_to_file), (len(packs), 0)]

for item in packs.items():
    item[1][0].grid(sticky='nw', padx=5, pady=2, row=item[1][1][0], column=item[1][1][1])
img = None
lable_worldcloud = tk.Label()
lable_worldcloud.grid(sticky='nw', column=2, row= 0, rowspan=len(packs))
progressbar = ttk.Progressbar(orient='horizontal', length=150, value=0, maximum=10)



window.mainloop()