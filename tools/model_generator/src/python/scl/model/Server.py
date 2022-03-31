#!/usr/bin/env python
""" generated source for module Server """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013 Michael Zillgith
#  *
#  *	This file is part of libIEC61850.
#  *
#  *	libIEC61850 is free software: you can redistribute it and/or modify
#  *	it under the terms of the GNU General Public License as published by
#  *	the Free Software Foundation, either version 3 of the License, or
#  *	(at your option) any later version.
#  *
#  *	libIEC61850 is distributed in the hope that it will be useful,
#  *	but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  *	GNU General Public License for more details.
#  *
#  *	You should have received a copy of the GNU General Public License
#  *	along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
#  *
#  *	See COPYING file for the complete license text.
#  
class Server(object):
    """ generated source for class Server """
    authentication = None
    logicalDevices = None

    def __init__(self, serverNode, typeDeclarations):
        """ generated source for method __init__ """
        authenticationNode = ParserUtils.getChildNodeWithTag(serverNode, "Authentication")
        if authenticationNode != None:
            self.authentication = Authentication(authenticationNode)
        ldNodes = ParserUtils.getChildNodesWithTag(serverNode, "LDevice")
        if len(ldNodes) == 0:
            raise SclParserException(serverNode, "No logical devices defined for AccessPoint")
        self.logicalDevices = LinkedList()
        for ldNode in ldNodes:
            self.logicalDevices.add(LogicalDevice(ldNode, typeDeclarations))

    def getAuthentication(self):
        """ generated source for method getAuthentication """
        return self.authentication

    def getLogicalDevices(self):
        """ generated source for method getLogicalDevices """
        return self.logicalDevices

