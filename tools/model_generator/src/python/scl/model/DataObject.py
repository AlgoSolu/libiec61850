#!/usr/bin/env python
""" generated source for module DataObject """
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
class DataObject(DataModelNode):
    """ generated source for class DataObject """
    name = None
    count = int()
    dataAttributes = None
    subDataObjects = None
    sclType = None
    parent = None
    trans = False

    def __init__(self, doDefinition, typeDeclarations, parent):
        """ generated source for method __init__ """
        super(DataObject, self).__init__()
        self.name = doDefinition.__name__
        self.count = doDefinition.getCount()
        self.parent = parent
        self.trans = doDefinition.isTransient()
        self.dataAttributes = LinkedList()
        self.subDataObjects = LinkedList()
        self.sclType = typeDeclarations.lookupType(doDefinition.getType(), DataObjectType.__class__)
        if self.sclType == None:
            raise SclParserException("type declaration missing for data object.")
        #  mark type as used 
        self.sclType.setUsed(True)
        createDataAttributes(typeDeclarations, self.sclType)
        createSubDataObjects(typeDeclarations, self.sclType)

    def createSubDataObjects(self, typeDeclarations, doType):
        """ generated source for method createSubDataObjects """
        sdoDefinitions = doType.getSubDataObjects()
        for sdoDefinition in sdoDefinitions:
            self.subDataObjects.add(DataObject(sdoDefinition, typeDeclarations, self))

    def createDataAttributes(self, typeDeclarations, sclType):
        """ generated source for method createDataAttributes """
        daDefinitions = None
        if isinstance(sclType, (DataObjectType, )):
            daDefinitions = (sclType).getDataAttributes()
        if isinstance(sclType, (DataAttributeType, )):
            daDefinitions = (sclType).getSubDataAttributes()
        for daDefinition in daDefinitions:
            if daDefinition.getFc() == FunctionalConstraint.SE:
                self.dataAttributes.add(DataAttribute(daDefinition, typeDeclarations, FunctionalConstraint.SG, self))
            self.dataAttributes.add(DataAttribute(daDefinition, typeDeclarations, None, self))

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getDataAttributes(self):
        """ generated source for method getDataAttributes """
        return self.dataAttributes

    def getSubDataObjects(self):
        """ generated source for method getSubDataObjects """
        return self.subDataObjects

    def getCount(self):
        """ generated source for method getCount """
        return self.count

    def isTransient(self):
        """ generated source for method isTransient """
        return self.trans

    def getChildByName(self, childName):
        """ generated source for method getChildByName """
        for dataAttribute in dataAttributes:
            if dataAttribute.__name__ == childName:
                return dataAttribute
        for dataObject in subDataObjects:
            if dataObject.__name__ == childName:
                return dataObject
        return None

    def getSclType(self):
        """ generated source for method getSclType """
        return self.sclType

    def getParent(self):
        """ generated source for method getParent """
        return self.parent

