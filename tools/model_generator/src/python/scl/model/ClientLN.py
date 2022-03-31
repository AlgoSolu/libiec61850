#!/usr/bin/env python
""" generated source for module ClientLN """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013-2019 Michael Zillgith, MZ Automation GmbH
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
class ClientLN(object):
    """ generated source for class ClientLN """
    node = None

    def __init__(self, node):
        """ generated source for method __init__ """
        self.node = node

    def getIedName(self):
        """ generated source for method getIedName """
        return ParserUtils.parseAttribute(self.node, "iedName")

    def getApRef(self):
        """ generated source for method getApRef """
        return ParserUtils.parseAttribute(self.node, "apRef")

    def getLdInst(self):
        """ generated source for method getLdInst """
        return ParserUtils.parseAttribute(self.node, "ldInst")

    def getPrefix(self):
        """ generated source for method getPrefix """
        return ParserUtils.parseAttribute(self.node, "prefix")

    def getLnClass(self):
        """ generated source for method getLnClass """
        return ParserUtils.parseAttribute(self.node, "lnClass")

    def getLnInst(self):
        """ generated source for method getLnInst """
        return ParserUtils.parseAttribute(self.node, "lnInst")

    def getDesc(self):
        """ generated source for method getDesc """
        return ParserUtils.parseAttribute(self.node, "desc")

