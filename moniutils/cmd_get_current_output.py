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


from collections import namedtuple
from Xlib import X, protocol, display
from Xlib.ext import randr


Point = namedtuple('Point', ['x', 'y'])


def main_entrypoint():
    dpy = display.Display()
    scr = dpy.screen()
    res = randr.get_screen_resources(scr.root)
    pointer = scr.root.query_pointer()

    pos = Point(pointer.root_x, pointer.root_y)

    for output in res.outputs:
        output_info = randr.get_output_info(dpy, output, 0)
        if output_info.crtc:
            crtc_info = randr.get_crtc_info(dpy, output_info.crtc, 0)

            match = (crtc_info.x <= pos.x and
                     crtc_info.y <= pos.y and
                     pos.x < crtc_info.x + crtc_info.width and
                     pos.y < crtc_info.y + crtc_info.height)

            if match:
                print(output_info.name)
                break


# for crtc in res.crtcs:
#     info = randr.get_crtc_info(dpy, crtc, 0)
#     if info.outputs:
#         output_info = randr.get_output_info(dpy, info.outputs[0], 0)
#         print(output_info)
#         match = (info.x <= pos.x and
#                  info.y <= pos.y and
#                  pos.x < info.x + info.width and
#                  pos.y < info.y + info.height)
#         if match:
#             print(output_info.name)
#             break

# EOF #
