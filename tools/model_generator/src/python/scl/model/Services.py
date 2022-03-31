#!/usr/bin/env python
""" generated source for module Services """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013-2020 Michael Zillgith
#  *
#  *  This file is part of libIEC61850.
#  *
#  *  libIEC61850 is free software: you can redistribute it and/or modify
#  *  it under the terms of the GNU General Public License as published by
#  *  the Free Software Foundation, either version 3 of the License, or
#  *  (at your option) any later version.
#  *
#  *  libIEC61850 is distributed in the hope that it will be useful,
#  *  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  *  GNU General Public License for more details.
#  *
#  *  You should have received a copy of the GNU General Public License
#  *  along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
#  *
#  *  See COPYING file for the complete license text.
#  
class Services(object):
    """ generated source for class Services """
    self = None

    def __init__(self, servicesNode):
        """ generated source for method __init__ """
        self = servicesNode

    def getReportSettings(self):
        """ generated source for method getReportSettings """
        reportSettingsNode = ParserUtils.getChildNodeWithTag(self, "ReportSettings")
        if reportSettingsNode != None:
            return ReportSettings(reportSettingsNode)
        return None

