#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   jamcalibre.py por: Flavio Danesse fdanesse@gmail.com
#   https://sites.google.com/site/flaviodanesse/
#   https://sites.google.com/site/sugaractivities/
#   http://codigosdeejemplo.blogspot.com/
#   CeibalJAM! - Uruguay - Activity Central - Sugar Labs
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from sugar.activity import activity
import sys
import os
import gobject

import gtk, pygtk
pygtk.require("2.0")

from sugar import env

#sys.path.insert(0, '/home/olpc/Activities/JAMCalibre.activity')

class jamcalibre(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle, False)
	self.bundle_path = activity.get_bundle_path()

        try:
            self.desktop_parent = gtk.EventBox()
            self.desktop_parent.show()
            self.set_canvas(self.desktop_parent)
        except AttributeError:
            for widget in self.get_children():
                self.remove(widget)
            self.desktop_parent = self

	self.show_all()

        os.environ['LD_LIBRARY_PATH'] = "%s:%s" % (os.path.join(self.bundle_path, 'lib'), os.environ.get('LD_LIBRARY_PATH', ''))
        os.environ['PATH'] = "%s:%s" % (os.path.join(self.bundle_path, 'bin'), os.environ.get('PATH', ''))

	sys.stdout.flush() 
	os.execvp("calibre", [])



