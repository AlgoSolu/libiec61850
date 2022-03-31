#!/usr/bin/env python
""" generated source for module EnumerationValue """
from __future__ import print_function
# package: com.libiec61850.scl.types
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
class EnumerationValue(object):
    """ generated source for class EnumerationValue """
    symbolicName = None
    ord = int()

    @overloaded
    def __init__(self, symbolicName, ord):
        """ generated source for method __init__ """
        self.symbolicName = symbolicName
        self.ord = ord

    @__init__.register(object, Node)
    def __init___0(self, xmlNode):
        """ generated source for method __init___0 """
        ordString = ParserUtils.parseAttribute(xmlNode, "ord")
        if ordString == None:
            raise SclParserException(xmlNode, "ord attribute missing")
        self.ord = int(ordString)
        self.symbolicName = xmlNode.getTextContent()

    def getSymbolicName(self):
        """ generated source for method getSymbolicName """
        return self.symbolicName

    def getOrd(self):
        """ generated source for method getOrd """
        return self.ord

