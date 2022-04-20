#!/usr/bin/python

import sys
import gi
import os
import logging
import asyncio
import threading
gi.require_version('Notify', '0.7')
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Notify, Gtk, Adw, Gio


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #window setup
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)       
        self.set_default_size(700, 500)
        self.set_title("sm64LinuxBuilder")
        
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)


        








        #notification setup


        Notify.init("sm64LinuxBuilder")
        global n
        n = Notify.Notification.new("sm64LinuxBuilder", "Build Complete!")

          
        
        #flap//pane
        
        flap_Toggle_button = Gtk.ToggleButton.new()
        flap_Toggle_button.set_icon_name(icon_name='sidebar-show-symbolic')
        flap_Toggle_button.connect('clicked', self.on_flap_button_toggled)
        self.header.pack_start(child=flap_Toggle_button)

        self.adw_flap = Adw.Flap.new()
        self.adw_flap.set_reveal_flap(reveal_flap=True)
        self.adw_flap.set_locked(locked=True)
        self.box1.append(child=self.adw_flap)
        stack = Gtk.Stack.new()
        self.adw_flap.set_content(content=stack)

        
        #model for menu for compilation speeds
        
        action = Gio.SimpleAction.new("fastest", None)
        action.connect("activate", self.Fastest)
        self.add_action(action)
        
        action = Gio.SimpleAction.new("normal", None)
        action.connect("activate", self.Normal)
        self.add_action(action)
        
        action = Gio.SimpleAction.new("slow", None)
        action.connect("activate", self.Slow)
        self.add_action(action)
        
        
        global menu
        menu = Gio.Menu.new()
        menu.append("Slow", "win.slow")
        menu.append("Normal", "win.normal")
        menu.append("Fastest", "win.fastest")
        
        
        
        
        
        #pane entries
        
        
        
        
        #sm64-ex
        
        box_page_1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_1, name='sm64ex', title='sm64ex')
        
        
        build_page_1 = Adw.SplitButton(label="Start Compilation")
        build_page_1.set_menu_model(menu)
        build_page_1.set_halign(align=Gtk.Align.CENTER)
        build_page_1.set_valign(align=Gtk.Align.START)
        build_page_1.set_hexpand(expand=True)
        build_page_1.set_vexpand(expand=True)
        launch_page_1 = Gtk.Button(label="Launch")
        launch_page_1.set_halign(align=Gtk.Align.CENTER)
        launch_page_1.set_valign(align=Gtk.Align.START)
        launch_page_1.set_hexpand(expand=True)
        launch_page_1.set_vexpand(expand=True)
        
        description_page_1 = Gtk.Label.new(str='Sm64ex is generic mario 64 with quality of life features.')
        description_page_1.set_halign(align=Gtk.Align.CENTER)
        description_page_1.set_valign(align=Gtk.Align.END)
        description_page_1.set_hexpand(expand=True)
        description_page_1.set_vexpand(expand=True)
        
        box_page_1.append(child=description_page_1)
        box_page_1.append(child=build_page_1)
        box_page_1.append(child=launch_page_1)
        build_page_1.connect('clicked', self.compileSm64ex)
        launch_page_1.connect('clicked', self.launchSm64ex)
        
        
        
        
        
        
        
        
        
        #sm64-ex-coop
        
        box_page_2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_2, name='Sm64ex-coop', title='sm64ex-coop')

        build_page_2 = Adw.SplitButton(label="Start Compilation")
        build_page_2.set_menu_model(menu)
        build_page_2.set_halign(align=Gtk.Align.CENTER)
        build_page_2.set_valign(align=Gtk.Align.START)
        build_page_2.set_hexpand(expand=True)
        build_page_2.set_vexpand(expand=True)
        
        launch_page_2 = Gtk.Button(label="Launch")
        launch_page_2.set_halign(align=Gtk.Align.CENTER)
        launch_page_2.set_valign(align=Gtk.Align.START)
        launch_page_2.set_hexpand(expand=True)
        launch_page_2.set_vexpand(expand=True)
        
        description_page_2 = Gtk.Label.new(str='sm64ex-coop is a fork of sm64ex with Online Multiplayer!')
        description_page_2.set_halign(align=Gtk.Align.CENTER)
        description_page_2.set_valign(align=Gtk.Align.END)
        description_page_2.set_hexpand(expand=True)
        description_page_2.set_vexpand(expand=True)
        
        box_page_2.append(child=description_page_2)
        box_page_2.append(child=build_page_2)
        box_page_2.append(child=launch_page_2)
        build_page_2.connect('clicked', self.compileSm64excoop)
        launch_page_2.connect('clicked', self.launchSm64excoop)
        
        #Render96
        
        box_page_3 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_3, name='Render96', title='Render96')

        build_page_3 = Adw.SplitButton(label="Start Compilation")
        build_page_3.set_menu_model(menu)
        build_page_3.set_halign(align=Gtk.Align.CENTER)
        build_page_3.set_valign(align=Gtk.Align.START)
        build_page_3.set_hexpand(expand=True)
        build_page_3.set_vexpand(expand=True)
        
        launch_page_3 = Gtk.Button(label="Launch")
        launch_page_3.set_halign(align=Gtk.Align.CENTER)
        launch_page_3.set_valign(align=Gtk.Align.START)
        launch_page_3.set_hexpand(expand=True)
        launch_page_3.set_vexpand(expand=True)
        
        description_page_3 = Gtk.Label.new(str='Render96 is a fork of sm64ex with Dynos and models!')
        description_page_3.set_halign(align=Gtk.Align.CENTER)
        description_page_3.set_valign(align=Gtk.Align.END)
        description_page_3.set_hexpand(expand=True)
        description_page_3.set_vexpand(expand=True)
        
        box_page_3.append(child=description_page_3)
        box_page_3.append(child=build_page_3)
        box_page_3.append(child=launch_page_3)
        build_page_3.connect('clicked', self.compileRender96)
        launch_page_3.connect('clicked', self.launchRender96)
        
        #sm64 plus
        
        box_page_4 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_4, name='sm64plus', title='sm64plus')


        build_page_4 = Adw.SplitButton(label="Start Compilation")
        build_page_4.set_menu_model(menu)
        build_page_4.set_halign(align=Gtk.Align.CENTER)
        build_page_4.set_valign(align=Gtk.Align.START)
        build_page_4.set_hexpand(expand=True)
        build_page_4.set_vexpand(expand=True)
        launch_page_4 = Gtk.Button(label="Launch")
        launch_page_4.set_halign(align=Gtk.Align.CENTER)
        launch_page_4.set_valign(align=Gtk.Align.START)
        launch_page_4.set_hexpand(expand=True)
        launch_page_4.set_vexpand(expand=True)
        
        description_page_4 = Gtk.Label.new(str='Mario 64 with neat diffrences like extended movesets.')
        description_page_4.set_halign(align=Gtk.Align.CENTER)
        description_page_4.set_valign(align=Gtk.Align.END)
        description_page_4.set_hexpand(expand=True)
        description_page_4.set_vexpand(expand=True)
        
        box_page_4.append(child=description_page_4)
        box_page_4.append(child=build_page_4)
        box_page_4.append(child=launch_page_4)
        build_page_4.connect('clicked', self.compileSm64plus)
        launch_page_4.connect('clicked', self.launchSm64plus)


        #Moon64
        box_page_5 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_5, name='Moon64', title='Moon64')


        build_page_5 = Adw.SplitButton(label="Start Compilation")
        build_page_5.set_menu_model(menu)
        build_page_5.set_halign(align=Gtk.Align.CENTER)
        build_page_5.set_valign(align=Gtk.Align.START)
        build_page_5.set_hexpand(expand=True)
        build_page_5.set_vexpand(expand=True)
        launch_page_5 = Gtk.Button(label="Launch")
        launch_page_5.set_halign(align=Gtk.Align.CENTER)
        launch_page_5.set_valign(align=Gtk.Align.START)
        launch_page_5.set_hexpand(expand=True)
        launch_page_5.set_vexpand(expand=True)

        description_page_5 = Gtk.Label.new(str='Mario 64 with achivements!.')
        description_page_5.set_halign(align=Gtk.Align.CENTER)
        description_page_5.set_valign(align=Gtk.Align.END)
        description_page_5.set_hexpand(expand=True)
        description_page_5.set_vexpand(expand=True)

        box_page_5.append(child=description_page_5)
        box_page_5.append(child=build_page_5)
        box_page_5.append(child=launch_page_5)
        build_page_5.connect('clicked', self.compileMoon64)
        launch_page_5.connect('clicked', self.launchMoon64)





        # Sidebar
        
        stack_sidebar = Gtk.StackSidebar.new()
        stack_sidebar.set_stack(stack=stack)
        self.adw_flap.set_flap(flap=stack_sidebar)
        
    def on_flap_button_toggled(self, widget):
        self.adw_flap.set_reveal_flap(not self.adw_flap.get_reveal_flap())

        #Headerbar menu
        
        #entries
        
        
        
    global compilationSpeed
    compilationSpeed = " -j2"
    
    
    def launchSm64ex(self, menu):

            os.system('./sm64ex/build/us_pc/sm64.us.f3dex2e ')

    def launchSm64plus(self, menu):
            
            os.system('cd sm64plus/build/us_pc ./sm64plus/build/us_pc/sm64.us.f3dex2e ')
            
    def launchSm64excoop(self, menu):         
            
            os.system('cd sm64ex-coop/build/us_pc/ && ./sm64.us.f3dex2e ')
            
    def launchRender96(self, menu):         
            
            os.system('cd Render96ex/build/us_pc/ && ./sm64.us.f3dex2e ')
            
    def launchMoon64(self, menu):

            os.system('cd Moon64/build/us_pc/ && ./moon64.us.f3dex2e ')

    def compileMoon64(self, menu):

            print(compilationSpeed)
            os.system('git clone https://github.com/UnderVolt/Moon64.git && cp -r baserom.us.z64 Moon64 && cd Moon64 && make' + compilationSpeed)
            n.show()


    def compileSm64ex(self, menu):
            
            print(compilationSpeed)
            os.system('git clone https://github.com/sm64pc/sm64ex.git && cp -r baserom.us.z64 sm64ex && cd sm64ex && make' + compilationSpeed)
            n.show()
            
    def compileSm64plus(self, menu):
            
            print(compilationSpeed)
            os.system('git clone https://github.com/MorsGames/sm64plus.git && cp -r baserom.us.z64 sm64plus && cd sm64plus && make CUSTOM_TEXTURES=0' + compilationSpeed)
            n.show()

    def compileRender96(self, menu):
            
            print(compilationSpeed)
            os.system('git clone https://github.com/Render96/Render96ex.git --branch tester_rt64alpha && cp -r baserom.us.z64 Render96ex && cd Render96ex && make' + compilationSpeed)
            n.show()
    def compileSm64excoop(self, menu):
      
            print(compilationSpeed)
            os.system('git clone https://github.com/djoslin0/sm64ex-coop.git && cp -r baserom.us.z64 sm64ex-coop && cd sm64ex-coop && make' + compilationSpeed)

            n.show()


    def Fastest(self, action, param):
        global compilationSpeed
        compilationSpeed = " -j"
        print(compilationSpeed)
        
    def Normal(self, action, param):
        global compilationSpeed
        compilationSpeed = " -j2"
        print(compilationSpeed)
        
    def Slow(self, action, param):
        global compilationSpeed
        compilationSpeed = ""
        print(compilationSpeed)
    

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.github.WryOpussum.sm64LinuxBuilder")
app.run(sys.argv)
