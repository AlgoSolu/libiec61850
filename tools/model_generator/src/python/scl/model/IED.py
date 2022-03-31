#!/usr/bin/env python
""" generated source for module IED """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013, 2014 Michael Zillgith
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
class IED(object):
    """ generated source for class IED """
    name = None
    accessPoints = None
    typeDeclarations = None
    self = None

    def __init__(self, iedNode, typeDeclarations):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(iedNode, "name")
        self = iedNode
        accessPointNodes = ParserUtils.getChildNodesWithTag(iedNode, "AccessPoint")
        self.accessPoints = LinkedList()
        for accessPointNode in accessPointNodes:
            self.accessPoints.add(AccessPoint(accessPointNode, typeDeclarations))
        self.typeDeclarations = typeDeclarations

    def getTypeDeclarations(self):
        """ generated source for method getTypeDeclarations """
        return self.typeDeclarations

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getAccessPoints(self):
        """ generated source for method getAccessPoints """
        return self.accessPoints

    def getAccessPointByName(self, name):
        """ generated source for method getAccessPointByName """
        for ap in accessPoints:
            if ap.__name__ == name:
                return ap
        return None

    def getFirstAccessPoint(self):
        """ generated source for method getFirstAccessPoint """
        return self.accessPoints.get(0)

    def getServices(self):
        """ generated source for method getServices """
        servicesNode = ParserUtils.getChildNodeWithTag(self, "Services")
        if servicesNode != None:
            return Services(servicesNode)
        else:
            return None

