import io
import sys
import sqlite3
import os
# import random
# import datetime
# import asyncio

from ui_load import template
from main import main
from play_AllTime import play_timer

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MenuGame(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUi()

    def initUi(self) -> None:
        self.connectionMenu()

    def connectionMenu(self) -> None:
        self.lvl2_btn.setEnabled(False)
        self.lvl3_btn.setEnabled(False)
        self.lvl4_btn.setEnabled(False)
        self.lvl5_btn.setEnabled(False)

        try:
            con = sqlite3.connect(r'database.db')
            cur = con.cursor()
            ls = cur.execute(
                'SELECT levels_completed, record_score FROM user_progress').fetchone()
            levels_completed, score = ls[0], ls[1]
            if levels_completed >= 1:
                self.lvl2_btn.setEnabled(True)
            if levels_completed >= 2:
                self.lvl3_btn.setEnabled(True)
            if levels_completed >= 3:
                self.lvl4_btn.setEnabled(True)
            if levels_completed >= 4:
                self.lvl5_btn.setEnabled(True)

            self.record_lcd.display(score)
        finally:
            con.commit()
            con.close()

        self.lvl1_btn.clicked.connect(self.goLevel1)
        self.lvl2_btn.clicked.connect(self.goLevel2)
        self.lvl3_btn.clicked.connect(self.goLevel3)
        self.lvl4_btn.clicked.connect(self.goLevel4)
        self.lvl5_btn.clicked.connect(self.goLevel5)

        self.play_btn.clicked.connect(self.playAllTime)

    def goLevel1(self):
        try:
            win, score = main(3, 4, 1.5, 10, 5, 1700, 0.15)
            con = sqlite3.connect(r'database.db')
            cur = con.cursor()
            win_check = cur.execute(
                f'SELECT levels_completed FROM user_progress').fetchone()[0] >= 1
            if win and not win_check:
                cur.execute(f'UPDATE user_progress SET levels_completed = 1')
                self.winMsg(1)
        finally:
            con.commit()
            con.close()
            self.initUi()

    def goLevel2(self):
        try:
            win, score = main(3.2, 4, 1.6, 10, 5, 1600, 0.2)
            con = sqlite3.connect(r'database.db')
            cur = con.cursor()
            win_check = cur.execute(
                f'SELECT levels_completed FROM user_progress').fetchone()[0] >= 2
            if win and not win_check:
                cur.execute(f'UPDATE user_progress SET levels_completed = 2')
                self.winMsg(2)
        finally:
            con.commit()
            con.close()
            self.initUi()

    def goLevel3(self):
        try:
            win, score = main(3.3, 4.5, 1.7, 15, 5, 1500, 0.25)
            con = sqlite3.connect(r'database.db')
            cur = con.cursor()
            win_check = cur.execute(
                f'SELECT levels_completed FROM user_progress').fetchone()[0] >= 3
            if win and not win_check:
                cur.execute(f'UPDATE user_progress SET levels_completed = 3')
                self.winMsg(3)
        finally:
            con.commit()
            con.close()
            self.initUi()

    def goLevel4(self):
        try:
            win, score = main(3.4, 5, 2, 15, 5, 1350, 0.25)
            con = sqlite3.connect(r'database.db')
            cur = con.cursor()
            win_check = cur.execute(
                f'SELECT levels_completed FROM user_progress').fetchone()[0] >= 4
            if win and not win_check:
                cur.execute(f'UPDATE user_progress SET levels_completed = 4')
                self.winMsg(4)
        finally:
            con.commit()
            con.close()
            self.initUi()

    def goLevel5(self):
        try:
            win, score = main(4.4, 5.5, 3.5, 25, 3, 1150, 0.2)
            con = sqlite3.connect(r'database.db')
            cur = con.cursor()
            win_check = cur.execute(
                f'SELECT levels_completed FROM user_progress').fetchone()[0] >= 5
            if win and not win_check:
                cur.execute(f'UPDATE user_progress SET levels_completed = 5')
                self.winMsgFinal()
        finally:
            con.commit()
            con.close()
            self.initUi()

    def playAllTime(self):
        try:
            con = sqlite3.connect(r'database.db')
            cur = con.cursor()
            purpose_check = cur.execute(
                f'SELECT record_score FROM user_progress').fetchone()[0]
            timer, score = play_timer(2.8, 5.5, 3, purpose_check, 5, 1500, 0.1)
            score_check = cur.execute(
                f'SELECT record_score FROM user_progress').fetchone()[0]
            timer_check = cur.execute(
                f'SELECT record_time FROM user_progress').fetchone()[0]
            if score > score_check:
                cur.execute(f'UPDATE user_progress SET record_score = {score}')
            if timer > timer_check:
                cur.execute(f'UPDATE user_progress SET record_time = {timer}')
        finally:
            con.commit()
            con.close()
            self.initUi()

    def winMsg(self, lvl):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Важное сообщение!")
        dlg.setText(f"Вы прошли {lvl} уровень, поздравляю!\nДвигаемся дальше)")
        dlg.exec_()
        # if button == QMessageBox.Ok:
        #    print("OK!")

    def winMsgFinal(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Важное сообщение!")
        dlg.setText(
            f"Вы прошли последний уровень, поздравляю!\nПоставьте рекорд в бесконечном режиме)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MenuGame()
    ex.show()
    sys.exit(app.exec())
