# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1130, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.calc_homography_btn = QPushButton(self.centralwidget)
        self.calc_homography_btn.setObjectName(u"calc_homography_btn")
        self.calc_homography_btn.setEnabled(True)
        self.calc_homography_btn.setGeometry(QRect(10, 620, 280, 30))
        sizePolicy.setHeightForWidth(self.calc_homography_btn.sizePolicy().hasHeightForWidth())
        self.calc_homography_btn.setSizePolicy(sizePolicy)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 280, 560))
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 278, 558))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 200))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(180, 580, 50, 30))
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.road_unit = QDoubleSpinBox(self.centralwidget)
        self.road_unit.setObjectName(u"road_unit")
        self.road_unit.setGeometry(QRect(235, 580, 55, 30))
        sizePolicy.setHeightForWidth(self.road_unit.sizePolicy().hasHeightForWidth())
        self.road_unit.setSizePolicy(sizePolicy)
        self.road_unit.setValue(1.000000000000000)
        self.imu = QCheckBox(self.centralwidget)
        self.imu.setObjectName(u"imu")
        self.imu.setGeometry(QRect(10, 580, 55, 30))
        self.utm = QCheckBox(self.centralwidget)
        self.utm.setObjectName(u"utm")
        self.utm.setGeometry(QRect(65, 580, 55, 30))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(300, 10, 821, 681))
        self.image_holder = QVBoxLayout(self.verticalLayoutWidget)
        self.image_holder.setObjectName(u"image_holder")
        self.image_holder.setContentsMargins(0, 0, 0, 0)
        self.cam_pose_est_btn = QPushButton(self.centralwidget)
        self.cam_pose_est_btn.setObjectName(u"cam_pose_est_btn")
        self.cam_pose_est_btn.setGeometry(QRect(10, 660, 280, 30))
        self.region_growing = QCheckBox(self.centralwidget)
        self.region_growing.setObjectName(u"region_growing")
        self.region_growing.setGeometry(QRect(120, 580, 40, 30))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LabelGUI", None))
        self.calc_homography_btn.setText(QCoreApplication.translate("MainWindow", u"Calculate Homography", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.utm.setText(QCoreApplication.translate("MainWindow", u"UTM", None))
        self.cam_pose_est_btn.setText(QCoreApplication.translate("MainWindow", u"Estimate Camera Pose", None))
        self.region_growing.setText(QCoreApplication.translate("MainWindow", u"RG", None))
    # retranslateUi

