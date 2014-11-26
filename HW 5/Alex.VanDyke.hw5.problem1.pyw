#!/usr/bin/python2.7

import sys, os
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from math import sin
from dns.rdatatype import NULL
#from DropdownGUI import Form
#http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		
		""" CENTRAL WIDGET """
		self.form = Form()
		self.setCentralWidget(self.form)
				
		""" MENU BAR SETUP """
				
		""" FILE MENU """
		self.menuFile = self.menuBar().addMenu("&File")
		self.actionSave = QAction("&Save", self)
		self.actionSaveAs = QAction("Save As", self)
		self.actionSave.setShortcut('Ctrl+S')
		self.connect(self.actionSave, SIGNAL("triggered()"), self.save)
		self.connect(self.actionSaveAs, SIGNAL("triggered()"), self.saveas)
		self.actionExit = QAction("&*Exit", self)
		self.actionExit.setShortcut('Ctrl+Q')
		self.connect(self.actionExit, SIGNAL("triggered()"), self.close)
		
		self.menuFile.addActions([self.actionSave, self.actionSaveAs, self.actionExit])
		
		""" HELP MENU """
		self.menuHelp = self.menuBar().addMenu("&Help") #& underlines the H, give keyboard shortcut
		self.actionAbout = QAction("&About", self)
		self.connect(self.actionAbout, SIGNAL("triggered()"), self.about)
		self.menuHelp.addActions([self.actionAbout])
				
	def save(self):
		fname = QFileDialog.getSaveFileName(self, 'Save File')
		file_open = open(fname, 'w')
		self.vals = self.form.param_edit.text()
		self.func = self.form.output_edit.text()
		file_open.write('x = ')
		file_open.write(self.vals)
		file_open.write('f(x) = ')
		file_open.write(self.func)
		file_open.close()	
			
	def saveas(self):
		fname = unicode(QFileDialog.getSaveFileName(self, "Save as..."))
		file_open = open(fname, 'w')
		self.vals = self.form.param_edit.text()
		self.func = self.form.output_edit.text()
		file_open.write('x = ')
		file_open.write(self.vals)
		file_open.write('f(x) = ')
		file_open.write(self.func)
		file_open.close()
		
	def about(self):
		QMessageBox.about(self, "About Fucntion Evaluator", 
						'''Enter the values that you want to evaluate for x using commas to separate
						Choose the function you want to evalutate from the dropdown menu''')
		
class MatplotlibCanvas(FigureCanvas) :
    """ This is borrowed heavily from the matplotlib documentation;
        specifically, see:
        http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100) :
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)
        f = NULL
        x = NULL
        self.compute_initial_figure(f, x)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self, f, x):
#         t = np.arange(0.0, 3.0, 0.01)
#         f = np.sin(2*np.pi*)
        self.axes.plot(x, f)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('f(t)')  
		

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		self.plot = MatplotlibCanvas()
		self.function_edit = QComboBox(self)
        #Where initial cursor will be
		self.param_edit = QLineEdit("x = ...")
		self.param_edit.selectAll()
		self.output_edit = QLineEdit("Output = ...")
		self.solve_button = QPushButton("Solve", self)

				        
		self.function_edit.addItem("10*x")
		self.function_edit.addItem("x**2")
		self.function_edit.addItem("1/x")
		self.function_edit.addItem("np.sin(" + "x" + ")")
                             
        #Vertical box layout
		layout = QVBoxLayout()
		layout.addWidget(self.plot)
		layout.addWidget(self.param_edit) 
		layout.addWidget(self.function_edit)
		layout.addWidget(self.output_edit)
		layout.addWidget(self.solve_button)
        
        #Set layout
		self.setLayout(layout)
		self.param_edit.setFocus()
        
        #When output box is highlighted, return pressed activates
		self.connect(self.param_edit, SIGNAL("returnPressed()"), self.updateUI)
		self.connect(self.solve_button, SIGNAL("clicked()"), self.buttonClicked)
		self.connect(self.output_edit, SIGNAL("returnPressed()"), self.updateUI)
                        
	def updateUI(self):
		try:
			x = np.array(eval(str(self.param_edit.text())))
            #Reads in as Qt string or text, convert to string to eval, eval, convert solution to string
			f = eval(str(self.function_edit.currentText()))
			f_s = str(f).replace("[","").replace("]","").replace("  ", ", ")
			self.output_edit.setText(f_s)
			self.plot.compute_initial_figure(f, x)
			self.plot.draw()
		except:
			self.output_edit.setText("Unhandled function or parameter")
	   	
	def buttonClicked(self):
		try:
			x = np.array(eval(str(self.param_edit.text())))
            #Reads in as Qt string or text, convert to string to eval, eval, convert solution to string
			f = eval(str(self.function_edit.currentText()))
			f_s = str(f).replace("[","").replace("]","").replace("  ", ", ").replace("  ", ", ")
			self.output_edit.setText(f_s)
			self.plot.compute_initial_figure(f, x)
			self.plot.draw()
		except:
			self.output_edit.setText("Unhandled function or parameter")
	   	
app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()



