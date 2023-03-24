import sys
from time import sleep
import random

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QDateTime
import pyautogui


class Application(QWidget):
  def __init__(self):
    super(Application, self).__init__()
    self.initUI()

  def initUI(self):
    # 窗口配置
    self.setWindowTitle('release-hands')
    self.resize(250, 150)

    # 页面布局
    self.time_label = QLabel('当前时间')
    self.button_status_label = QLabel('当前状态: 停止')
    self.button_start = QPushButton('开始')
    self.button_stop = QPushButton('停止')

    layout = QGridLayout()

    layout.addWidget(self.time_label, 0, 0, 1, 2)
    layout.addWidget(self.button_status_label, 1, 0, 1, 2)
    layout.addWidget(self.button_start, 2, 0)
    layout.addWidget(self.button_stop, 2, 1)

    self.setLayout(layout)

    # 设置按钮事件
    self.button_start.clicked.connect(self.start_auto_play)
    self.button_stop.clicked.connect(self.stop_auto_play)

    # 设置定时器
    self.timer = QTimer()
    self.timer.timeout.connect(self.show_time)
    # 每x毫秒执行一次
    self.timer.start(1)

  # 展示当前时间
  def show_time(self):
    # 获取当前时间
    time = QDateTime.currentDateTime()
    timedisplay = time.toString('yyyy-MM-dd hh:mm:ss.zzz')
    # 展示当前时间到time_label
    self.time_label.setText(timedisplay)

  # 开始自动按键
  def start_auto_play(self):
    self.timer_auto_play = QTimer()
    self.timer_auto_play.timeout.connect(self.auto_play)
    self.button_status_label.setText('当前状态: 开始')
    self.timer_auto_play.start(100)

  def auto_play(self):
    random_interval = random.randint(1, 3) / 10
    pyautogui.press('d')
    pyautogui.press('a', interval=random_interval)

  # 停止自动按键
  def stop_auto_play(self):
    self.button_status_label.setText('当前状态: 终止')
    self.timer_auto_play.stop()

  def keyPressEvent(self, event: QKeyEvent) -> None:
    # print(event.key())
    return super().keyPressEvent(event)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = Application()
  main.show()
  sys.exit(app.exec_())
