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

class UserInterface:
    # returns a name read from user, None if user inputs empty line
    def read_name(self):
        name = input()
        if name == '':
            return None
        else:
            return name

    # returns a list of names read from the user
    def read_names(self):
        print('type names be saved in registry (one per line, empty line ends):')
        # code to be written here; use read_name()
        return [] # this line must also be deleted

    # prints names, each name on a separate line
    def show_names(self, names):
        # code to be written here
        pass
