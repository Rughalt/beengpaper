# This Python file uses the following encoding: utf-8

# Copyright (c) 2019 Antoni Sobkowicz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from setuptools import setup

APP = ['beengpaper.py']
DATA_FILES = ['app_icon.png','icon.png']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'Beengpaper',
        'CFBundleDisplayName': 'Beengpaper',
        'CFBundleGetInfoString': "Gets Bing daily wallpaper to your desktop",
        'CFBundleIdentifier': "com.dragonshorn.bngpaper",
        'CFBundleVersion': "1.2.0",
        'CFBundleShortVersionString': "1.2.0",
        'NSHumanReadableCopyright': u"Copyright © 2019, Antoni Sobkowicz / Dragonshorn Studios",
        'LSUIElement': True,
    },
    'packages': ['rumps','appscript'],
    'iconfile':'app_icon.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['appscript', 'rumps']
)