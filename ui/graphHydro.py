# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphHydro.ui'
#
# Created: Tue Sep 12 11:17:11 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
#***************************
try:
    from matplotlib.backends.backend_qt4agg\
        import NavigationToolbar2QTAgg as NavigationToolbar

except:
    from matplotlib.backends.backend_qt4agg \
        import NavigationToolbar2QT as NavigationToolbar
# **************************************************
class Ui_GraphHydro(object):
    def setupUi(self, GraphHydro):
        GraphHydro.setObjectName(_fromUtf8("GraphHydro"))
        GraphHydro.resize(919, 519)
        self.gridLayout = QtGui.QGridLayout(GraphHydro)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.comboBox_State = QtGui.QComboBox(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_State.sizePolicy().hasHeightForWidth())
        self.comboBox_State.setSizePolicy(sizePolicy)
        self.comboBox_State.setObjectName(_fromUtf8("comboBox_State"))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_State)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.comboBox_Scenar = QtGui.QComboBox(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Scenar.sizePolicy().hasHeightForWidth())
        self.comboBox_Scenar.setSizePolicy(sizePolicy)
        self.comboBox_Scenar.setObjectName(_fromUtf8("comboBox_Scenar"))
        self.comboBox_Scenar.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_Scenar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.comboBox_var1 = QtGui.QComboBox(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_var1.sizePolicy().hasHeightForWidth())
        self.comboBox_var1.setSizePolicy(sizePolicy)
        self.comboBox_var1.setObjectName(_fromUtf8("comboBox_var1"))
        self.comboBox_var1.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_var1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        # ****************************************
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GraphHydro.canvas.sizePolicy().hasHeightForWidth())
        GraphHydro.canvas.setSizePolicy(sizePolicy)   
        self.verticalLayout.addWidget(GraphHydro.canvas)
        # ********************************************
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.bt_reculTot = QtGui.QPushButton(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_reculTot.sizePolicy().hasHeightForWidth())
        self.bt_reculTot.setSizePolicy(sizePolicy)
        self.bt_reculTot.setDefault(False)
        self.bt_reculTot.setObjectName(_fromUtf8("bt_reculTot"))
        self.horizontalLayout_2.addWidget(self.bt_reculTot)
        self.bt_recul = QtGui.QPushButton(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_recul.sizePolicy().hasHeightForWidth())
        self.bt_recul.setSizePolicy(sizePolicy)
        self.bt_recul.setObjectName(_fromUtf8("bt_recul"))
        self.horizontalLayout_2.addWidget(self.bt_recul)
        self.comboBox_time = QtGui.QComboBox(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_time.sizePolicy().hasHeightForWidth())
        self.comboBox_time.setSizePolicy(sizePolicy)
        self.comboBox_time.setObjectName(_fromUtf8("comboBox_time"))
        self.comboBox_time.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_time)
        self.bt_av = QtGui.QPushButton(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_av.sizePolicy().hasHeightForWidth())
        self.bt_av.setSizePolicy(sizePolicy)
        self.bt_av.setObjectName(_fromUtf8("bt_av"))
        self.horizontalLayout_2.addWidget(self.bt_av)
        self.bt_avTot = QtGui.QPushButton(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_avTot.sizePolicy().hasHeightForWidth())
        self.bt_avTot.setSizePolicy(sizePolicy)
        self.bt_avTot.setObjectName(_fromUtf8("bt_avTot"))
        self.horizontalLayout_2.addWidget(self.bt_avTot)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        # ******************************
        self.toolbar = NavigationToolbar(GraphHydro.canvas, GraphHydro)
        self.verticalLayout.addWidget(self.toolbar)
        # ******************************************
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget_RES = QtGui.QTableWidget(GraphHydro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_RES.sizePolicy().hasHeightForWidth())
        self.tableWidget_RES.setSizePolicy(sizePolicy)
        self.tableWidget_RES.setObjectName(_fromUtf8("tableWidget_RES"))
        self.tableWidget_RES.setColumnCount(0)
        self.tableWidget_RES.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_RES)
        self.bt_exportCSV = QtGui.QPushButton(GraphHydro)
        self.bt_exportCSV.setObjectName(_fromUtf8("bt_exportCSV"))
        self.verticalLayout_2.addWidget(self.bt_exportCSV)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.actionBt_reculTot = QtGui.QAction(GraphHydro)
        self.actionBt_reculTot.setObjectName(_fromUtf8("actionBt_reculTot"))
        self.actionBt_recul = QtGui.QAction(GraphHydro)
        self.actionBt_recul.setObjectName(_fromUtf8("actionBt_recul"))
        self.actionBt_av = QtGui.QAction(GraphHydro)
        self.actionBt_av.setObjectName(_fromUtf8("actionBt_av"))
        self.actionBt_avTot = QtGui.QAction(GraphHydro)
        self.actionBt_avTot.setObjectName(_fromUtf8("actionBt_avTot"))
        self.actionBt_exportCSV = QtGui.QAction(GraphHydro)
        self.actionBt_exportCSV.setObjectName(_fromUtf8("actionBt_exportCSV"))
        self.actionComboBox_State = QtGui.QAction(GraphHydro)
        self.actionComboBox_State.setObjectName(_fromUtf8("actionComboBox_State"))
        self.actionComboBox_Scenar = QtGui.QAction(GraphHydro)
        self.actionComboBox_Scenar.setObjectName(_fromUtf8("actionComboBox_Scenar"))
        self.actionComboBox_var1 = QtGui.QAction(GraphHydro)
        self.actionComboBox_var1.setObjectName(_fromUtf8("actionComboBox_var1"))
        self.actionComboBox_var2 = QtGui.QAction(GraphHydro)
        self.actionComboBox_var2.setObjectName(_fromUtf8("actionComboBox_var2"))
        self.actionTableWidget_RES = QtGui.QAction(GraphHydro)
        self.actionTableWidget_RES.setObjectName(_fromUtf8("actionTableWidget_RES"))
        self.actionComboBox_time = QtGui.QAction(GraphHydro)
        self.actionComboBox_time.setObjectName(_fromUtf8("actionComboBox_time"))

        self.retranslateUi(GraphHydro)
        QtCore.QObject.connect(self.bt_recul, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_recul.trigger)
        QtCore.QObject.connect(self.bt_reculTot, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_reculTot.trigger)
        QtCore.QObject.connect(self.bt_av, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_av.trigger)
        QtCore.QObject.connect(self.bt_avTot, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_avTot.trigger)
        QtCore.QObject.connect(self.bt_exportCSV, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_exportCSV.trigger)
        QtCore.QObject.connect(self.comboBox_State, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.actionComboBox_State.trigger)
        QtCore.QObject.connect(self.comboBox_Scenar, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.actionComboBox_Scenar.trigger)
        QtCore.QObject.connect(self.comboBox_var1, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.actionComboBox_var1.trigger)
        QtCore.QObject.connect(self.comboBox_time, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.actionComboBox_time.trigger)
        QtCore.QMetaObject.connectSlotsByName(GraphHydro)

    def retranslateUi(self, GraphHydro):
        GraphHydro.setWindowTitle(_translate("GraphHydro", "Hydro. Results", None))
        self.comboBox_State.setItemText(0, _translate("GraphHydro", "Transcritical unsteady", None))
        self.comboBox_State.setItemText(1, _translate("GraphHydro", "Steady", None))
        self.comboBox_State.setItemText(2, _translate("GraphHydro", "Unsteady", None))
        self.comboBox_Scenar.setItemText(0, _translate("GraphHydro", "Scenar", None))
        self.comboBox_var1.setItemText(0, _translate("GraphHydro", "None", None))
        self.bt_reculTot.setText(_translate("GraphHydro", "<<", None))
        self.bt_recul.setText(_translate("GraphHydro", "<", None))
        self.comboBox_time.setItemText(0, _translate("GraphHydro", "Times/Pk", None))
        self.bt_av.setText(_translate("GraphHydro", ">", None))
        self.bt_avTot.setText(_translate("GraphHydro", ">>", None))
        self.bt_exportCSV.setText(_translate("GraphHydro", "Results export CSV", None))
        self.actionBt_reculTot.setText(_translate("GraphHydro", "bt_reculTot", None))
        self.actionBt_recul.setText(_translate("GraphHydro", "bt_recul", None))
        self.actionBt_av.setText(_translate("GraphHydro", "bt_av", None))
        self.actionBt_avTot.setText(_translate("GraphHydro", "bt_avTot", None))
        self.actionBt_exportCSV.setText(_translate("GraphHydro", "bt_exportCSV", None))
        self.actionComboBox_State.setText(_translate("GraphHydro", "comboBox_State", None))
        self.actionComboBox_Scenar.setText(_translate("GraphHydro", "comboBox_Scenar", None))
        self.actionComboBox_var1.setText(_translate("GraphHydro", "comboBox_var1", None))
        self.actionComboBox_var2.setText(_translate("GraphHydro", "comboBox_var2", None))
        self.actionTableWidget_RES.setText(_translate("GraphHydro", "tableWidget_RES", None))
        self.actionComboBox_time.setText(_translate("GraphHydro", "comboBox_time", None))

class NavigationToolbar(NavigationToolbar):
    # only display the buttons we need
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Back', 'Forward', 'Pan', 'Zoom', 'Save')]
