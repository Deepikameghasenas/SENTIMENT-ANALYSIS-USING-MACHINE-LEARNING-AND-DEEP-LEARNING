import pandas as pd 
from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox as msg 
from pandastable import Table 
from tkintertable import TableCanvas 


class csv_to_excel: 

    def __init__(self, root): 

        self.root = root 
        self.file_name = '' 
        self.f = Frame(self.root, 
                    height = 200, 
                    width = 300) 
        
        # Place the frame on root window 
        self.f.pack() 
        
        # Creating label widgets 
        self.message_label = Label(self.f, 
                                text = 'Welcome to sentiment analysis', 
                                font = ('Arial', 19,'underline'), 
                                fg = 'Green') 
        self.message_label2 = Label(self.f, 
                                    text = 'Text Analysis', 
                                    font = ('Arial', 14,'underline'), 
                                    fg = 'Red') 

        # Buttons 
        self.convert_button = Button(self.f, 
                                    text = 'Browse', 
                                    font = ('Arial', 14), 
                                    bg = 'Orange', 
                                    fg = 'Black', 
                                    command = self.convert_csv_to_xls) 
        self.display_button = Button(self.f, 
                                    text = 'Display', 
                                    font = ('Arial', 14), 
                                    bg = 'Green', 
                                    fg = 'Black', 
                                    command = self.display_xls_file)
        self.analysis_button = Button(self.f, 
                                    text = 'Analysis', 
                                    font = ('Arial', 14), 
                                    bg = 'Green', 
                                    fg = 'Black', 
                                    command = self.analysis)
        self.resultView_button = Button(self.f, 
                                    text = 'Result View', 
                                    font = ('Arial', 14), 
                                    bg = 'Green', 
                                    fg = 'Black', 
                                    command = self.resultView_button)
        self.exit_button = Button(self.f, 
                                text = 'Exit', 
                                font = ('Arial', 14), 
                                bg = 'Red', 
                                fg = 'Black', 
                                command = root.destroy) 

        # Placing the widgets using grid manager 
        self.message_label.grid(row = 1, column = 1) 
        self.message_label2.grid(row = 2, column = 1) 
        self.convert_button.grid(row = 3, column = 0, 
                                padx = 0, pady = 15) 
        self.display_button.grid(row = 3, column = 1, 
                                padx = 10, pady = 15)
        self.analysis_button.grid(row = 3, column = 2, 
                                padx = 10, pady = 15)
        self.resultView_button.grid(row = 3, column = 3, 
                                padx = 10, pady = 15)
        self.exit_button.grid(row = 4, column = 3, 
                            padx = 10, pady = 15) 

    def convert_csv_to_xls(self):
        self.file_name = filedialog.askopenfilename(initialdir = '/Desktop', 
                                                        title = 'Select a CSV file', 
                                                        filetypes = (('csv file','*.csv'), 
                                                                    ('csv file','*.xls')))
        df = pd.read_csv(self.file_name,encoding='unicode_escape')
        if(len(df) == 0):
            msg.showinfo('No Rows Selected', 'CSV has no rows')
        else:
            df.to_csv("output.csv",index = False)
            msg.showinfo('Data file ceated', 'Data File created') 
##        try:
##            #import Extract_ML
##            self.file_name = 'dataset.csv' 
##            
##            df = pd.read_csv(self.file_name) 
##            
##            # Next - Pandas DF to Excel file on disk 
##            if(len(df) == 0):    
##                msg.showinfo('No Rows Selected', 'CSV has no rows') 
##            else: 
##                
##                # saves in the current directory 
##                with pd.ExcelWriter('op.xls') as writer: 
##                        df.to_excel(writer,'GFGSheet') 
##                        writer.save() 
##                        msg.showinfo('Data file ceated', 'Data File created')  
##            
##        except FileNotFoundError as e: 
##                msg.showerror('Error in opening file', e) 

    def display_xls_file(self): 
        try: 
            self.file_name = 'output.csv' 
            df = pd.read_csv(self.file_name) 
            
            if (len(df)== 0): 
                msg.showinfo('No records', 'No records') 
            else: 
                pass
                
            # Now display the DF in 'Table' object 
            # under'pandastable' module 
            self.f2 = Frame(self.root, height=200, width=300) 
            self.f2.pack(fill=BOTH,expand=1) 
            self.table = Table(self.f2, dataframe=df,read_only=True) 
            self.table.show() 
        
        except FileNotFoundError as e: 
            print(e) 
            msg.showerror('Error in opening file',e)
    def resultView_button(self): 
        try: 
            self.file_name = 'outputres.csv' 
            df = pd.read_csv(self.file_name) 
            
            if (len(df)== 0): 
                msg.showinfo('No records', 'No records') 
            else: 
                pass
                
            # Now display the DF in 'Table' object 
            # under'pandastable' module 
            self.f2 = Frame(self.root, height=200, width=300) 
            self.f2.pack(fill=BOTH,expand=1) 
            self.table = Table(self.f2, dataframe=df,read_only=True) 
            self.table.show() 
        
        except FileNotFoundError as e: 
            print(e) 
            msg.showerror('Error in opening file',e)
    def analysis(self): 
        import SentiMentAnalysis
        
       

# Driver Code 
root = Tk() 
root.title('Sentiment Analysis') 

obj = csv_to_excel(root) 
root.geometry('800x600') 
root.mainloop()
