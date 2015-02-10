#!/usr/bin/env python

# A script to create a basic WebKit wrapper for a webapp


import sys

from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView


# Modify these variables to control the window's title and size
TITLE = 'Title bar text'
HORIZONTAL_SIZE = 1850
VERTICAL_SIZE = 1000

# Modify this variable to set the page the webapp starts with
STARTING_URL = 'http://localhost:8001'


app = QApplication(sys.argv)

browser = QWebView()

browser.load(QUrl(STARTING_URL))
browser.move(0, 0)
browser.resize(HORIZONTAL_SIZE, VERTICAL_SIZE)
browser.setWindowTitle(TITLE)

browser.show()

sys.exit(app.exec_())
