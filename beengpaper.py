#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

# Copyright (c) 2019 Antoni Sobkowicz / Dragonshorn Studios
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

import urllib.request
from threading import Timer
import rumps
import os
import json
import logging
from appscript import *
from rumps import separator, MenuItem

configs = {}
configs_data = {}
home_dir = os.path.expanduser('~')+'/.bwg'
base_wallpaper_url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt="


if not os.path.exists(home_dir):
    os.makedirs(home_dir)

logging.basicConfig(filename=os.path.expanduser('~')+'/.bwg/'+'wallpaper.log',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

region_code = {'en-us': 'US', 'en-ca': 'Canada - English', 'en-au': 'Australia', 'en-uk': 'United Kingdom',
               'en-in': 'India', 'de-de': 'Germany', 'ja-jp': 'Japan', 'zh-cn': 'China', 'fr-fr': 'France',
               'fr-ca': 'Canada - French', 'en-ww': 'International'}


class BeengpaperApp(rumps.App):
    current_wallpaper_hsh = ""
    region = 'en-ww'
    name = 'No wallpaper downloaded'
    copyright = 'No wallpaper downloaded'

    def __init__(self):

        super(BeengpaperApp, self).__init__("Beengpaper")

        if os.path.exists(home_dir + '/config.json'):
            config = json.load(open(home_dir + '/config.json'))
            self.region = config['region']
            self.current_wallpaper_hsh = config['current_wallpaper_hsh']
            self.name = config['name']
            self.copyright = config['copyright']


        self.menu = ["About Image", "Image Title", "Image Copyright",separator,"Region",separator,"About Beengpaper"]
        self.icon = 'icon.png'
        self.template = True

        print_button = self.menu['Image Copyright']
        print_button.title = self.copyright
        title_button = self.menu['Image Title']
        title_button.title = self.name

        self.menu['Region'].add(MenuItem('US', callback=lambda sender: self.set_region('en-us',sender)))
        self.menu['Region'].add(MenuItem('Germany', callback=lambda sender: self.set_region('de-de',sender)))
        self.menu['Region'].add(MenuItem('Australia', callback=lambda sender: self.set_region('en-au',sender)))
        self.menu['Region'].add(MenuItem('Canada - English', callback=lambda sender: self.set_region('en-ca',sender)))
        self.menu['Region'].add(MenuItem('Canada - French', callback=lambda sender: self.set_region('fr-ca',sender)))
        self.menu['Region'].add(MenuItem('United Kingdom', callback=lambda sender: self.set_region('en-uk',sender)))
        self.menu['Region'].add(MenuItem('India', callback=lambda sender: self.set_region('en-in',sender)))
        self.menu['Region'].add(MenuItem('France', callback=lambda sender: self.set_region('fr-fr',sender)))
        self.menu['Region'].add(MenuItem('Japan', callback=lambda sender: self.set_region('ja-jp',sender)))
        self.menu['Region'].add(MenuItem('China', callback=lambda sender: self.set_region('zh-cn',sender)))
        self.menu['Region'].add(MenuItem('International', callback=lambda sender: self.set_region('en-ww',sender)))

        self.menu['Region'].title = 'Region (%s)' % region_code[self.region]
        logging.info('Starting app')

        t = Timer(30.0, self.get_new_wallpaper)
        t.start()
        self.get_new_wallpaper()

    @rumps.clicked("About Beengpaper")
    def about(self, _):
        window = rumps.alert(title='Beengpaper', message='Get your daily dose of Bing wallpapers on your desktop\nCopyright © 2019 Antoni Sobkowicz / Dragonshorn Studios', ok=None, cancel=None, icon_path='app_icon.png')
        window.run()

    def get_new_wallpaper(self):
        url = base_wallpaper_url + self.region
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        logging.info('Getting new wallpaper... ' + data['images'][0]['hsh'] + ' ' + data['images'][0]['url'])
        if self.current_wallpaper_hsh != data['images'][0]['hsh']:
            try:
                try:
                    os.remove(home_dir + "/wallpaper.png")
                except:
                    pass
                try:
                    os.remove(home_dir + "/wallpaper"+self.current_wallpaper_hsh+".png")
                except:
                    pass

                logging.info('Downloading wallpaper ' + data['images'][0]['url'])
                urllib.request.urlretrieve('http://www.bing.com' + data['images'][0]['url'], home_dir + "/wallpaper_"+data['images'][0]['hsh']+".png")

                self.current_wallpaper_hsh = data['images'][0]['hsh']
                logging.info('Setting wallpaper')

                se = app('System Events')
                desktops = se.desktops.display_name.get()
                for d in desktops:
                    desk = se.desktops[its.display_name == d]
                    desk.picture.set(mactypes.File(home_dir + "/wallpaper_" + self.current_wallpaper_hsh + ".png"))

                print_button = self.menu['Image Copyright']
                print_button.title = data['images'][0]["copyright"]
                self.copyright = data['images'][0]["copyright"]
                title_button = self.menu['Image Title']
                title_button.title = data['images'][0]["title"]
                self.name = data['images'][0]["title"]

                rumps.notification("You've got a new wallpaper!", data['images'][0]["title"], data['images'][0]["copyright"])
                logging.info("You've got a new wallpaper! " + data['images'][0]["title"] + ' ' + data['images'][0]["copyright"])

                self.save_config()

                pass
            except Exception as ex:
                logging.info('Error on ' + str(ex))
        else:
            logging.info('Not updating wallpaper')
        pass

    def set_region(self,name,menu):
        self.region = name
        self.menu['Region'].title = 'Region (%s)' % region_code[self.region]
        self.get_new_wallpaper()
        self.save_config()
        pass

    def save_config(self):
        config = {'region': self.region, 'current_wallpaper_hsh': self.current_wallpaper_hsh,'name':self.name,'copyright':self.copyright}
        json.dump(config, open(home_dir + '/config.json','w'))

        logging.info('Saved configuration data')
        pass


if __name__ == "__main__":
    BeengpaperApp().run()