## Import Required Packages
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

## Declaration of Global Variables
global flag1,flag2

## Function to Create GUI for Embedding - GrayScale
def createGrayScaleEmbedGUI():
    ## Function to Close Window
    def close_window():
        if ((textbox_input.get("1.0", "end-1c")) != " ")  and (dropdownbox_input.current() != -1):
            pass
            #gui_window.destroy()  # Close the window
        else:
            messagebox.showerror("Error", "Secret Message or Grayscale Selection CANNOT be Empty!!")
    ## Function to Save to a File
    def saveToFile():
        flag1 = flag2 = 0
        global secret_message,grayscale_cover_image
        ## Get Secret Message Input
        secret_message = textbox_input.get('1.0',END)   #"1.0" means that the input should be read from line one, character zero (ie: the very first character). END is an imported constant which is set to the string "end". The END part means to read until the end of the text box is reached.
        ## Get GrayScale Cover Image Input
        grayscale_cover_image = dropdownbox_input.get()
        if not secret_message.strip():
        ## Throw Error Pop-Up
            messagebox.showerror("Error", "Secret Message cannot be Empty.")
            flag1 = 1
        if not grayscale_cover_image.strip():
        ## Throw Error Pop-Up
            messagebox.showerror("Error", "Select any GrayScale Cover Image.")
            flag2 = 1
        ## Open a Text File in Write Mode and Write the Option Selected from the Drop Down Box to the File
        with open("GrayScale Cover Image Selected.txt","w") as img_file:
            img_file.write(f"{grayscale_cover_image}")
        ## Open a Text File in Write Mode and Write the Input taken from the Text Box to the File
        with open("emb_input.txt", "w") as file:
            file.write(secret_message.replace('\n', ''))

        if flag1 == 0  and flag2 == 0:
            gui_window.destroy()

    ## Create GUI Window
    gui_window = Tk()
    gui_window.protocol("WM_DELETE_WINDOW", close_window)
    gui_window.title('Patient Details(Embedding) - GrayScale')
    gui_window.geometry("900x400")

    ## Create the Input Fields
    ## Text Box Creation
    textbox_label = Label(gui_window, text='Secret Message  :',font=("Times New Roman", 15))
    textbox_input = Text(gui_window,width = 30,height=6)
    textbox_input.pack() #pack() -  Used to Make a Widget Fill the Entire Frame
    textbox_label.place(x=20,y=70)
    textbox_input.place(x=170,y=73)
    ## Drop Down Box Creation
    dropdownbox_label = Label(gui_window, text='Grayscale Cover Image :' ,font=("Times New Roman", 15))
    dropdownbox_options = ['Lena_512_8bit.jpg','Baboon_512_8bit.jpg','Barbara_512_8bit.jpg','Goldhill_512_8bit.jpg','Pepper_512_8bit.jpg','Sailboat_512_8bit.jpg'] # create a list of options
    dropdownbox_input = Combobox(gui_window, values=dropdownbox_options ,font=("Times New Roman", 15), width = 20) #combobox - Create a Drop-Down Box with the List of Options
    dropdownbox_input.pack()
    dropdownbox_label.place(x=440,y=70)
    dropdownbox_input.place(x=650,y=73)
    ## Button Creation
    button_label = Button(gui_window, text="EMBED", font = ("Times New Roman", 15),command=saveToFile,width = 20,height = 2)
    button_label.place(x= 330,y=250)

    ## Running The GUI
    gui_window.mainloop()

#createGrayScaleEmbedGUI()