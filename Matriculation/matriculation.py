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
matr = pd.read_csv('/Users/sherryzhang/Desktop/Python/Matr/GHMatr.csv')
#selfmatr = pd.read_csv('./GHMatr.csv')

def full_matr(school):
    """Filter Value Counts of All"""
    school_check = matr['Highschool'] == school
    val_all = matr[school_check]['School'].value_counts()
    return val_all

def full_gender(school):
    """Filter All Data by Gender"""
    female_all = matr['Gender'] == 'Female'
    male_all = matr['Gender'] == 'Male'

    school_check = matr['Highschool'] == school

    female = matr[female_all & school_check]['School'].value_counts()
    male = matr[male_all & school_check]['School'].value_counts()

    return female, male

def ivy_league(school):
    """Filter by Ivy League"""
    school_check = matr['Highschool'] == school
    ivy_check = matr['Ivy League'] == True
    ivy = matr[ivy_check & school_check]['School'].value_counts()
    return ivy

def ivy_gender(school):
    """Filter by Ivy League Gender"""

    ivy_check = matr['Ivy League'] == True
    female_ivy = matr['Gender'] == 'Female'
    male_ivy = matr['Gender'] == 'Male'

    school_check = matr['Highschool'] == school

    female = matr[female_ivy & ivy_check & school_check]['School'].value_counts()
    male = matr[male_ivy & ivy_check & school_check]['School'].value_counts()

    return female, male

def state_schools(school):
    """Filter by State Schools"""
    school_check = matr['Highschool'] == school
    state_check = matr['State'] == True
    state = matr[state_check & school_check]['School'].value_counts()
    return state

def state_gender(school):
    """Filter by State Schools Gender"""
    state_check = matr['State'] == True
    female_state = matr['Gender'] == 'Female'
    male_state = matr['Gender'] == 'Male'

    school_check = matr['Highschool'] == school

    female = matr[female_state & state_check & school_check]['School'].value_counts()
    male = matr[male_state & state_check & school_check]['School'].value_counts()

    return female, male



def ivy_league_year(year, school):
    """Filter by Ivy League by Year"""
    school_check = matr['Highschool'] == school
    ivy_check = matr['Ivy League'] == True
    year_check = matr['Year'] == year
    ivy = matr[ivy_check & year_check & school_check]['School'].value_counts()
    return ivy

def ivy_gender_year(year, school):
    """Filter by Ivy League Gender by Year"""

    ivy_check = matr['Ivy League'] == True
    year_check = matr['Year'] == year

    female_ivy = matr['Gender'] == 'Female'
    male_ivy = matr['Gender'] == 'Male'

    school_check = matr['Highschool'] == school

    female = matr[female_ivy & ivy_check & year_check & school_check]['School'].value_counts()
    male = matr[male_ivy & ivy_check & year_check & school_check]['School'].value_counts()

    return female, male

def state_schools_year(year, school):
    """Filter by State Schools by Year"""
    school_check = matr['Highschool'] == school
    state_check = matr['State'] == True
    year_check = matr['Year'] == year
    state = matr[state_check & year_check & school_check]['School'].value_counts()
    return state

