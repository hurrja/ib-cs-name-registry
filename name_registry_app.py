# Copyright (C) 2025 Jarmo Hurri

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https:#www.gnu.org/licenses/>.

# application class
from user_interface import UserInterface
from name_register import NameRegister

class NameRegistryApp:
    def __init__(self):
        self.ui = UserInterface()
        self.name_register = NameRegister()

    # application logic
    def run(self):
        names = self.ui.read_names(); # read names from user
        self.name_register.set_names(names) # store names into register
        self.ui.show_names(self.name_register.get_names()) # show names in register to user

app = NameRegistryApp()
app.run()
