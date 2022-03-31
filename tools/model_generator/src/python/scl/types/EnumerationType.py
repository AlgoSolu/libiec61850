#!/usr/bin/env python
""" generated source for module EnumerationType """
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
class EnumerationType(SclType):
    """ generated source for class EnumerationType """
    enumValues = None

    @overloaded
    def __init__(self, xmlNode):
        """ generated source for method __init__ """
        super(EnumerationType, self).__init__(xmlNode)
        parseEnumerationValueNodes(xmlNode)

    @__init__.register(object, str)
    def __init___0(self, name):
        """ generated source for method __init___0 """
        super(EnumerationType, self).__init__(None)
        self.enumValues = LinkedList()

    @classmethod
    def getDefaultEnumTypes(cls):
        """ generated source for method getDefaultEnumTypes """
        defaultTypes = LinkedList()
        return defaultTypes

    def addEnumValue(self, enumValue):
        """ generated source for method addEnumValue """
        self.enumValues.add(enumValue)

    def parseEnumerationValueNodes(self, enumTypeNode):
        """ generated source for method parseEnumerationValueNodes """
        elements = enumTypeNode.getChildNodes()
        if elements != None:
            self.enumValues = LinkedList()
            enumValueNode = None
            i = 0
            while i < elements.getLength():
                enumValueNode = elements.item(i)
                if enumValueNode.getNodeName() == "EnumVal":
                    self.enumValues.add(EnumerationValue(enumValueNode))
                i += 1

    def getOrdByEnumString(self, enumString):
        """ generated source for method getOrdByEnumString """
        for value in enumValues:
            if value.getSymbolicName() == enumString:
                return value.getOrd()
        raise IllegalValueException("Enum has no value " + enumString)

    def isValidOrdValue(self, ordValue):
        """ generated source for method isValidOrdValue """
        for enumValue in enumValues:
            if enumValue.getOrd() == ordValue:
                return True
        return False

