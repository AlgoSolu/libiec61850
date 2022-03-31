#!/usr/bin/env python
""" generated source for module AccessPoint """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  AccessPoint.java
#  *
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
class AccessPoint(object):
    """ generated source for class AccessPoint """
    name = None
    server = None

    def __init__(self, apNode, typeDeclarations):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(apNode, "name")
        if self.name == None:
            raise SclParserException(apNode, "AccessPoint as no name defined!")
        serverNode = ParserUtils.getChildNodeWithTag(apNode, "Server")
        if serverNode == None:
            self.server = None
        else:
            self.server = Server(serverNode, typeDeclarations)

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getServer(self):
        """ generated source for method getServer """
        return self.server

