#!/usr/bin/env python
""" generated source for module SettingControl """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2014 Michael Zillgith
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
class SettingControl(object):
    """ generated source for class SettingControl """
    desc = None
    numOfSGs = 1
    actSG = 1

    def __init__(self, settingControlNode):
        """ generated source for method __init__ """
        self.desc = ParserUtils.parseAttribute(settingControlNode, "desc")
        numOfSGsString = ParserUtils.parseAttribute(settingControlNode, "numOfSGs")
        if numOfSGsString != None:
            self.numOfSGs = Integer.decode(numOfSGsString)
        actSGString = ParserUtils.parseAttribute(settingControlNode, "actSG")
        if actSGString != None:
            self.actSG = Integer.decode(actSGString)

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getNumOfSGs(self):
        """ generated source for method getNumOfSGs """
        return self.numOfSGs

    def getActSG(self):
        """ generated source for method getActSG """
        return self.actSG

