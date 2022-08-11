import markdown
from tkinter import *
from tkinter import StringVar, ttk, filedialog

#FUNCTIONS: 

fileInPath= ""
fileOutPath= ""

## Open file
def browseFiles():
    filename_in = filedialog.askopenfilename(initialdir="./", title = "Select .md file",
                                            filetypes=(("Markdown files", "*.md"), ("all files", "*.*")))

    inOpenedLabel.configure(text=filename_in)

    print(filename_in)

    global fileInPath  
    fileInPath = str(filename_in)

    
    return 
## Output file
def outputFile():
    filename_out = filedialog.asksaveasfile(initialdir="./", title="Select where to save file",
                                            filetypes=(("Html files", "*.html"), ("all files", "*.*")))
    
    outOpenedLabel.configure(text=filename_out.name)

    global fileOutPath 
    fileOutPath = filename_out.name
    

#Convert file 
def convertFile(inFilename, outFilename):

        ##Open input file
    with open(inFilename, 'r') as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    print(html)

    with open(outFilename, 'w') as output_file:
        output_file.write(html)
    print("file converted!")



#WINDOW

#Luodaan root ikkuna
root = Tk()
root.title("Md to HTML")
root.geometry('600x200')
root.resizable(0,0)

#Configure grid:
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=2)

##INPUT FILE
#File path 
inFilepathLabel = ttk.Label(root, text="Filepath:")
inFilepathLabel.grid(column=0, row=0, sticky=W, padx=10, pady=15)

# Filepath label(opened)
inOpenedLabel = Label(root, text="")
inOpenedLabel.grid(column=1, row=0, sticky=W)

##OUTPUT FILE
outFilepathLabel = ttk.Label(root, text="Output path:")
outFilepathLabel.grid(column=0, row=1, sticky=W, padx=10, pady=5)

## output filepath (opened)
outOpenedLabel= Label(root, text="")
outOpenedLabel.grid(column=1, row=1, sticky=W)

#Buttons:
buttonBrowseFiles = Button(root,
                            text="Browse Files",
                            command=browseFiles,
                            width=10,
                            height=1)

buttonBrowseFiles.grid(column=2, row=0)


## output file
buttonOutputFile = Button(root,
                            text="Save as",
                            command=outputFile,
                            width=10,
                            height=1
                            )
buttonOutputFile.grid(column=2, row=1)

##Convert file
buttonConvertFile = Button(root,
                            text="Convert to HTML",
                            command=lambda: convertFile(fileInPath, fileOutPath),
                            width=40,
                            height=2)
buttonConvertFile.grid(column=1, row=2)






root.mainloop()