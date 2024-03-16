import tkinter as tk
import PyPDF2 
from PIL import Image, ImageTk
## PIL aka a pillo
from tkinter.filedialog import askopenfile

## print("This is my First program which is working fine!!") 

## Creating a windpw/root object with Tkinter
root = tk.Tk()  ## begining of the interface 

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

## logo 
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image= logo)
logo_label.image = logo ## important line
logo_label.grid(column=1, row=0)
 
## instructions 

instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)


## Add command function to button widget 
def open_file():
    browser_text.set("loading...")            ### print("It's Working Bro!!")
    ## limit file Dialogue to browser only for PDF files
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf= PyPDF2.PdfFileReader(file)    ## print("file sucessfully loaded")
        page = read_pdf.getPage(0)
        page_content = page.extractText()  ## extract file from the file 
        print(page_content)


        ## text box
        ## inserting text into a text widget 
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center",justify="center")  # justify widget text to the center 
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        ## testing the app
        browser_text.set("Browse")

##  browsing button 
browser_text = tk.StringVar()                ###font="Raleway", bg="#20bebe", fg="white", height=2, width=2 === used for styling the button widget
browser_btn = tk.Button(root, textvariable=browser_text,command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browser_text.set("Browse")
browser_btn.grid(column=1, row=2)

## adding vertical margins in Tkinter
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)


  
root.mainloop()  ## ending of the interface