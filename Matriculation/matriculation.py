"""Analyze Greenhill's College Matriculation"""

import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QGuiApplication
import PyQt5.QtCore as QtCore
import matplotlib.backends.backend_qt5agg as plt_backend
import sys
import functools

#change to ./ when uploading
#matr = pd.read_csv('/Users/sherryzhang/Desktop/Matr/GHMatr.csv')
matr = pd.read_csv('./GHMatr.csv')

def full_matr():
    """Filter Value Counts of All"""
    val_all = matr['School'].value_counts()
    return val_all

def full_gender():
    """Filter All Data by Gender"""
    female_all = matr['Gender'] == 'Female'
    male_all = matr['Gender'] == 'Male'

    female = matr[female_all]['School'].value_counts()
    male = matr[male_all]['School'].value_counts()

    return female, male

def ivy_league():
    """Filter by Ivy League"""
    ivy_check = matr['Ivy League'] == True
    ivy = matr[ivy_check]['School'].value_counts()
    return ivy

def ivy_gender():
    """Filter by Ivy League Gender"""

    ivy_check = matr['Ivy League'] == True
    female_ivy = matr['Gender'] == 'Female'
    male_ivy = matr['Gender'] == 'Male'

    female = matr[female_ivy & ivy_check]['School'].value_counts()
    male = matr[male_ivy & ivy_check]['School'].value_counts()

    return female, male

def state_schools():
    """Filter by State Schools"""
    state_check = matr['State'] == True
    state = matr[state_check]['School'].value_counts()
    return state

def state_gender():
    """Filter by State Schools Gender"""
    state_check = matr['State'] == True
    female_state = matr['Gender'] == 'Female'
    male_state = matr['Gender'] == 'Male'

    female = matr[female_state & state_check]['School'].value_counts()
    male = matr[male_state & state_check]['School'].value_counts()

    return female, male



def ivy_league_year(year):
    """Filter by Ivy League by Year"""
    ivy_check = matr['Ivy League'] == True
    year_check = matr['Year'] == year
    ivy = matr[ivy_check&year_check]['School'].value_counts()
    return ivy

def ivy_gender_year(year):
    """Filter by Ivy League Gender by Year"""

    ivy_check = matr['Ivy League'] == True
    year_check = matr['Year'] == year

    female_ivy = matr['Gender'] == 'Female'
    male_ivy = matr['Gender'] == 'Male'

    female = matr[female_ivy & ivy_check &year_check]['School'].value_counts()
    male = matr[male_ivy & ivy_check&year_check]['School'].value_counts()

    return female, male

def state_schools_year(year):
    """Filter by State Schools by Year"""
    state_check = matr['State'] == True
    year_check = matr['Year'] == year
    state = matr[state_check&year_check]['School'].value_counts()
    return state

