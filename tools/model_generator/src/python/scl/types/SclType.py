#!/usr/bin/env python
""" generated source for module SclType """
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
class SclType(object):
    """ generated source for class SclType """
    id = None
    description = None
    isUsed = False

    @overloaded
    def __init__(self, xmlNode):
        """ generated source for method __init__ """
        self.id = ParserUtils.parseAttribute(xmlNode, "id")
        self.description = ParserUtils.parseAttribute(xmlNode, "desc")
        if self.id == None:
            raise SclParserException(xmlNode, "id is missing!")

    @__init__.register(object, str, str)
    def __init___0(self, id, description):
        """ generated source for method __init___0 """
        self.id = id
        self.description = description

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getDesc(self):
        """ generated source for method getDesc """
        return self.description

    def setUsed(self, isUsed):
        """ generated source for method setUsed """
        self.isUsed = isUsed

    def isUsed(self):
        """ generated source for method isUsed """
        return self.isUsed

