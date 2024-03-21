from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd 
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
import matplotlib.figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from collections import OrderedDict
filename_train = 'train.csv'
filename=None
ErrorrateMeans=list()
AccuracyMeans=list()
class LoginPage:


    def __init__(self, window):
        



        def main():
            def show_predicted_label(label):
                if label == 1:
                    messagebox.showerror('FAKE','Our system suggests this might be a FAKE Account')
                else:
                    messagebox.showinfo('REAL!','Our system suggests this might be a REAL Account')

            def Linear_Svc_Manual_Input ():
                print("here")
                if e1 :
                    inputframe =pd.DataFrame(
                    OrderedDict(
                    {
                    'profilepic':[e10.get()],
                    'nums/length username':[e9.get()],
                    'fullname words':[e8.get()],
                    'nums/length fullname':[e7.get()],
                    'name=username':[e6.get()],
                    'description length':[e5.get()],
                    'external URL':[e4.get()],
                    'private':[e2.get()],
                    '#posts':[e1.get()],
                    '#followers':[e0.get()],
                    '#follows':[e4.get()]}))
                    inputframe = inputframe[['profilepic','nums/length username','fullname words','nums/length fullname','name=username','description length','external URL','private','#posts','#followers','#follows']]
                    print(inputframe.loc[0])
                
                df=pd.read_csv(filename_train)
                train = df
                test = inputframe
                features = train.values[:,0:10]
                testing_data = test.values[:,0:10]
                labels = train.values[:,11].astype("int")
                model2 = LinearSVC()
                model2.fit(features,labels)
                predictions_model2 = model2.predict(testing_data)
                
                print('2.Linear SVC :\n')
                print('\n Predicted Class :',predictions_model2[0])
                show_predicted_label(predictions_model2[0])
                    
                    
            def Naive_Bayes_Manual_Input ():
                print("here")
                
                if e1 :
                    inputframe =pd.DataFrame(
                    OrderedDict(
                    {
                    'profilepic':[e10.get()],
                    'nums/length username':[e9.get()],
                    'fullname words':[e8.get()],
                    'nums/length fullname':[e7.get()],
                    'name=username':[e6.get()],
                    'description length':[e5.get()],
                    'external URL':[e4.get()],
                    'private':[e2.get()],
                    '#posts':[e1.get()],
                    '#followers':[e0.get()],
                    '#follows':[e4.get()]}))
                    inputframe = inputframe[['profilepic','nums/length username','fullname words','nums/length fullname','name=username','description length','external URL','private','#posts','#followers','#follows']]
                    print(inputframe.loc[0])
                    
                df=pd.read_csv(filename_train) 
                train = df
                test = inputframe
                features = train.values[:,0:10]
                testing_data = test.values[:,0:10]
                labels = train.values[:,11].astype("int")

                model1 = MultinomialNB()
                model1.fit(features,labels)
                predictions_model1 = model1.predict(testing_data)
                
                print('\n1.Multinomial Naive Bayes :\n')
                print('\n Predicted Class :',predictions_model1[0])
                show_predicted_label(predictions_model1[0])		
                    
            def Knn__Manual_Input():
                print("here")
                
                if e1 :
                    inputframe =pd.DataFrame(
                    OrderedDict(
                    {
                    'profilepic':[e10.get()],
                    'nums/length username':[e9.get()],
                    'fullname words':[e8.get()],
                    'nums/length fullname':[e7.get()],
                    'name=username':[e6.get()],
                    'description length':[e5.get()],
                    'external URL':[e4.get()],
                    'private':[e2.get()],
                    '#posts':[e1.get()],
                    '#followers':[e0.get()],
                    '#follows':[e4.get()]}))
                    inputframe = inputframe[['profilepic','nums/length username','fullname words','nums/length fullname','name=username','description length','external URL','private','#posts','#followers','#follows']]
                    print(inputframe.loc[0])
                
                df=pd.read_csv(filename_train) 
                train = df
                test = inputframe
                features = train.values[:,0:10]
                testing_data = test.values[:,0:10]
                labels = train.values[:,11].astype("int")
                model3 = KNeighborsClassifier(n_neighbors=3)
                model3.fit(features,labels)
                predictions_model3 = model3.predict(testing_data)
                print('3.K-Nearest Neighbors  :\n')
                print('\n Predicted Class :',predictions_model3[0])
                show_predicted_label(predictions_model3[0])	

            self.window.destroy()
            window = Tk()

            window.geometry("1440x1113")
            window.configure(bg = "#000000")
            canvas = Canvas(
                window,
                bg = "#000000",
                height = 1113,
                width = 1440,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)

            background_img = PhotoImage(file = f"./images/background.png")
            background = canvas.create_image(
                720.0, 556.5,
                image=background_img)

            img0 = PhotoImage(file = f"./images/img0.png")
            b0 = Button(
                image = img0,
                borderwidth = 0,
                highlightthickness = 0,
                command = Linear_Svc_Manual_Input,
                relief = "flat")

            b0.place(
                x = 834, y = 966,
                width = 212,
                height = 77)

            img1 = PhotoImage(file = f"./images/img1.png")
            b1 = Button(
                image = img1,
                borderwidth = 0,
                highlightthickness = 0,
                command = Naive_Bayes_Manual_Input,
                relief = "flat")

            b1.place(
                x = 614, y = 966,
                width = 212,
                height = 77)

            img2 = PhotoImage(file = f"./images/img2.png")
            b2 = Button(
                image = img2,
                borderwidth = 0,
                highlightthickness = 0,
                command = Knn__Manual_Input,
                relief = "flat")

            b2.place(
                x = 394, y = 966,
                width = 212,
                height = 77)

            entry0_img = PhotoImage(file = f"./images/img_textBox0.png")
            entry0_bg = canvas.create_image(
                1029.5, 803.5,
                image = entry0_img)

            e0 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e0.place(
                x = 747, y = 788,
                width = 565,
                height = 29)

            entry1_img = PhotoImage(file = f"./images/img_textBox1.png")
            entry1_bg = canvas.create_image(
                1029.5, 683.5,
                image = entry1_img)

            e1 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e1.place(
                x = 747, y = 668,
                width = 565,
                height = 29)

            entry2_img = PhotoImage(file = f"./images/img_textBox2.png")
            entry2_bg = canvas.create_image(
                1029.5, 563.5,
                image = entry2_img)

            e2 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e2.place(
                x = 747, y = 548,
                width = 565,
                height = 29)

            entry3_img = PhotoImage(file = f"./images/img_textBox3.png")
            entry3_bg = canvas.create_image(
                1029.5, 443.5,
                image = entry3_img)

            e3 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e3.place(
                x = 747, y = 428,
                width = 565,
                height = 29)

            entry4_img = PhotoImage(file = f"./images/img_textBox4.png")
            entry4_bg = canvas.create_image(
                719.5, 917.0,
                image = entry4_img)

            e4 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e4.place(
                x = 491, y = 903,
                width = 457,
                height = 26)

            entry5_img = PhotoImage(file = f"./images/img_textBox5.png")
            entry5_bg = canvas.create_image(
                1029.5, 323.5,
                image = entry5_img)

            e5 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e5.place(
                x = 747, y = 308,
                width = 565,
                height = 29)

            entry6_img = PhotoImage(file = f"./images/img_textBox6.png")
            entry6_bg = canvas.create_image(
                388.5, 803.5,
                image = entry6_img)

            e6 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e6.place(
                x = 106, y = 788,
                width = 565,
                height = 29)

            entry7_img = PhotoImage(file = f"./images/img_textBox7.png")
            entry7_bg = canvas.create_image(
                388.5, 683.5,
                image = entry7_img)

            e7 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e7.place(
                x = 106, y = 668,
                width = 565,
                height = 29)

            entry8_img = PhotoImage(file = f"./images/img_textBox8.png")
            entry8_bg = canvas.create_image(
                388.5, 563.5,
                image = entry8_img)

            e8 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e8.place(
                x = 106, y = 548,
                width = 565,
                height = 29)

            entry9_img = PhotoImage(file = f"./images/img_textBox9.png")
            entry9_bg = canvas.create_image(
                388.5, 443.5,
                image = entry9_img)

            e9 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e9.place(
                x = 106, y = 428,
                width = 565,
                height = 29)

            entry10_img = PhotoImage(file = f"./images/img_textBox10.png")
            entry10_bg = canvas.create_image(
                388.5, 323.5,
                image = entry10_img)

            e10 = Entry(
                bd = 0,
                bg = "#d9d9d9",
                highlightthickness = 0)

            e10.place(
                x = 106, y = 308,
                width = 565,
                height = 29)
            window.resizable(False, False)
            window.title('Manual Input')
            window.mainloop()

        #------------------------------------------------------
        def browse() :
            Tk().withdraw()
            global filename
            filename = askopenfilename()
            if filename:
                messagebox.showinfo('New Message!','File Uploaded!')
            

        #------------------others-----------------------------------

        def Naive_Bayes():
            if filename:
                global AccuracyMeans,ErrorrateMeans
                df1=pd.read_csv(filename_train) 
                df2=pd.read_csv(filename) 
                train = df1
                test = df2
                features = train.values[:,0:10]
                testing_data = test.values[:,0:10]
                labels = train.values[:,11].astype("int")
                testing_data_labels = test.values[:,11]

                model1 = MultinomialNB()
                model1.fit(features,labels)
                predictions_model1 = model1.predict(testing_data)
                
                accuracy=accuracy_score(testing_data_labels, predictions_model1)*100
                AccuracyMeans.append(accuracy)
                error_rate=100-accuracy
                ErrorrateMeans.append(error_rate)
                precision=precision_score(testing_data_labels, predictions_model1)*100
                recall=recall_score(testing_data_labels, predictions_model1)*100
                
                print('\n1.Multinomial Naive Bayes :\n')
                print('Confusion Matrix :')
                print(confusion_matrix(testing_data_labels, predictions_model1)) 
                print('Accuracy Is : '+str(accuracy )+' %')
                print('Error Rate Is : '+str(error_rate)+' %')
                print('Precision Is : '+str(precision)+' %')
                print('Recall Is : '+str(recall)+' %\n\n')

                labels = ['Error Rate', 'Accuracy ']
                sizes = [error_rate,accuracy]
                explode = (0, 0.1)  
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90) 
                plt.title('Naive Bayes Algorithm')
                ax1.axis('equal')  
                plt.tight_layout()
                plt.show()

            else:
                messagebox.showwarning('#ErrorSB404', 'Choose a file boii!!')

        def Linear_Svc():
            if filename:
                global AccuracyMeans,ErrorrateMeans
                df1=pd.read_csv(filename_train) 
                df2=pd.read_csv(filename) 
                train = df1
                test = df2
                features = train.values[:,0:10]
                labels = train.values[:,11].astype("int")
                testing_data = test.values[:,0:10]
                testing_data_labels = test.values[:,11]
                model2 = LinearSVC()
                model2.fit(features,labels)
                predictions_model2 = model2.predict(testing_data)
                
                accuracy=accuracy_score(testing_data_labels, predictions_model2)*100
                AccuracyMeans.append(accuracy)
                error_rate=100-accuracy
                ErrorrateMeans.append(error_rate)
                precision=precision_score(testing_data_labels, predictions_model2)*100
                recall=recall_score(testing_data_labels, predictions_model2)*100
                
                print('2.Linear SVC :\n')
                print('Confusion Matrix :')
                print(confusion_matrix(testing_data_labels, predictions_model2)) 
                print('Accuracy Is : '+str(accuracy )+' %')
                print('Error Rate Is : '+str(error_rate)+' %')
                print('Precision Is : '+str(precision)+' %')
                print('Recall Is : '+str(recall)+' %\n\n')

                labels = ['Error Rate', 'Accuracy ']
                sizes = [error_rate,accuracy]
                explode = (0, 0.1)  
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90) 

                plt.title('Linear SVC Algorithm')
                ax1.axis('equal')  
                plt.tight_layout()
                plt.show()

            else:
                messagebox.showwarning('#ErrorSB404', 'Choose a file boii!!')
                
                
        def Knn():
            if filename:
                global AccuracyMeans,ErrorrateMeans
                df1=pd.read_csv(filename_train) 
                df2=pd.read_csv(filename) 
                train = df1
                test = df2
                features = train.values[:,0:10]
                labels = train.values[:,11].astype("int")
                testing_data = test.values[:,0:10]
                testing_data_labels = test.values[:,11]

                model3 = KNeighborsClassifier(n_neighbors=3)
                model3.fit(features,labels)
                predictions_model3 = model3.predict(testing_data)
            
                accuracy=accuracy_score(testing_data_labels, predictions_model3)*100
                AccuracyMeans.append(accuracy)
                error_rate=100-accuracy
                ErrorrateMeans.append(error_rate)
                precision=precision_score(testing_data_labels, predictions_model3)*100
                recall=recall_score(testing_data_labels, predictions_model3)*100
                
                print('3.K-Nearest Neighbors  :\n')
                print('Confusion Matrix :')
                print(confusion_matrix(testing_data_labels, predictions_model3)) 
                print('Accuracy Is : '+str(accuracy )+' %')
                print('Error Rate Is : '+str(error_rate)+' %')
                print('Precision Is : '+str(precision)+' %')
                print('Recall Is : '+str(recall)+' %\n\n')

                labels = ['Error Rate', 'Accuracy ']
                sizes = [error_rate,accuracy]

                explode = (0, 0.1)  
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90) 

                plt.title('KNN Algorithm')
                ax1.axis('equal')  
                plt.tight_layout()
                plt.show()

            else:
                messagebox.showwarning('#ErrorSB404', 'Choose a file boii!!')

        self.window = window
        self.window.geometry('1440x1113')
        self.window.resizable(0, 0)
        self.window.title('Main Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('./images/mainscr.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(width=1440,height=1113)

        # ========================================================================
        # ============================choose file button================================
        # =======================================================================

        self.admin = Button(self.window, text='Choose File', font=("poppins", 13,"bold"), width=18, bd=0,
                            bg='#42b0ff', cursor='hand2', activebackground='#42b0ff', fg='black',command=browse)
        self.admin.place(relx=0.423, rely=0.255)

         # ========================================================================
        # ============================NAIVE BAYES button================================
        # ========================================================================

        self.doc = Button(self.window, text='Naive Bayes', font=("poppins", 13, "bold"), width=14, height=1, bd=0,
                            bg='#141414', cursor='hand2', activebackground='#141414', fg='white',command=Naive_Bayes)
        self.doc.place(relx=0.44, rely=0.674)

        
        # ========================================================================
        # ============================KNN button================================
        # ========================================================================

        def recepf():
            self.window.destroy()

        self.recep = Button(self.window, text='KNN', font=("poppins", 13, "bold"), width=14, height=1, bd=0,
                            bg='#141414', cursor='hand2', activebackground='#141414', fg='white',command=Knn)
        self.recep.place(relx=0.286, rely=0.674)

        # ========================================================================
        # ============================LINEAR SVC button================================
        # ========================================================================

        def recepf():
            self.window.destroy()

        self.recep = Button(self.window, text='Linear SVC', font=("poppins", 13, "bold"), width=14, height=1, bd=0,
                            bg='#141414', cursor='hand2', activebackground='#141414', fg='white',command=Linear_Svc)
        self.recep.place(relx=0.591, rely=0.674)

        #=========== MANUAL INPUT ==================================================

        self.back_button_label = Button(self.window, text="Give Manual Input", font=("POPPINS", 13, "bold"), bg='black', cursor="hand2",
                                          borderwidth=0, background="#141414", activebackground="black", fg="white",command=main)
        self.back_button_label.place(relx=0.435, rely=0.345, width=200, height=25)
   
def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
