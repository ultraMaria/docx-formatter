import tkinter as tk

from utils import create_document, process_config

file_path, fields = process_config()

def processContract(entries):
    info = {}
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        info[field] = text
    create_document(info, file_path)

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


root = tk.Tk()
#root.geometry("700x700")
root.title('Редактор документа')
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: processContract(e)))
b1 = tk.Button(root, text='Generate',
               command=(lambda e=ents: processContract(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b2 = tk.Button(root, text='Quit', command=root.quit)
b2.pack(side=tk.LEFT, padx=5, pady=5)
root.mainloop()
