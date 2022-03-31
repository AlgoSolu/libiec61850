#!/usr/bin/env python
""" generated source for module ReportControlBlock """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013, 2014 Michael Zillgith
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
class ReportControlBlock(object):
    """ generated source for class ReportControlBlock """
    name = None
    desc = None
    dataSet = None
    integrityPeriod = None
    rptID = None
    confRef = None
    buffered = False
    bufferTime = 0
    triggerOptions = None
    optionFields = None
    indexed = True
    rptEna = None

    def __init__(self, reportControlNode):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(reportControlNode, "name")
        self.desc = ParserUtils.parseAttribute(reportControlNode, "desc")
        self.dataSet = ParserUtils.parseAttribute(reportControlNode, "datSet")
        intgPdString = ParserUtils.parseAttribute(reportControlNode, "intgPd")
        if intgPdString != None:
            self.integrityPeriod = long(intgPdString)
        self.rptID = ParserUtils.parseAttribute(reportControlNode, "rptID")
        if self.rptID != None:
            if self.rptID == "":
                self.rptID = None
        confRefStr = ParserUtils.parseAttribute(reportControlNode, "confRev")
        if confRefStr != None:
            self.confRef = long(confRefStr)
        else:
            raise SclParserException("Missing required attribute \"confRef\"")
        bufferedVal = ParserUtils.parseBooleanAttribute(reportControlNode, "buffered")
        if bufferedVal != None:
            self.buffered = bufferedVal
        bufferTimeStr = ParserUtils.parseAttribute(reportControlNode, "bufTime")
        if bufferTimeStr != None:
            self.bufferTime = long(bufferTimeStr)
        trgOpsNode = ParserUtils.getChildNodeWithTag(reportControlNode, "TrgOps")
        if trgOpsNode != None:
            self.triggerOptions = TriggerOptions(trgOpsNode)
        else:
            self.triggerOptions = TriggerOptions()
        #  use default values if no node present
        optFieldsNode = ParserUtils.getChildNodeWithTag(reportControlNode, "OptFields")
        self.optionFields = OptionFields(optFieldsNode)
        indexed = ParserUtils.parseBooleanAttribute(reportControlNode, "indexed")
        if indexed != None:
            self.indexed = indexed.booleanValue()
        rptEnabledNode = ParserUtils.getChildNodeWithTag(reportControlNode, "RptEnabled")
        if rptEnabledNode != None:
            rptEna = RptEnabled(rptEnabledNode)
            if self.indexed == False:
                if self.rptEna.getMaxInstances() != 1:
                    raise SclParserException("RptEnabled.max != 1 is not allowed when indexed=\"false\"")
            self.rptEna = self.rptEna

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getDataSet(self):
        """ generated source for method getDataSet """
        return self.dataSet

    def getIntegrityPeriod(self):
        """ generated source for method getIntegrityPeriod """
        return self.integrityPeriod

    def getRptID(self):
        """ generated source for method getRptID """
        return self.rptID

    def getConfRef(self):
        """ generated source for method getConfRef """
        return self.confRef

    def isBuffered(self):
        """ generated source for method isBuffered """
        return self.buffered

    def getBufferTime(self):
        """ generated source for method getBufferTime """
        return self.bufferTime

    def getTriggerOptions(self):
        """ generated source for method getTriggerOptions """
        return self.triggerOptions

    def getOptionFields(self):
        """ generated source for method getOptionFields """
        return self.optionFields

    def isIndexed(self):
        """ generated source for method isIndexed """
        return self.indexed

    def getRptEna(self):
        """ generated source for method getRptEna """
        return self.rptEna

