#!/usr/bin/env python
""" generated source for module GSEControl """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013 Michael Zillgith
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
class GSEControl(object):
    """ generated source for class GSEControl """
    name = None
    desc = None
    dataSet = None
    confRev = 1
    appID = None
    fixedOffs = False

    def __init__(self, gseControlNode):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(gseControlNode, "name")
        self.desc = ParserUtils.parseAttribute(gseControlNode, "desc")
        self.dataSet = ParserUtils.parseAttribute(gseControlNode, "datSet")
        confRevString = ParserUtils.parseAttribute(gseControlNode, "confRev")
        if confRevString != None:
            self.confRev = int(confRevString)
        self.appID = ParserUtils.parseAttribute(gseControlNode, "appID")
        fixedOffs = ParserUtils.parseBooleanAttribute(gseControlNode, "fixedOffs")
        if fixedOffs != None:
            self.fixedOffs = fixedOffs
        typeString = ParserUtils.parseAttribute(gseControlNode, "type")
        if typeString != None:
            if not typeString == "GOOSE":
                raise SclParserException(gseControlNode, "GSEControl of type " + typeString + " not supported!")

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getDataSet(self):
        """ generated source for method getDataSet """
        return self.dataSet

    def getConfRev(self):
        """ generated source for method getConfRev """
        return self.confRev

    def getAppID(self):
        """ generated source for method getAppID """
        return self.appID

    def isFixedOffs(self):
        """ generated source for method isFixedOffs """
        return self.fixedOffs

