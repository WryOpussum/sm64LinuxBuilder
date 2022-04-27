import sys
import gi
from gi.repository import Gtk
from gi.repository import Adw
from gi.repository import Notify
from gi.repository import Gio
from pathlib import Path
import os
from romSelectionStorage import *

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
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        self.show()

     def dialog_response(self, widget, response):

        if response == Gtk.ResponseType.OK:
            glocalfile = self.get_file()
            RomDir = "{glocalfile.get_path}"
            print(f'Selected Rom: {glocalfile.get_basename()}')
            print(f'Selected Rom Path: {glocalfile.get_path()}')
            os.system(f'cp -r {glocalfile.get_path()} baserom.us.z64')

        widget.close()

