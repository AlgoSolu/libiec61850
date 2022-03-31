#!/usr/bin/env python
""" generated source for module TypeDeclarations """
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
class TypeDeclarations(object):
    """ generated source for class TypeDeclarations """
    typeDeclarations = None

    def __init__(self):
        """ generated source for method __init__ """
        self.typeDeclarations = LinkedList()
        defaultEnumTypes = EnumerationType.getDefaultEnumTypes()
        for enumType in defaultEnumTypes:
            self.typeDeclarations.add(enumType)

    def addType(self, sclType):
        """ generated source for method addType """
        self.typeDeclarations.add(sclType)

    @overloaded
    def lookupType(self, typeId):
        """ generated source for method lookupType """
        for typeDeclaration in typeDeclarations:
            if typeDeclaration.getId() == typeId:
                return typeDeclaration
        print("Cannot find type " + typeId)
        return None

    @lookupType.register(object, str, Class)
    def lookupType_0(self, typeId, type_):
        """ generated source for method lookupType_0 """
        for typeDeclaration in typeDeclarations:
            if typeDeclaration.__class__ == type_:
                if typeDeclaration.getId() == typeId:
                    return typeDeclaration
        print("Cannot find type " + typeId)
        return None

    def getTypeDeclarations(self):
        """ generated source for method getTypeDeclarations """
        return self.typeDeclarations

