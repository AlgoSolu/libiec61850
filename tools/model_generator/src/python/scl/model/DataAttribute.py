#!/usr/bin/env python
""" generated source for module DataAttribute """
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
class DataAttribute(DataModelNode):
    """ generated source for class DataAttribute """
    name = None
    fc = None
    type_ = None
    isBasicAttribute = True
    count = int()
    value = None
    shortAddress = None
    parent = None
    subDataAttributes = None
    sclType = None
    triggerOptions = None
    definition = None

    def __init__(self, daDefinition, typeDeclarations, fc, parent):
        """ generated source for method __init__ """
        super(DataAttribute, self).__init__()
        self.name = daDefinition.__name__
        self.fc = daDefinition.getFc()
        self.type_ = daDefinition.getAttributeType()
        self.count = daDefinition.getCount()
        self.parent = parent
        self.definition = daDefinition
        if self.fc == None:
            self.fc = fc
        if fc != None:
            self.fc = fc
        if (parent != None) and (isinstance(parent, (DataAttribute, ))):
            self.triggerOptions = (parent).getTriggerOptions()
        else:
            self.triggerOptions = daDefinition.getTriggerOptions()
        if self.type_ == AttributeType.CONSTRUCTED:
            self.isBasicAttribute = False
            createConstructedAttribute(daDefinition, typeDeclarations)
        elif self.type_ == AttributeType.ENUMERATED:
            createEnumeratedAttribute(daDefinition, typeDeclarations)

    def createEnumeratedAttribute(self, daDefinition, typeDeclarations):
        """ generated source for method createEnumeratedAttribute """
        self.sclType = typeDeclarations.lookupType(daDefinition.getType())
        if self.sclType == None:
            raise SclParserException("Missing type definition for enumerated data attribute: " + daDefinition.getbType())
        if not (isinstance(, (EnumerationType, ))):
            raise SclParserException("Wrong type definition for enumerated data attribute")
        self.sclType.setUsed(True)

    def createConstructedAttribute(self, daDefinition, typeDeclarations):
        """ generated source for method createConstructedAttribute """
        self.sclType = typeDeclarations.lookupType(daDefinition.getType(), DataAttributeType.__class__)
        if self.sclType == None:
            raise SclParserException("Missing type definition for constructed data attribute: " + daDefinition.getbType())
        if not (isinstance(, (DataAttributeType, ))):
            raise SclParserException("Wrong type definition for constructed data attribute")
        self.sclType.setUsed(True)
        dataAttributeType = self.sclType
        daDefinitions = dataAttributeType.getSubDataAttributes()
        self.subDataAttributes = LinkedList()
        for daDef in daDefinitions:
            self.subDataAttributes.add(DataAttribute(daDef, typeDeclarations, self.fc, self))

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getFc(self):
        """ generated source for method getFc """
        return self.fc

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def getSubDataAttributes(self):
        """ generated source for method getSubDataAttributes """
        return self.subDataAttributes

    def isBasicAttribute(self):
        """ generated source for method isBasicAttribute """
        return self.isBasicAttribute

    def getCount(self):
        """ generated source for method getCount """
        return self.count

    def getChildByName(self, childName):
        """ generated source for method getChildByName """
        for dataAttribute in subDataAttributes:
            if dataAttribute.__name__ == childName:
                return dataAttribute
        return None

    def getSclType(self):
        """ generated source for method getSclType """
        return self.sclType

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def setValue(self, value):
        """ generated source for method setValue """
        self.value = value

    def getShortAddress(self):
        """ generated source for method getShortAddress """
        return self.shortAddress

    def setShortAddress(self, shortAddress):
        """ generated source for method setShortAddress """
        self.shortAddress = shortAddress

    def getTriggerOptions(self):
        """ generated source for method getTriggerOptions """
        return self.triggerOptions

    def getDefinition(self):
        """ generated source for method getDefinition """
        return self.definition

    def getParent(self):
        """ generated source for method getParent """
        return self.parent

