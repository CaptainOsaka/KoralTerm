import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte, GLib

class TerminalWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="KoralTerm")
        self.set_default_size(800, 600)

        self.terminal = Vte.Terminal()
        self.terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,  # Flags
            None,  # Working directory
            ["/bin/bash"],  # Command
            [],  # Environment variables
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,  # Spawn flags
            None,  # Child setup function
            None,  # Child setup data
            None  # Child setup data destroy notify
        )

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_vexpand(True)
        self.scrolled_window.set_hexpand(True)
        self.scrolled_window.add(self.terminal)

        self.add(self.scrolled_window)

win = TerminalWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
