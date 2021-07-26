import os
import img2pdf
import PIL
import tkinter as tk

from PIL import Image
from PIL import ImageOps
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter import filedialog as fd, messagebox
from pikepdf import _cpphelpers


root = tk.Tk()

root['bg'] = "#fafafa"
root.title("Программа для работы с PDF и JPG")
root.geometry("700x700")


def get_dir_name():
    global dir_name
    dir_name = fd.askdirectory(mustexist=True)
    dir_name = os.path.normpath(dir_name)
    return dir_name


def convert_jpf_to_pdf():
    dir_name = get_dir_name()
    os.chdir(dir_name)
    with open(f"Новый файл.pdf", "wb") as f:
        imgs = []
        for file_name in os.listdir(dir_name):
            if file_name.endswith(".jpg") or file_name.endswith(".JPG"):
                path = os.path.join(dir_name, file_name)
                imgs.append(path)
            else:
                continue
        try:
            f.write(img2pdf.convert(imgs))
            messagebox.showinfo(title="Сделано!", message='"Новый файл.pdf" создан в выбранной вами папке.')
        except Exception as e:
            print(e)
            messagebox.showerror(title="Ошибка", message="Не выбрана папка с файлами JPG")
            pass


def compress_jpg():
    dir_name = get_dir_name()
    if dir_name == ".":
        messagebox.showerror(title="Ошибка", message='Не выбрана папка с файлами JPG')
    else:
        for file_name in os.listdir(dir_name):
            if file_name.endswith(".jpg") or file_name.endswith(".JPG"):
                path = os.path.join(dir_name, file_name)
                img = PIL.Image.open(path)
                myHeight, myWidth = img.size
                img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
                img = ImageOps.exif_transpose(img)
                img.save(path)
            else:
                continue
        messagebox.showinfo(title="Сделано!", message='Файлы JPG сжаты в выбранной папке.')

def merge_pdf():
    dir_name = get_dir_name()
    if dir_name == ".":
        messagebox.showerror(title="Ошибка", message="Не выбрана папка с файлами PDF")
    else:
        os.chdir(dir_name)
        merger = PdfFileMerger()
        for file_name in os.listdir(dir_name):
            if not file_name.endswith(".pdf"):
                continue
            mergering_files = os.path.join(dir_name, file_name)
            merger.append(mergering_files)
        merger.write(f"Объединенный файл.pdf")
        merger.close()
        messagebox.showinfo(title="Сделано!", message='PDF файлы в выбранной папке объединены в "Объединенный файл.pdf".')


def jpg_to_pdf_compress():
    dir_name = get_dir_name()
    if dir_name == ".":
        messagebox.showerror(title="Ошибка", message='Не выбрана папка с файлами JPG')
    else:
        for file_name in os.listdir(dir_name):
            if file_name.endswith(".jpg") or file_name.endswith(".JPG"):
                path = os.path.join(dir_name, file_name)
                img = PIL.Image.open(path)
                myHeight, myWidth = img.size
                img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
                img = ImageOps.exif_transpose(img)
                img.save(path)
            else:
                continue

    os.chdir(dir_name)
    with open(f"Новый файл.pdf", "wb") as f:
        imgs = []
        for file_name in os.listdir(dir_name):
            if file_name.endswith(".jpg") or file_name.endswith(".JPG"):
                path = os.path.join(dir_name, file_name)
                imgs.append(path)
            else:
                continue
        try:
            f.write(img2pdf.convert(imgs))
            messagebox.showinfo(title="Сделано!", message='"Новый файл.pdf" создан в выбранной вами папке.')
        except:
            messagebox.showerror(title="Ошибка", message="Не выбрана папка с файлами JPG")
            pass


info_jpg_to_pdf = Label(root, text='Из JPG в PDF', bg='#fafafa', font=("Arial", 20)).pack()
info_jpg_to_pdf_1 = Label(root, text='Выберите папку с изображениями.\nПрограмма найдёт все файлы JPG в выбранной папке.\nФайл PDF с названием "Новый файл.pdf" сохранится в выбранной вами папке.', bg='#fafafa', font=("Arial", 10)).pack()
btn_jpg_to_pdf = Button(root, text='Выбрать папку', command=convert_jpf_to_pdf).pack()

info_jpg_to_pdf_compress = Label(root, text='\nИз JPG в PDF c уменьшенным размером файла ', bg='#fafafa', font=("Arial", 20)).pack()
info_jpg_to_pdf_compress_1 = Label(root, text='Выберите папку с изображениями.\nПрограмма найдёт все файлы JPG в выбранной папке.\nДанная операция сжимает все файлы JPG в папке.\nВозможно незначительное ухудшение качества изображений.\nФайл PDF с названием "Новый файл.pdf" сохранится в выбранной вами папке.', bg='#fafafa', font=("Arial", 10)).pack()
btn_jpg_to_pdf_compress = Button(root, text='Выбрать папку', command=jpg_to_pdf_compress).pack()

info_merge_pdf = Label(root, text='\nОбъединение PDF файлов', bg='#fafafa', font=("Arial", 20)).pack()
info_merge_pdf_1 = Label(root, text='Выберите папку с файлами PDF для объединения.\nПрограмма найдёт все файлы PDF в выбранной папке.\nОбъединенный файл c названием "Объединенный файл.pdf" сохранится в выбранной вами папке.', bg='#fafafa', font=("Arial", 10)).pack()
btn_merge_pdf = Button(root, text='Выбрать папку', command=merge_pdf).pack()

info_compress_jpg = Label(root, text='\nСжать JPG-файлы', bg='white', font=("Arial", 20)).pack()
info_compress_jpg_1 = Label(root, text='Выберите папку с изображениями.\nПрограмма найдёт все файлы JPG в выбранной папке.\nВозможно незначительное ухудшение качества изображений.', bg='#fafafa', font=("Arial", 10)).pack()
btn_compress_jpg = Button(root, text='Выбрать папку', command=compress_jpg).pack()

info_about_program = Label(root, text='\nИногда программа может зависнуть на какое-то время.\nЭто означает, что она выполняет ваши задачи.\nЭто зависит от размера обрабатываемых файлов и мощности вашего компьютера.\nВ любом случае, если что-то пошло не так, вы можете закрыть программу и заново её запустить.', bg='#fafafa', font=("Arial", 8)).pack()

if __name__ == '__main__':
    root.mainloop()