def state_gender_year(year):
    """Filter by State Schools Gender by Year"""
    state_check = matr['State'] == True
    year_check = matr['Year'] == year

    female_state = matr['Gender'] == 'Female'
    male_state = matr['Gender'] == 'Male'

    female = matr[female_state & state_check & year_check]['School'].value_counts()
    male = matr[male_state & state_check & year_check]['School'].value_counts()

    return female, male

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.MainWidget = QWidget(self)
        self.MainLayout = QHBoxLayout()
        
        self.MainWidget.setLayout(self.MainLayout)
        #self.MainWidget.setFixedSize(900,600)

        self.setMinimumHeight(650)
        self.setMinimumWidth(1000)

        self.plot_layout = QVBoxLayout()
        self.figure = plt.figure()

        self.canvas = plt_backend.FigureCanvasQTAgg(self.figure)
        self.canvas.setFixedSize(600,400)
        self.toolbar = plt_backend.NavigationToolbar2QT(self.canvas, self.MainWidget)

        self.plot_layout.addWidget(self.canvas)
        self.plot_layout.addWidget(self.toolbar)

        self.MainLayout.addLayout(self.plot_layout)
        self.canvas.draw()


        
        #Plot Buttons for Total Values
        self.button_layout = QVBoxLayout()

        self.total_count = QPushButton('Total Count')
        self.button_layout.addWidget(self.total_count)
        self.total_count_func = functools.partial(self.plot_count, full_matr, 'Total Count')
        self.total_count.clicked.connect(self.total_count_func)

        self.total_gender = QPushButton('Total Gender')
        self.button_layout.addWidget(self.total_gender)
        self.total_gender_func = functools.partial(self.plot_gender, full_gender, 'Total Gender')
        self.total_gender.clicked.connect(self.total_gender_func)

        self.ivy_count = QPushButton('Ivy Total Count')
        self.button_layout.addWidget(self.ivy_count)
        self.ivy_count_func = functools.partial(self.plot_count, ivy_league, 'Ivy Total Count')
        self.ivy_count.clicked.connect(self.ivy_count_func)

        self.ivy_gender_count = QPushButton('Ivy Gender')
        self.button_layout.addWidget(self.ivy_gender_count)
        self.ivy_gender_count_func = functools.partial(self.plot_gender, ivy_gender, 'Ivy Gender')
        self.ivy_gender_count.clicked.connect(self.ivy_gender_count_func)

        self.state_count = QPushButton('State Total Count')
        self.button_layout.addWidget(self.state_count)
        self.state_count_func = functools.partial(self.plot_count, state_schools, 'State Total Count')
        self.state_count.clicked.connect(self.state_count_func)

        self.state_gender_count = QPushButton('State Gender')
        self.button_layout.addWidget(self.state_gender_count)
        self.state_gender_count_func = functools.partial(self.plot_gender, state_gender, 'State Gender')
        self.state_gender_count.clicked.connect(self.state_gender_count_func)

        self.MainLayout.addLayout(self.button_layout)



        #Drop Down Menu/Plotting by Year
        self.drop_layout = QVBoxLayout()

        self.drop_down = QComboBox()
        self.drop_down.addItems(['2021', '2020'])
        
        self.drop_layout.addWidget(self.drop_down)


        self.ivy_count_year = QPushButton('Ivy by Year')
        self.drop_layout.addWidget(self.ivy_count_year)
        self.ivy_count_year_func = functools.partial(self.plot_count_year, ivy_league_year, 'Ivy Count: ')
        self.ivy_count_year.clicked.connect(self.ivy_count_year_func)

        self.ivy_gender_year_count = QPushButton('Ivy Gender by Year')
        self.drop_layout.addWidget(self.ivy_gender_year_count)
        self.ivy_gender_year_count_func = functools.partial(self.plot_gender_year, ivy_gender_year, 'Ivy Gender: ')
        self.ivy_gender_year_count.clicked.connect(self.ivy_gender_year_count_func)

        self.state_count_year = QPushButton('State by Year')
        self.drop_layout.addWidget(self.state_count_year)
        self.state_count_year_func = functools.partial(self.plot_count_year, state_schools_year, 'State Count: ')
        self.state_count_year.clicked.connect(self.state_count_year_func)

        self.state_gender_year_count = QPushButton('State Gender by Year')
        self.drop_layout.addWidget(self.state_gender_year_count)
        self.state_gender_year_count_func = functools.partial(self.plot_gender_year, state_gender_year, 'State Gender: ')
        self.state_gender_year_count.clicked.connect(self.state_gender_year_count_func)

        self.MainLayout.addLayout(self.drop_layout)

    def plot_count(self, func, str1):
        """Plot Total Val"""
        plt.clf()
        self.a1 = self.figure.add_subplot()

        self.result = func()
        self.result.plot(kind='bar', ax = self.a1)

        self.figure.suptitle(str1)

        plt.tight_layout()

        self.canvas.draw()
    
    def plot_gender(self, func, str1):
        """Plot Graphs with Gender Count"""
        plt.clf()
        self.a1 = self.figure.add_subplot(1, 2, 1)
        self.a2 = self.figure.add_subplot(1, 2, 2)

        self.female, self.male = func()

        self.result_max = []

        self.result_max.append(max(self.female))
        self.result_max.append(max(self.male))

        self.max = max(self.result_max)

        self.a1.set_ylim([0,self.max])
        self.a2.set_ylim([0,self.max])
        
        self.female.plot(kind='bar',ax=self.a1)
        self.male.plot(kind='bar',ax=self.a2)

        self.a1.set_title('Female')
        self.a2.set_title('Male')
        self.figure.suptitle(str1)

        plt.tight_layout()

        self.canvas.draw()

    def plot_count_year(self, func, str1):
        """Plot Total Val by Year"""
        plt.clf()
        self.a1 = self.figure.add_subplot()
        
        year = int(self.drop_down.currentText())

        self.result = func(year)
        self.result.plot(kind='bar', ax = self.a1)

        self.figure.suptitle(str1 + str(year))

        plt.tight_layout()

        self.canvas.draw()
    
    def plot_gender_year(self, func, str1):
        """Plot Graphs with Gender Count by Year"""
        plt.clf()
        self.a1 = self.figure.add_subplot(1, 2, 1)
        self.a2 = self.figure.add_subplot(1, 2, 2)

        year = int(self.drop_down.currentText())

        self.female, self.male = func(year)

        self.result_max = []

        self.result_max.append(max(self.female))
        self.result_max.append(max(self.male))

        self.max = max(self.result_max)

        self.a1.set_ylim([0,self.max])
        self.a2.set_ylim([0,self.max])
        
        self.female.plot(kind='bar',ax=self.a1)
        self.male.plot(kind='bar',ax=self.a2)

        self.a1.set_title('Female')
        self.a2.set_title('Male')
        self.figure.suptitle(str1 + str(year))

        plt.tight_layout()

        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
