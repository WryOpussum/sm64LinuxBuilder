# window.py
#
# Copyright 2022 WryOpussum
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk
from gi.repository import Adw
from gi.repository import Notify
from gi.repository import Gio
import os
from pathlib import Path


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




        #Header hamburger menu







        action = Gio.SimpleAction.new("fileChooser", None)
        action.connect("activate", self.fileChooser)
        self.add_action(action)  # Here the action is being added to the window, but you could add it to the
                                 # application or an "ActionGroup"


        # Create a new menu, containing that action
        Headermenu = Gio.Menu.new()
        Headermenu.append("Pick rom", "win.fileChooser")  # Or you would do app.something if you had attached the
                                                      # action to the application

        # Create a popover
        self.popover = Gtk.PopoverMenu()  # Create a new popover menu
        self.popover.set_menu_model(Headermenu)

        # Create a menu button
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")  # Give it a nice icon

        # Add menu button to the header bar
        self.header.pack_end(self.hamburger)






        #other menu for compilation
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

    def fileChooser(self, action, param):
        FileChooser(parent=self)

    global compilationSpeed
    compilationSpeed = " -j2"


    def launchSm64ex(self, menu):

            os.system('flatpak-spawn --host ./sm64ex/build/us_pc/sm64.us.f3dex2e ')

    def launchSm64plus(self, menu):

            os.system('flatpak-spawn --host cd sm64plus/build/us_pc ./sm64plus/build/us_pc/sm64.us.f3dex2e ')

    def launchSm64excoop(self, menu):

            os.system('flatpak-spawn --host cd sm64ex-coop/build/us_pc/ ./sm64.us.f3dex2e ')

    def launchRender96(self, menu):

            os.system('flatpak-spawn --hostcd Render96ex/build/us_pc/ ./sm64.us.f3dex2e ')

    def launchMoon64(self, menu):

            os.system('flatpak-spawn --host cd Moon64/build/us_pc/ ./moon64.us.f3dex2e ')

    def compileMoon64(self, menu):

            print(compilationSpeed)
            os.system('flatpak-spawn --host git clone https://github.com/UnderVolt/Moon64.git  && flatpak-spawn --host cp -r baserom.us.z64 Moon64 && flatpak-spawn --host cd Moon64 && flatpak-spawn --host make' + compilationSpeed)
            n.show()


    def compileSm64ex(self, menu):

            print(compilationSpeed)
            os.system(f'flatpak-spawn --host git clone https://github.com/sm64pc/sm64ex.git  && flatpak-spawn --host cp -r baserom.us.z64 sm64ex/baserom.us.z64 && flatpak-spawn --host cd sm64ex && flatpak-spawn --host make' + compilationSpeed)
            n.show()

    def compileSm64plus(self, menu):

            print(compilationSpeed)
            os.system('flatpak-spawn --host git clone https://github.com/MorsGames/sm64plus.git  && flatpak-spawn --host cp -r baserom.us.z64 sm64plus && flatpak-spawn --host cd sm64plus &&  flatpak-spawn --host make CUSTOM_TEXTURES=0' + compilationSpeed)
            n.show()

    def compileRender96(self, menu):

            print(compilationSpeed)
            os.system('flatpak-spawn --host git clone https://github.com/Render96/Render96ex.git  --branch tester_rt64alpha && flatpak-spawn --host cp -r baserom.us.z64 Render96ex && flatpak-spawn --host cd Render96ex && flatpak-spawn --host make' + compilationSpeed)
            n.show()
    def compileSm64excoop(self, menu):

            print(compilationSpeed)
            os.system('flatpak-spawn --host git clone https://github.com/djoslin0/sm64ex-coop.git  && flatpak-spawn --host cp -r baserom.us.z64 sm64ex-coop && flatpak-spawn --host cd sm64excoop make' + compilationSpeed)

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

class FileChooser(Gtk.FileChooserDialog):
     home = Path.home()

     def __init__(self, parent,):
        super().__init__(transient_for=parent, use_header_bar=True)

        self.set_action(action=Gtk.FileChooserAction.OPEN)
        title = 'Select'
        self.set_title(title=title)
        self.set_modal(modal=True)
        self.connect('response', self.dialog_response)
        self.set_current_folder(
            Gio.File.new_for_path(path=str(self.home)),
        )

        # Criando os botões que ficarão na barra de título (Gtk.HeaderBar()).
        self.add_buttons(
            '_Cancel', Gtk.ResponseType.CANCEL,
            '_Select', Gtk.ResponseType.OK
        )
        btn_select = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        # Adicionando estilo no botão.
        btn_select.get_style_context().add_class(class_name='suggested-action')
        btn_cancel = self.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )
        btn_cancel.get_style_context().add_class(class_name='normal-action')

        self.show()

     def dialog_response(self, widget, response):

        if response == Gtk.ResponseType.OK:
            glocalfile = self.get_file()
            print(f'Selected Rom: {glocalfile.get_basename()}')
            print(f'Selected Rom Path: {glocalfile.get_path()}')
            os.system(f'flatpak-spawn --host cp -r {glocalfile.get_path()} baserom.us.z64')

        widget.close()

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.github.WryOpussum.sm64LinuxBuilder")
app.run(sys.argv)
