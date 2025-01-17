# Copyright (C) 2018-2019 Red Hat, Inc.
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
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""Utilities for Bodhi's message schemas."""


def truncate(title: str) -> str:
    """
    Truncate the string to 40 characters and adds ellipsis.

    Args:
        title: The string you wish to truncate.
    Returns:
        The truncated string.
    """
    if len(title) >= 40:
        title = title[:40] + "…"
    return title


# Keep this in sync with bodhi.server.util.MENTION_RE
# (enhancement: create a bodhi-common package that every subpackage
# would depend on and put it there)
MENTION_RE = r'(?<!\S)(@\w+)'
