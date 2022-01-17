from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import cv2
import mediapipe as mp
import time
import pandas as pd
from threading import Thread

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    df = pyqtSignal(pd.DataFrame)
        

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        mpDraw = mp.solutions.drawing_utils
        mpPose = mp.solutions.pose
        pose = mpPose.Pose()
        df = pd.DataFrame({"Pull Ups": [0], "Key Points": [0], "vel": [0], "x": [0]})

        cap = cv2.VideoCapture(0)
        up = False
        counter = 0
        ind = 0
        #df = pd.DataFrame({"Pull Ups": [0], "Key Points": [0], "vel": [0], "x": [0]})

        cap = cv2.VideoCapture(0)

        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                success, cv_img = cap.read()
                
                cv_img = cv2.resize(cv_img, (1280, 720))
                imgRGB = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                results = pose.process(imgRGB)

                # print(results.pose_landmarks)
                # print("-----------------------------------------------------")
                if results.pose_landmarks:
                    mpDraw.draw_landmarks(cv_img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
                    points = {}
                    for id, lm in enumerate(results.pose_landmarks.landmark):
                        h,w,c = cv_img.shape
                        cx, cy = int(lm.x*w), int(lm.y*h)
                        df.loc[ind, "x"] = cx
                        df.loc[ind, "y"] = cy
                        # print(id,lm,cx,cy)
                        points[id] = (cx,cy)
                        ind += 1
                        if ind > 0:
                            prev_ind = int(ind - 1)
                        else:
                            prev_ind = 0
                        df.loc[ind, "Pull Ups"] = counter
                        #df.loc[ind, "Key Points"] = points[14]
                        df.loc[ind, "vel"] = ((counter / ind) * 30) * 60 
                        #print(df)


                    cv2.circle(cv_img, points[0], 15, (255,0,0), cv2.FILLED)
                    cv2.circle(cv_img, points[15], 15, (255,0,0), cv2.FILLED)
                    cv2.circle(cv_img, points[16], 15, (255,0,0), cv2.FILLED)
                    cv2.circle(cv_img, points[13], 15, (255,0,0), cv2.FILLED)
                    self.change_pixmap_signal.emit(cv_img)
                    self.df.emit(df)

                    if not up and points[14][1] + 40 < points[12][1]:
                        #print("UP")
                        up = True
                        counter += 1
                    elif points[14][1] > points[12][1]:
                        # print("Down")
                        up = False
                        # print("----------------------",counter)
        
                #cv2.putText(cv_img, str(counter), (100,150),cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0),12)
                    
        # shut down capture system
        cap.release()
        return df

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()
    def return_df(self):
        return self.get_df

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1566, 856)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pull_ups = QtWidgets.QLabel(self.centralwidget)
        self.pull_ups.setGeometry(QtCore.QRect(130, 20, 120, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pull_ups.setFont(font)
        self.pull_ups.setObjectName("pull_ups")
        self.progressBar = QRoundProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(980, 190, 571, 451))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.speed = QtWidgets.QLabel(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(350, 20, 120, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.speed.setFont(font)
        self.speed.setObjectName("speed")
        self.pr = QtWidgets.QLabel(self.centralwidget)
        self.pr.setGeometry(QtCore.QRect(550, 20, 120, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pr.setFont(font)
        self.pr.setObjectName("pr")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 61, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icons8-pullups-80.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 20, 61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icons8-speed-100.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 30, 61, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("icons8-best-seller-100.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.t_elapsed = QtWidgets.QLabel(self.centralwidget)
        self.t_elapsed.setGeometry(QtCore.QRect(1180, 70, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.t_elapsed.setFont(font)
        self.t_elapsed.setObjectName("t_elapsed")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(70, 180, 640, 480))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1566, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pull_ups.setText(_translate("MainWindow", "0"))
        self.speed.setText(_translate("MainWindow", "0"))
        self.pr.setText(_translate("MainWindow", "0"))
        self.t_elapsed.setText(_translate("MainWindow", "00:00"))
        
        #self.setWindowTitle("Qt live label demo")
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        #self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()
        self.prog_t()
        self.thread.df.connect(self.df)
        self.start_time = time.time()






    def closeEvent(self, event):
        self.thread.stop()
        event.accept()
        
    def prog_t(self):
        p_t = Thread(target=self.progress)
        p_t.start()
    def progress(self):
        self.progressBar.setValue()
        for i in range(0, 101, 1):
            self.progressBar.setValue(i)
            #self.processEvents()
            time.sleep(1)





    #@pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    def df(self, df):
        self.wo_df = df
        self.pull_ups.setText(str(max(self.wo_df["Pull Ups"])))
        self.pr.setText("31")
        self.speed.setText(str(int(max(self.wo_df["vel"]))))
        self.updated_time = time.time()
        timess = int(self.updated_time - self.start_time)
        if timess < 10:
            self.t_elapsed.setText("0:0" + str(timess))
        else:
            self.t_elapsed.setText("0:" + str(timess))

        

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
from qroundprogressbar import QRoundProgressBar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
