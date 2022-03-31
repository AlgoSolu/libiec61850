#!/usr/bin/env python
""" generated source for module SubNetwork """
from __future__ import print_function
# package: com.libiec61850.scl.communication
# 
#  *  Copyright 2013 Michael Zillgith
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
class SubNetwork(object):
    """ generated source for class SubNetwork """
    name = None
    type_ = None
    connectedAPs = None

    def __init__(self, netNode):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(netNode, "name")
        self.type_ = ParserUtils.parseAttribute(netNode, "type")
        if self.name == None:
            raise SclParserException(netNode, "SubNetwork is missing attribute name!")
        self.connectedAPs = LinkedList()
        nodes = ParserUtils.getChildNodesWithTag(netNode, "ConnectedAP")
        for node in nodes:
            self.connectedAPs.add(ConnectedAP(node))

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def getConnectedAPs(self):
        """ generated source for method getConnectedAPs """
        return self.connectedAPs

