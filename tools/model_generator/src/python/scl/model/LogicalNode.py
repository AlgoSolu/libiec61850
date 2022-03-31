#!/usr/bin/env python
""" generated source for module LogicalNode """
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
class LogicalNode(DataModelNode):
    """ generated source for class LogicalNode """
    lnClass = None
    lnType = None
    inst = None
    desc = None
    prefix = None
    sclType = None
    dataObjects = None
    dataSets = None
    reportControlBlocks = None
    gseControlBlocks = None
    smvControlBlocks = None
    logControlBlocks = None
    logs = None
    settingGroupControlBlocks = None
    parentLogicalDevice = None

    def __init__(self, lnNode, typeDeclarations, parent):
        """ generated source for method __init__ """
        super(LogicalNode, self).__init__()
        self.lnClass = ParserUtils.parseAttribute(lnNode, "lnClass")
        self.lnType = ParserUtils.parseAttribute(lnNode, "lnType")
        self.inst = ParserUtils.parseAttribute(lnNode, "inst")
        self.desc = ParserUtils.parseAttribute(lnNode, "desc")
        self.prefix = ParserUtils.parseAttribute(lnNode, "prefix")
        self.parentLogicalDevice = parent
        if self.lnClass == None:
            raise SclParserException(lnNode, "required attribute \"lnClass\" is missing in logical node.")
        if self.lnType == None:
            raise SclParserException(lnNode, "required attribute \"lnType\" is missing in logical node.")
        if self.inst == None:
            raise SclParserException(lnNode, "required attribute \"inst\" is missing in logical node.")
        #  instantiate DataObjects
        self.sclType = typeDeclarations.lookupType(self.lnType)
        if self.sclType == None:
            raise SclParserException(lnNode, "missing type declaration " + self.lnType)
        if isinstance(self.sclType, (LogicalNodeType, )):
            self.dataObjects = LinkedList()
            type_ = self.sclType
            #  mark type as used 
            type_.setUsed(True)
            doDefinitions = type_.getDataObjectDefinitions()
            for doDefinition in doDefinitions:
                self.dataObjects.add(DataObject(doDefinition, typeDeclarations, self))
        else:
            raise SclParserException(lnNode, "wrong type " + self.lnType + " for logical node")
        #  Parse data set definitions 
        self.dataSets = LinkedList()
        dataSetNodes = ParserUtils.getChildNodesWithTag(lnNode, "DataSet")
        for dataSet in dataSetNodes:
            self.dataSets.add(DataSet(dataSet))
        #  Parse report control block definitions 
        self.reportControlBlocks = LinkedList()
        reportControlNodes = ParserUtils.getChildNodesWithTag(lnNode, "ReportControl")
        for reportControlNode in reportControlNodes:
            self.reportControlBlocks.add(ReportControlBlock(reportControlNode))
        #  Parse GSE control block definitions 
        self.gseControlBlocks = LinkedList()
        gseControlNodes = ParserUtils.getChildNodesWithTag(lnNode, "GSEControl")
        for gseControlNode in gseControlNodes:
            self.gseControlBlocks.add(GSEControl(gseControlNode))
        #  Parse Sampled Values (SV) control block definitions 
        self.smvControlBlocks = LinkedList()
        svControlNodes = ParserUtils.getChildNodesWithTag(lnNode, "SampledValueControl")
        for svControlNode in svControlNodes:
            self.smvControlBlocks.add(SampledValueControl(svControlNode))
        #  Parse log control block definitions 
        self.logControlBlocks = LinkedList()
        logControlNodes = ParserUtils.getChildNodesWithTag(lnNode, "LogControl")
        for logControlNode in logControlNodes:
            self.logControlBlocks.add(LogControl(logControlNode))
        #  Parse logs 
        self.logs = LinkedList()
        logNodes = ParserUtils.getChildNodesWithTag(lnNode, "Log")
        for logNode in logNodes:
            self.logs.add(Log(logNode))
        #  Parse setting group control block definitions 
        self.settingGroupControlBlocks = LinkedList()
        sgNodes = ParserUtils.getChildNodesWithTag(lnNode, "SettingControl")
        if (self.lnClass == "LLN0" == False) and (len(sgNodes) > 0):
            raise SclParserException(lnNode, "LN other than LN0 is not allowed to contain SettingControl")
        if len(sgNodes) > 1:
            raise SclParserException(lnNode, "LN contains more then one SettingControl")
        for sgNode in sgNodes:
            self.settingGroupControlBlocks.add(SettingControl(sgNode))
        #  Parse data object instances 
        doiNodes = ParserUtils.getChildNodesWithTag(lnNode, "DOI")
        for doiNode in doiNodes:
            doiName = ParserUtils.parseAttribute(doiNode, "name")
            dataObject = getChildByName(doiName)
            if dataObject == None:
                raise SclParserException(doiNode, "Missing data object with name \"" + doiName + "\"")
            parseDataAttributeNodes(doiNode, dataObject)
            parseSubDataInstances(doiNode, dataObject)

    def parseDataAttributeNodes(self, doiNode, dataObject):
        """ generated source for method parseDataAttributeNodes """
        daiNodes = ParserUtils.getChildNodesWithTag(doiNode, "DAI")
        for daiNode in daiNodes:
            daiName = ParserUtils.parseAttribute(daiNode, "name")
            dataAttribute = dataObject.getChildByName(daiName)
            if dataAttribute == None:
                raise SclParserException(daiNode, "Missing data attribute with name \"" + daiName + "\"")
            valNode = ParserUtils.getChildNodeWithTag(daiNode, "Val")
            if valNode != None:
                value = valNode.getTextContent()
                try:
                    dataAttribute.setValue(DataModelValue(dataAttribute.getType(), dataAttribute.getSclType(), value))
                except IllegalValueException as e:
                    raise SclParserException(valNode, e.getMessage())
            shortAddress = ParserUtils.parseAttribute(daiNode, "sAddr")
            if shortAddress != None:
                if not shortAddress == "":
                    dataAttribute.setShortAddress(shortAddress)

    def parseSubDataInstances(self, doiNode, dataObject):
        """ generated source for method parseSubDataInstances """
        sdiNodes = ParserUtils.getChildNodesWithTag(doiNode, "SDI")
        for sdiNode in sdiNodes:
            sdiName = ParserUtils.parseAttribute(sdiNode, "name")
            subDataAttribute = dataObject.getChildByName(sdiName)
            if subDataAttribute == None:
                print("subelement with name " + sdiName + " not found!")
            self.parseDataAttributeNodes(sdiNode, subDataAttribute)
            self.parseSubDataInstances(sdiNode, subDataAttribute)

    def getLnClass(self):
        """ generated source for method getLnClass """
        return self.lnClass

    def getLnType(self):
        """ generated source for method getLnType """
        return self.lnType

    def getInst(self):
        """ generated source for method getInst """
        return self.inst

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getPrefix(self):
        """ generated source for method getPrefix """
        return self.prefix

    def getName(self):
        """ generated source for method getName """
        name = ""
        if self.prefix != None:
            name += self.prefix
        name += self.lnClass
        name += self.inst
        return name

    def getDataObjects(self):
        """ generated source for method getDataObjects """
        return self.dataObjects

    def getDataSets(self):
        """ generated source for method getDataSets """
        return self.dataSets

    def getReportControlBlocks(self):
        """ generated source for method getReportControlBlocks """
        return self.reportControlBlocks

    def getGSEControlBlocks(self):
        """ generated source for method getGSEControlBlocks """
        return self.gseControlBlocks

    def getSampledValueControlBlocks(self):
        """ generated source for method getSampledValueControlBlocks """
        return self.smvControlBlocks

    def getSettingGroupControlBlocks(self):
        """ generated source for method getSettingGroupControlBlocks """
        return self.settingGroupControlBlocks

    def getLogControlBlocks(self):
        """ generated source for method getLogControlBlocks """
        return self.logControlBlocks

    def getLogs(self):
        """ generated source for method getLogs """
        return self.logs

    def getChildByName(self, childName):
        """ generated source for method getChildByName """
        for dataObject in dataObjects:
            if dataObject.__name__ == childName:
                return dataObject
        return None

    def getParentLogicalDevice(self):
        """ generated source for method getParentLogicalDevice """
        return self.parentLogicalDevice

    def getSclType(self):
        """ generated source for method getSclType """
        return self.sclType

    def getParent(self):
        """ generated source for method getParent """
        return None