def state_gender_year(year, school):
    """Filter by State Schools Gender by Year"""
    state_check = matr['State'] == True
    year_check = matr['Year'] == year

    female_state = matr['Gender'] == 'Female'
    male_state = matr['Gender'] == 'Male'

    school_check = matr['Highschool'] == school

    female = matr[female_state & state_check & year_check & school_check]['School'].value_counts()
    male = matr[male_state & state_check & year_check & school_check]['School'].value_counts()

    return female, male

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.MainWidget = QWidget(self)
        self.MainLayout = QHBoxLayout()
        
        self.MainWidget.setLayout(self.MainLayout)
        #self.MainWidget.setFixedSize(900,600)

        self.setMinimumHeight(650)
        self.setMinimumWidth(1400)

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
        self.total_count_func = functools.partial(self.plot_count, full_matr, 'Total Count', 'Greenhill')
        self.total_count.clicked.connect(self.total_count_func)

        self.total_gender = QPushButton('Total Gender')
        self.button_layout.addWidget(self.total_gender)
        self.total_gender_func = functools.partial(self.plot_gender, full_gender, 'Total Gender', 'Greenhill')
        self.total_gender.clicked.connect(self.total_gender_func)

        self.ivy_count = QPushButton('Ivy Total Count')
        self.button_layout.addWidget(self.ivy_count)
        self.ivy_count_func = functools.partial(self.plot_count, ivy_league, 'Ivy Total Count', 'Greenhill')
        self.ivy_count.clicked.connect(self.ivy_count_func)

        self.ivy_gender_count = QPushButton('Ivy Gender')
        self.button_layout.addWidget(self.ivy_gender_count)
        self.ivy_gender_count_func = functools.partial(self.plot_gender, ivy_gender, 'Ivy Gender', 'Greenhill')
        self.ivy_gender_count.clicked.connect(self.ivy_gender_count_func)

        self.state_count = QPushButton('State Total Count')
        self.button_layout.addWidget(self.state_count)
        self.state_count_func = functools.partial(self.plot_count, state_schools, 'State Total Count', 'Greenhill')
        self.state_count.clicked.connect(self.state_count_func)

        self.state_gender_count = QPushButton('State Gender')
        self.button_layout.addWidget(self.state_gender_count)
        self.state_gender_count_func = functools.partial(self.plot_gender, state_gender, 'State Gender', 'Greenhill')
        self.state_gender_count.clicked.connect(self.state_gender_count_func)

        self.MainLayout.addLayout(self.button_layout)



        #Drop Down Menu/Plotting by Year
        self.drop_layout = QVBoxLayout()

        self.drop_down = QComboBox()
        self.drop_down.addItems(['2021', '2020'])
        
        self.drop_layout.addWidget(self.drop_down)


        self.ivy_count_year = QPushButton('Ivy by Year')
        self.drop_layout.addWidget(self.ivy_count_year)
        self.ivy_count_year_func = functools.partial(self.plot_count_year, ivy_league_year, 'Ivy Count: ', 'Greenhill')
        self.ivy_count_year.clicked.connect(self.ivy_count_year_func)

        self.ivy_gender_year_count = QPushButton('Ivy Gender by Year')
        self.drop_layout.addWidget(self.ivy_gender_year_count)
        self.ivy_gender_year_count_func = functools.partial(self.plot_gender_year, ivy_gender_year, 'Ivy Gender: ', 'Greenhill')
        self.ivy_gender_year_count.clicked.connect(self.ivy_gender_year_count_func)

        self.state_count_year = QPushButton('State by Year')
        self.drop_layout.addWidget(self.state_count_year)
        self.state_count_year_func = functools.partial(self.plot_count_year, state_schools_year, 'State Count: ', 'Greenhill')
        self.state_count_year.clicked.connect(self.state_count_year_func)

        self.state_gender_year_count = QPushButton('State Gender by Year')
        self.drop_layout.addWidget(self.state_gender_year_count)
        self.state_gender_year_count_func = functools.partial(self.plot_gender_year, state_gender_year, 'State Gender: ', 'Greenhill')
        self.state_gender_year_count.clicked.connect(self.state_gender_year_count_func)

        self.pie = QPushButton('Pie Chart')
        self.drop_layout.addWidget(self.pie)
        self.pie.clicked.connect(self.pie_chart)

        self.MainLayout.addLayout(self.drop_layout)



        #Drop Down Menu/Plotting by School
        self.school_layout = QVBoxLayout()

        self.school_drop = QComboBox()
        self.school_drop.addItems(['Hockaday', 'St. Marks'])
        
        self.school_layout.addWidget(self.school_drop)

        self.total_count_s = QPushButton('Total Count')
        self.school_layout.addWidget(self.total_count_s)
        self.total_count_s_func = functools.partial(self.plot_count_s, full_matr, ' Total Count')
        self.total_count_s.clicked.connect(self.total_count_s_func)

        self.ivy_count_s = QPushButton('Ivy Total Count')
        self.school_layout.addWidget(self.ivy_count_s)
        self.ivy_count_s_func = functools.partial(self.plot_count_s, ivy_league, ' Ivy Total Count')
        self.ivy_count_s.clicked.connect(self.ivy_count_s_func)

        self.state_count_s = QPushButton('State Total Count')
        self.school_layout.addWidget(self.state_count_s)
        self.state_count_s_func = functools.partial(self.plot_count_s, state_schools, ' State Total Count')
        self.state_count_s.clicked.connect(self.state_count_s_func)

        self.MainLayout.addLayout(self.school_layout)



        self.compare_layout = QVBoxLayout()

        self.compare_drop1 = QComboBox()
        self.compare_drop1.addItems(['Greenhill', 'Hockaday', 'St. Marks'])
        self.compare_layout.addWidget(self.compare_drop1)

        self.compare_drop2 = QComboBox()
        self.compare_drop2.addItems(['Greenhill', 'Hockaday', 'St. Marks'])
        self.compare_layout.addWidget(self.compare_drop2)

        self.compare_year = QComboBox()
        self.compare_year.addItems(['2021', '2020'])
        self.compare_layout.addWidget(self.compare_year)

        self.ivy_count_c = QPushButton('Ivy Total Count')
        self.compare_layout.addWidget(self.ivy_count_c)
        self.ivy_count_c_func = functools.partial(self.plot_compare, ivy_league_year, 'Ivy Total Count:')
        self.ivy_count_c.clicked.connect(self.ivy_count_c_func)

        self.state_count_c = QPushButton('State Total Count')
        self.compare_layout.addWidget(self.state_count_c)
        self.state_count_c_func = functools.partial(self.plot_compare, state_schools_year, 'Ivy Total Count:')
        self.state_count_c.clicked.connect(self.state_count_c_func)

        self.MainLayout.addLayout(self.compare_layout)



    def plot_count(self, func, str1, school):
        """Plot Total Val"""
        plt.clf()
        self.a1 = self.figure.add_subplot()

        result = func(school)
        result.plot(kind='bar', ax = self.a1)

        self.figure.suptitle(str1)

        plt.tight_layout()

        self.canvas.draw()
    
    def plot_gender(self, func, str1, school):
        """Plot Graphs with Gender Count"""
        plt.clf()
        self.a1 = self.figure.add_subplot(1, 2, 1)
        self.a2 = self.figure.add_subplot(1, 2, 2)

        female, male = func(school)

        result_max = []

        result_max.append(max(female))
        result_max.append(max(male))

        self.max = max(result_max)

        self.a1.set_ylim([0,self.max])
        self.a2.set_ylim([0,self.max])
        
        female.plot(kind='bar',ax=self.a1)
        male.plot(kind='bar',ax=self.a2)

        self.a1.set_title('Female')
        self.a2.set_title('Male')
        self.figure.suptitle(str1)

        plt.tight_layout()

        self.canvas.draw()

    def plot_count_year(self, func, str1, school):
        """Plot Total Val by Year"""
        plt.clf()
        self.a1 = self.figure.add_subplot()
        
        year = int(self.drop_down.currentText())

        result = func(year, school)
        result.plot(kind='bar', ax = self.a1)

        self.figure.suptitle(str1 + str(year))

        plt.tight_layout()

        self.canvas.draw()
    
    def plot_gender_year(self, func, str1, school):
        """Plot Graphs with Gender Count by Year"""
        plt.clf()
        self.a1 = self.figure.add_subplot(1, 2, 1)
        self.a2 = self.figure.add_subplot(1, 2, 2)

        year = int(self.drop_down.currentText())

        female, male = func(year, school)

        result_max = []

        result_max.append(max(female))
        result_max.append(max(male))

        self.max = max(result_max)

        self.a1.set_ylim([0,self.max])
        self.a2.set_ylim([0,self.max])
        
        female.plot(kind='bar',ax=self.a1)
        male.plot(kind='bar',ax=self.a2)

        self.a1.set_title('Female')
        self.a2.set_title('Male')
        self.figure.suptitle(str1 + str(year))

        plt.tight_layout()

        self.canvas.draw()


    def pie_chart(self):
        plt.clf()
        self.a1 = self.figure.add_subplot()

        year = int(self.drop_down.currentText())
        year_check = matr['Year'] == year

        ivy = matr['Ivy League'] == True
        state = matr['State'] == True

        ivy_count = len(matr[ivy & year_check])
        state_count = len(matr[state & year_check])

        other_count = len(matr[year_check]) - ivy_count - state_count

        array = [ivy_count, state_count, other_count]
        labels = ["Ivy League", "State Schools", "Other"]
        colors = ["lightgreen", "paleturquoise", "royalblue"]

        self.a1.pie(array, labels = labels, autopct='%1.1f%%', colors = colors)

        self.figure.suptitle(f"Pie Chart: {year}")

        plt.tight_layout()
        self.canvas.draw()


    def plot_count_s(self, func, str1):
        """Plot Total Val"""
        plt.clf()
        self.a1 = self.figure.add_subplot()

        school = (self.school_drop.currentText())

        result = func(school)
        result.plot(kind='bar', ax = self.a1)

        self.figure.suptitle(school + str1)

        plt.tight_layout()

        self.canvas.draw()


    def plot_compare(self, func, str1):
        plt.clf()
        self.a1 = self.figure.add_subplot(1,2,1)
        self.a2 = self.figure.add_subplot(1,2,2)

        school1 = self.compare_drop1.currentText()
        school2 = self.compare_drop2.currentText()

        year = int(self.compare_year.currentText())

        result1 = func(year, school1)
        result2 = func(year, school2)

        result_max = []

        result_max.append(max(result1))
        result_max.append(max(result2))

        self.max = max(result_max)

        self.a1.set_ylim([0,self.max])
        self.a2.set_ylim([0,self.max])

        result1.plot(kind='bar', ax=self.a1)
        result2.plot(kind='bar', ax=self.a2)

        self.figure.suptitle(f"{str1} {school1} vs. {school2}")

        plt.tight_layout()

        self.canvas.draw()
        


def main():
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
