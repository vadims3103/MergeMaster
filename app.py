from tkinter import *

class MergeMasterApp:
    def __init__(self, root):
        self.window = root
        self.window.title("MergeMaster")
        self.window.geometry("600x300")

        self.template_file_path = ""
        self.data_file_path = ""
        self.output_folder_path = ""

        self.draw_app_interface()
    
    def draw_app_interface(self):
        # Labels and button for Template file selection
        template_file_select_label = Label(self.window, text="Select Template File (.docx)")
        template_file_select_label.grid(column=0, row=0)

        template_file_select_button = Button(self.window, text="Select File")
        template_file_select_button.grid(column=1, row=0)

        self.template_file_name = Label(self.window, text="Template_File.docx", relief="flat", width=20)
        self.template_file_name.grid(column=2, row=0)

        # Labels and button for Data file selection
        data_file_select_label = Label(self.window, text="Select Data File (.xlsx)")
        data_file_select_label.grid(column=0, row=1)

        data_file_select_button = Button(self.window, text="Select File")
        data_file_select_button.grid(column=1, row=1)

        self.data_file_name = Label(self.window, text="Data_File.xslx", relief="flat", width=20)
        self.data_file_name.grid(column=2, row=1)

        # Labels and button for Output folder selection
        output_folder_select_label = Label(self.window, text="Select folder for saving merged files")
        output_folder_select_label.grid(column=0, row=2)

        output_folder_select_button = Button(self.window, text="Select Folder")
        output_folder_select_button.grid(column=1, row=2)

        self.output_folder_name = Label(self.window, text="/Downloads/Test_Folder")
        self.output_folder_name.grid(column=2, row=2)

        # Labels and input for naming merged files
        # TODO wrapping label information as template file can include a lot of keywords
        self.template_file_keyword_label = Label(self.window, text="The list of keywords used in the Template File: ${Name}, ${Surname}, ${Age}")
        self.template_file_keyword_label.grid(column=0, row=3, columnspan=3)

        # TODO label and input for naming output file names
        output_file_name_label = Label(self.window, text="Output file name:")
        output_file_name_label.grid(column=0, row=4)

        self.output_file_name = Entry(self.window, width=30)
        self.output_file_name.grid(column=1, row=4, columnspan=3)
        self.output_file_name.insert(0, "Template_File_${index}")

        # Error message and merge file button
        # TODO place for error information: if files and folder are not selected, data file do not include all keywords placed in template file
        # TODO button that stars process of merging files, it is not active if all files and folder are not selected
        self.error_message_label = Label(self.window, text="This is an error message that displays if something is not correct")
        self.error_message_label.grid(column=0, row=5, columnspan=2)

        merge_button = Button(self.window, text="Merge Files")
        merge_button.grid(column=2, row=5)


root = Tk()
app = MergeMasterApp(root)
root.mainloop()