#!/usr/bin/env python3

# moniutils - Monitor Utilities for X11
# Copyright (C) 2022 Ingo Ruhnke <grumbel@gmail.com>
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


from setuptools import setup, find_packages


setup(name='moniutils',
      version='0.1.0',
      scripts=[],
      entry_points={
          'console_scripts': [
              'moniutils-get-current-output = moniutils.cmd_get_current_output:main_entrypoint',
          ]},
      install_requires=[
          'python-xlib',
      ],
      packages=['moniutils'],
)


# EOF #
