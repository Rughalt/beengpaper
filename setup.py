# This Python file uses the following encoding: utf-8
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
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHumanReadableCopyright': u"Copyright © 2019, Antoni Sobkowicz / Dragonshorn Studios, All Rights Reserved",
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