from PyPDF2 import PdfFileMerger
from tkinter import *
import os


def merge(pdf_name):
    if not pdf_name:
        pdf_name = "archivo_combinado.pdf"
        
    pdfs = [pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
    pdfs = sorted(pdfs)

    if len(pdfs) == 0:
        print("No hay archivos")
        return

    if not pdf_name.endswith(".pdf"):
        pdf_name = pdf_name+".pdf"

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(open(pdf, "rb"))

    print(len(pdfs))
    print(pdfs)

    with open(pdf_name, "wb") as file:
        merger.write(file)


# TKINTER INICIO
window = Tk()
window.geometry("100x100")
window.title("Combinador PDF")

# Info
pdf_name = StringVar(window)

# Label
label = Label(window, text="Nombre del pdf")
label.grid(row=1, column=1)

# Button
button = Button(window, text="Combinar!", command=lambda: merge(pdf_name.get()))
button.grid(row=3, column=1)

# Entry
entry = Entry(window, textvariable=pdf_name)
entry.grid(row=2, column=1)

# Size
window.grid_columnconfigure(1)
window.grid_rowconfigure(3)

window.mainloop()
