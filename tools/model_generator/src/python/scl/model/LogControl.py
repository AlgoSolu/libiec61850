#!/usr/bin/env python
""" generated source for module LogControl """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2014-2016 Michael Zillgith
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
class LogControl(object):
    """ generated source for class LogControl """
    name = None
    desc = None
    dataSet = None
    ldInst = None
    prefix = ""
    lnClass = "LLN0"
    lnInst = ""
    logName = None
    logEna = True
    reasonCode = True
    intgPd = 0

    #  integrity period in ms
    triggerOptions = None

    def __init__(self, logControlNode):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(logControlNode, "name")
        if self.name == None:
            raise SclParserException(logControlNode, "LogControl is missing required attribute \"name\"")
        self.desc = ParserUtils.parseAttribute(logControlNode, "desc")
        self.dataSet = ParserUtils.parseAttribute(logControlNode, "datSet")
        if self.dataSet != None:
            if self.dataSet == "":
                self.dataSet = None
        self.ldInst = ParserUtils.parseAttribute(logControlNode, "ldInst")
        self.prefix = ParserUtils.parseAttribute(logControlNode, "prefix")
        lnClassString = ParserUtils.parseAttribute(logControlNode, "lnClass")
        if lnClassString != None:
            self.lnClass = lnClassString
        lnInstString = ParserUtils.parseAttribute(logControlNode, "lnInst")
        if lnInstString != None:
            self.lnInst = lnInstString
        self.logName = ParserUtils.parseAttribute(logControlNode, "logName")
        if self.logName == None:
            raise SclParserException(logControlNode, "LogControl is missing required attribute \"logName\"")
        if self.logName == "":
            self.logName = None
        intgPdString = ParserUtils.parseAttribute(logControlNode, "intgPd")
        if intgPdString != None:
            self.intgPd = Integer.decode(intgPdString)
        logEnaBoolean = ParserUtils.parseBooleanAttribute(logControlNode, "logEna")
        if logEnaBoolean != None:
            self.logEna = logEnaBoolean
        reasonCodeBoolean = ParserUtils.parseBooleanAttribute(logControlNode, "reasonCode")
        if reasonCodeBoolean != None:
            self.reasonCode = reasonCodeBoolean
        trgOpsNode = ParserUtils.getChildNodeWithTag(logControlNode, "TrgOps")
        if trgOpsNode != None:
            self.triggerOptions = TriggerOptions(trgOpsNode)
        else:
            self.triggerOptions = TriggerOptions()
        #  use default values if no node present

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getDataSet(self):
        """ generated source for method getDataSet """
        return self.dataSet

    def getLdInst(self):
        """ generated source for method getLdInst """
        return self.ldInst

    def getPrefix(self):
        """ generated source for method getPrefix """
        return self.prefix

    def getLnClass(self):
        """ generated source for method getLnClass """
        return self.lnClass

    def getLogName(self):
        """ generated source for method getLogName """
        return self.logName

    def isLogEna(self):
        """ generated source for method isLogEna """
        return self.logEna

    def isReasonCode(self):
        """ generated source for method isReasonCode """
        return self.reasonCode

    def getIntgPd(self):
        """ generated source for method getIntgPd """
        return self.intgPd

    def getTriggerOptions(self):
        """ generated source for method getTriggerOptions """
        return self.triggerOptions

