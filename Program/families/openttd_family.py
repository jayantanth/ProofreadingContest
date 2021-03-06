# -*- coding: utf-8  -*-

__version__ = '$Id: openttd_family.py 10828 2012-12-23 20:59:00Z drtrigon $'

import family

# The project wiki of OpenTTD, an open source game (Transport Tycoon Deluxe clone).

class Family(family.Family):

    def __init__(self):
        family.Family.__init__(self)
        self.name = 'openttd'
        self.langs = {
            'en': 'wiki.openttd.org',
        }

        self.namespaces[4] = {
            '_default': [u'OpenTTD', self.namespaces[4]['_default']],
        }
        self.namespaces[5] = {
            '_default': [u'OpenTTD talk', self.namespaces[5]['_default']],
        }
        self.namespaces[100] = {
            '_default': u'Manual',
        }
        self.namespaces[101] = {
            '_default': u'Development',
        }

    def scriptpath(self, code):
        return ''

    def version(self, code):
        return "1.12.0"

    def apipath(self, code):
        raise NotImplementedError(
            "The openttd family does not support api.php")
