# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giaodien.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 475)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 350, 641, 122))
        self.widget.setObjectName("widget")
        self.btnLayout = QtWidgets.QGridLayout(self.widget)
        self.btnLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.btnLayout.setContentsMargins(0, 0, 0, 0)
        self.btnLayout.setObjectName("btnLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowse = QtWidgets.QPushButton(self.widget)
        self.btnBrowse.setMaximumSize(QtCore.QSize(16777215, 23))
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.txtBrowse = QtWidgets.QLineEdit(self.widget)
        self.txtBrowse.setObjectName("txtBrowse")
        self.horizontalLayout.addWidget(self.txtBrowse)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnHistogram = QtWidgets.QPushButton(self.widget)
        self.btnHistogram.setObjectName("btnHistogram")
        self.gridLayout.addWidget(self.btnHistogram, 0, 0, 1, 1)
        self.btnBoxplot = QtWidgets.QPushButton(self.widget)
        self.btnBoxplot.setObjectName("btnBoxplot")
        self.gridLayout.addWidget(self.btnBoxplot, 0, 1, 1, 1)
        self.btnPie = QtWidgets.QPushButton(self.widget)
        self.btnPie.setObjectName("btnPie")
        self.gridLayout.addWidget(self.btnPie, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.btnLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnScat2D = QtWidgets.QPushButton(self.widget)
        self.btnScat2D.setObjectName("btnScat2D")
        self.gridLayout_2.addWidget(self.btnScat2D, 0, 0, 1, 1)
        self.btnMaxtrix = QtWidgets.QPushButton(self.widget)
        self.btnMaxtrix.setObjectName("btnMaxtrix")
        self.gridLayout_2.addWidget(self.btnMaxtrix, 0, 1, 1, 1)
        self.btnParallel = QtWidgets.QPushButton(self.widget)
        self.btnParallel.setObjectName("btnParallel")
        self.gridLayout_2.addWidget(self.btnParallel, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.btnStarglyph = QtWidgets.QPushButton(self.widget)
        self.btnStarglyph.setObjectName("btnStarglyph")
        self.verticalLayout_3.addWidget(self.btnStarglyph)
        self.btnLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnBrowse.setText(_translate("Dialog", "Browse"))
        self.btnHistogram.setText(_translate("Dialog", "Histogram"))
        self.btnBoxplot.setText(_translate("Dialog", "Boxplot"))
        self.btnPie.setText(_translate("Dialog", "Pie"))
        self.btnScat2D.setText(_translate("Dialog", "Scatter plot 2D"))
        self.btnMaxtrix.setText(_translate("Dialog", "Maxtrix"))
        self.btnParallel.setText(_translate("Dialog", "Parallel"))
        self.btnStarglyph.setText(_translate("Dialog", "btnStarglyph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
