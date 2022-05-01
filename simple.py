#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
"""

# import required functionality from PyQt5.QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    # create application object
    app = QApplication(sys.argv)

    # use user interface constructor to construct window
    w = QWidget()
    
    # resize window
    w.resize(250, 150)
    
    # move window
    w.move(300, 300)
    
    # set window title
    w.setWindowTitle('Simple')
    
    # display window on screen
    w.show()

    # end main if exit method is called or widget is destroyed
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
 
