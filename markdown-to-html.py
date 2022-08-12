import markdown
from tkinter import *
from tkinter import StringVar, ttk, filedialog
from tkinter import messagebox as mbox

#GLOBAL VARIABLES: 

fileInPath= ""
fileOutPath= ""
fileLocation = ""


# FUNCTIONS

## Open file
def inputFile():
    statusLabel.configure(text="")
    dialogFileIn = filedialog.askopenfilename(initialdir="./", title = "Select .md file",
                                            filetypes=(("Markdown files", "*.md"), ("all files", "*.*")))

    inOpenedLabel.configure(text=dialogFileIn)

    print(dialogFileIn)

    global fileInPath  
    fileInPath = "/"+str(dialogFileIn)
    return 

## Output file
def outputFile():
    statusLabel.configure(text="")

    dialogFileOut = filedialog.asksaveasfile(initialdir="./", title="Select where to save file",
                                            filetypes=(("Html files", "*.html"), ("all files", "*.*")))
    
    outOpenedLabel.configure(text=dialogFileOut.name)

    global fileOutPath 
    fileOutPath = dialogFileOut.name
    

#Convert file 
def convertFile(inFilename, outFilename):

    global fileInPath
    global fileOutPath
    global fileLocation

    if inFilename == "" or outFilename == "":
        print("Input or output file missing!")
        statusLabel.configure(text="Input or output file missing!", fg="red")

    else:
            ##Open input file
        with open(inFilename, 'r') as input_file:
            text = input_file.read()

        html = markdown.markdown(text)
        print(html)

        with open(outFilename, 'w') as output_file:
            output_file.write(html)
        print("file converted!")
        statusLabel.configure(text="File Converted to HTML", fg="black")
        
        fileLocation = fileOutPath
        fileInPath = ""
        fileOutPath = ""
        inOpenedLabel.configure(text="")
        outOpenedLabel.configure(text="")
        filePopup()

#File convert popup

def filePopup():
    global fileLocation
    mbox.showinfo(title="File convert Success!", message="You have converted file: " + fileLocation)



#WINDOW

#Create root ikkuna
root = Tk()
root.title("Md to HTML")
root.geometry('800x200')
root.resizable(0,0)

#Configure grid:
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=3)

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

## Status label
statusLabel = Label(root, text="")
statusLabel.grid(column=1, row=3, sticky=S)

#Buttons:

##BrowseFiles
buttonInputFile = Button(root,
                            text="Browse Files",
                            command=inputFile,
                            width=10,
                            height=1)

buttonInputFile.grid(column=2, row=0)


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
buttonConvertFile.grid(column=1, row=2, sticky=S)






root.mainloop()