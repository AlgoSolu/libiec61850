#!/usr/bin/env python
""" generated source for module DataModelNode """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
# package: com.libiec61850.scl.model
# 
#  *  DataModelNode.java
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
class DataModelNode(object):
    """ generated source for interface DataModelNode """
    __metaclass__ = ABCMeta
    @abstractmethod
    def getName(self):
        """ generated source for method getName """

    @abstractmethod
    def getChildByName(self, childName):
        """ generated source for method getChildByName """

    @abstractmethod
    def getSclType(self):
        """ generated source for method getSclType """

    @abstractmethod
    def getParent(self):
        """ generated source for method getParent """

