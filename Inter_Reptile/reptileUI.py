# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reptileUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtGui import QPixmap
import os
import sys
from PIL import Image



class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow,rowCount):
        MainWindow.setObjectName("ReptileManager")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 471, 561))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        #设置表格不可修改
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #设置表格整行选择
        self.Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        #设置表格可以多选
        self.Table.setSelectionMode(QAbstractItemView.ExtendedSelection) 

        
        self.Table.setGeometry(QtCore.QRect(0, 30, 471, 531))
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(2)
        self.Table.setColumnWidth(0,320)
        self.Table.setColumnWidth(1,110)
        self.Table.setRowCount(rowCount)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.Table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Table.setHorizontalHeaderItem(1, item)
        #构建表格
        self.setTableItem(rowCount)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.importData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.importData.setObjectName("importData")
        self.horizontalLayout.addWidget(self.importData)
        self.cleanTable = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cleanTable.setObjectName("cleanTable")
        self.horizontalLayout.addWidget(self.cleanTable)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.deleteImg = QtWidgets.QPushButton(self.centralwidget)
        self.deleteImg.setGeometry(QtCore.QRect(500, 210, 75, 23))
        self.deleteImg.setObjectName("deleteImg")
        self.openImg = QtWidgets.QPushButton(self.centralwidget)
        self.openImg.setGeometry(QtCore.QRect(500, 310, 75, 23))
        self.openImg.setObjectName("openImg")
        self.deleteFolder = QtWidgets.QPushButton(self.centralwidget)
        self.deleteFolder.setGeometry(QtCore.QRect(500, 360, 75, 23))
        self.deleteFolder.setObjectName("deleteFolder")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 10, 481, 561))
        self.label.setText("")
        self.label.setObjectName("label")
        self.openFolder = QtWidgets.QPushButton(self.centralwidget)
        self.openFolder.setGeometry(QtCore.QRect(500, 260, 75, 23))
        self.openFolder.setObjectName("openFolder")
        self.totalImg = QtWidgets.QLabel(self.centralwidget)
        self.totalImg.setGeometry(QtCore.QRect(500, 170, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalImg.setFont(font)
        self.totalImg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.totalImg.setMouseTracking(False)
        self.totalImg.setIndent(-1)
        self.totalImg.setObjectName("totalImg")
        self.totalImgValue = QtWidgets.QLabel(self.centralwidget)
        self.totalImgValue.setGeometry(QtCore.QRect(640, 170, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalImgValue.setFont(font)
        self.totalImgValue.setText("")
        self.totalImgValue.setObjectName("totalImgValue")
        self.totalValue = QtWidgets.QLabel(self.centralwidget)
        self.totalValue.setGeometry(QtCore.QRect(640, 130, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalValue.setFont(font)
        self.rowCountStr=str(rowCount)
        self.totalValue.setText(self.rowCountStr)
        self.totalValue.setObjectName("totalValue")
        self.Total = QtWidgets.QLabel(self.centralwidget)
        self.Total.setGeometry(QtCore.QRect(500, 130, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Total.setFont(font)
        self.Total.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Total.setMouseTracking(False)
        self.Total.setIndent(-1)
        self.Total.setObjectName("Total")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 230, 51, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 330, 51, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.mainPath='D:\\A学习\\PYTHON\\Python入门到实践\\API\\'
        self.fpath=self.mainPath+'image1\\'
      
        
        #信号槽函数
        self.Table.cellClicked['int','int'].connect(self.selectRow)
        self.openFolder.clicked.connect(self.openFolderAct)
        self.deleteImg.clicked.connect(self.deleteImgAct)
        self.pushButton.clicked.connect(self.backImgAct)
        self.pushButton_2.clicked.connect(self.nextImgAct)
        self.openImg.clicked.connect(self.openImgAct)
        self.deleteFolder.clicked.connect(self.deleteFolderAct)
        self.importData.clicked.connect(self.importDataAct)
        self.cleanTable.clicked.connect(self.Table.clearContents)        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ReptileManager"))
        item = self.Table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件夹名"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "图片数量"))
        __sortingEnabled = self.Table.isSortingEnabled()
        self.Table.setSortingEnabled(False)
        self.Table.setSortingEnabled(__sortingEnabled)
        self.deleteImg.setText(_translate("MainWindow", "删除文件"))
        self.openImg.setText(_translate("MainWindow", "打开图片"))
        self.deleteFolder.setText(_translate("MainWindow", "删除文件夹"))
        self.openFolder.setText(_translate("MainWindow", "打开文件夹"))
        self.totalImg.setText(_translate("MainWindow", "图集共有照片:"))
        self.Total.setText(_translate("MainWindow", "共有图集:"))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", ">"))
        self.importData.setText(_translate("MainWindow", "导入"))
        self.cleanTable.setText(_translate("MainWindow", "清空表格"))
        
     
    #设置表格
    def setTableItem(self,rowCount):
        for i in range(0,rowCount):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.Table.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.Table.setItem(i, 1, item)
        
        
        
    #更新Items
    def updateItem(self,name,count,i):
        _translate = QtCore.QCoreApplication.translate
        item = self.Table.item(i, 0)
        self.nameValue=str(name)
        #print(self.nameValue)
        item.setText(_translate("MainWindow", self.nameValue))
        item = self.Table.item(i, 1)
        self.countStr=str(count)
        item.setText(_translate("MainWindow", self.countStr))
        
    
    #创建缩略图    
    def makeIco(self,infile):
        size = (481,561)
        f = os.path.splitext(infile)
        img = Image.open(infile)
        img.thumbnail(size,Image.ANTIALIAS)
        savePath='icoImg/icoimg.png'
        img.save(savePath,"PNG")
        
        img=QPixmap(savePath)
        self.label.setPixmap(img)
        


    #选择当前列并获取两个Item的值   
    def selectRow(self,row):
        self.icoPos=1
        _translate = QtCore.QCoreApplication.translate
        self.imgName=self.Table.item(row,0).text()
        self.imgCounts=self.Table.item(row,1).text()
        self.totalImgValue.setText(_translate("MainWindow", self.imgCounts))
        self.sendRow=row
        #self.min=1
        #self.max=self.imgCounts
        
        #文件夹路径
        self.folderPath=self.fpath+self.imgName
        self.imgPath=self.folderPath+'\\'+str(self.icoPos)+'.png'
        self.makeIco(self.imgPath)
        
        
        
    
    #打开所选文件夹
    def openFolderAct(self):
        Obj=self.folderPath
        if Obj and os.path.exists(Obj): #文件or 目录存在
            os.startfile(str(Obj)) 
 
        else:# 不存在的目录
            print("不存在的目录")
            
    
    #删除图片
    def deleteImgAct(self):
        _translate = QtCore.QCoreApplication.translate
        if os.path.exists(self.imgPath):
            #删除文件，可使用以下两种方法。
            os.remove(self.imgPath)
            self.imgCounts=str(int(self.imgCounts)-1)
            item=self.Table.item(self.sendRow, 1)
            item.setText(_translate("MainWindow", self.imgCounts))
            self.totalImgValue.setText(_translate("MainWindow", self.imgCounts))
            self.renameAfterDelete()
                    

        else:
            print('no such file:%s'%self.imgPath)
    
    
    #上一张图片
    def backImgAct(self):
        if self.icoPos==1:
            return
        else:
            self.icoPos-=1
            self.imgPath=self.folderPath+'\\'+str(self.icoPos)+'.png'
            self.makeIco(self.imgPath)
            
            
    #下一张图片
    def nextImgAct(self):
        imgMax=int(self.imgCounts)
        if self.icoPos==imgMax:
            return
        else:
            self.icoPos+=1
            self.imgPath=self.folderPath+'\\'+str(self.icoPos)+'.png'
            self.makeIco(self.imgPath)
     
        
    #删除文件后遍历重命名所有文件    
    def renameAfterDelete(self):
        n=1
        for root,dirs,files in os.walk(self.folderPath):
            for item in files:
                name=str(n)+'.png'
                os.rename(os.path.join(root,item),os.path.join(root,name))
                n+=1
        self.icoPos=1
        self.imgPath=self.folderPath+'\\'+str(self.icoPos)+'.png'
        if os.path.exists(self.imgPath):
            self.makeIco(self.imgPath)
        else:
            self.label.setText(" ")
                
    #打开图片
    def openImgAct(self):
        Obj=self.imgPath
        if Obj and os.path.exists(Obj): #图片存在
            os.startfile(str(Obj)) 
 
        else:# 不存在的图片
            print("不存在的图片")
            
    
    #删除文件夹
    def deleteFolderAct(self):
        for root,dirs,files in os.walk(self.folderPath):
            for item in files:
                os.remove(os.path.join(root, item))
            os.rmdir(self.folderPath)
            self.label.setText(" ")
            item=self.Table.item(self.sendRow,0)
            item.setText(" ")
            item=self.Table.item(self.sendRow,1)
            item.setText(" ")
            return
        
    
    #导入文件夹
    def importDataAct(self):
        self.Table.clearContents
        path=self.lineEdit.text()
        try:
            if path!="":
                path=self.lineEdit.text()
                print(path)
            else:
                path = QtWidgets.QFileDialog.getExistingDirectory(self.importData,"浏览","D:\\",QtWidgets.QFileDialog.ShowDirsOnly)
                print(path)
            '''path=self.mainPath+self.lineEdit.text()+'\\'
            self.fpath=path
            self.lineEdit.setText("")'''
            rowCount=len(os.listdir(path))
            self.lineEdit.setText("")
        except FileNotFoundError:
                pass
        path+='/'
        self.fpath=path
        self.Table.setRowCount(rowCount)
        self.setTableItem(rowCount)
        self.totalValue.setText(str(rowCount))
        i=0
        for root,dirs,files in os.walk(path):
            for name in dirs:
                inPath=path+name
                imgNums=str(len(os.listdir(inPath)))
                item=self.Table.item(i,0)
                item.setText(name)
                item=self.Table.item(i,1)
                item.setText(imgNums)
                i+=1
         
        
        
        
        
    
    
            
        
        
        

