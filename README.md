## Beengpaper

Beengpaper (pronounced *bingpaper*) is a small macOS menu bar
application that downloads the daily wallpaper from Bing and sets it on
all of your desktops.

<img src="app_icon.png" alt="Bgnpaper Icon" width="200"/>

> First (a little bit ugly) version of Beengpaper icon

### Requirements
Beengpaper requires macOS El Captain (10.11) or later.

### Installation 

Download the application here, open `.dmg` file and drag and drop the
app into Applications folder.

### Building the app yourself

Beengpaper is written in Python (Python 3.7), using rumps and appscript
libraries. Additionally you need py2app to build the application package
and create-dmg (awesome little tool for creating dmg files you can find
[here](https://github.com/sindresorhus/create-dmg)).

```
git clone
cd beengpaper
python setup.py py2app
```

### FAQ
**Q. But why?**

A. Because I got bored one sunday morning, and I like Bing wallpapers.

**Q. Names in the menu change but application does not change my
wallpaper**

A. This may be caused by one of three things:
- You did not allow application access to System Events when it first
  asked (you can change it under Preferences > Security)
- Your current wallpaper setting is "Change wallpaper every ..." in
  macOS preferences. Set wallpaper to static image to allow Beengpaper
  to work
- Application broke because something changed in Bing stream. If you
  think your problem is not related to two above, pleas open an issue on
  GitHub.
 
**Q. How can I make Beengpaper launch on startup?**

A. Unfortunately, Beengpaper cannot set itself as a launch program. You
can however easily make it launch on login using macOS Preferences pane.
Navigate to Preferences > Users and Groups > Login and add Beengpaper.

### License and copyright

Copyright © 2019 Antoni Sobkowicz / Dragonshorn Studios.

This program is licensed under MIT license.

All product names, logos, and brands are property of their respective
owners. All company, product and service names used in this website are
for identification purposes only. Use of these names, logos, and brands
does not imply endorsement.
