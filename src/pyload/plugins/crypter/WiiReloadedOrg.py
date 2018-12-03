# -*- coding: utf-8 -*-

from ..internal.deadcrypter import DeadCrypter


class WiiReloadedOrg(DeadCrypter):
    __name__ = "WiiReloadedOrg"
    __type__ = "crypter"
    __version__ = "0.16"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?wii-reloaded\.org/protect/get\.php\?i=.+"
    __config__ = [("enabled", "bool", "Activated", True)]

    __description__ = """Wii-Reloaded.org decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("hzpz", None)]