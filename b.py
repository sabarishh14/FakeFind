from tkinter import *
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
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

