#!/usr/bin/env python
""" generated source for module DynamicCodeGenerator """
from __future__ import print_function
# package: com.libiec61850.tools
class DynamicCodeGenerator(object):
    """ generated source for class DynamicCodeGenerator """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        if len(args):
            print("Dynamic code generator")
            print("Usage: gencode <ICD file> [-ied  <ied-name>] [-ap <access-point-name>] [<output filename>]")
            System.exit(1)
        icdFile = args[0]
        outputStream = System.out
        accessPointName = None
        iedName = None
        if len(args):
            i = 1
            while len(args):
                if args[i] == "-ap":
                    accessPointName = args[i + 1]
                    print("Select access point " + accessPointName)
                    i += 1
                elif args[i] == "-ied":
                    iedName = args[i + 1]
                    print("Select IED " + iedName)
                    i += 1
                else:
                    outputStream = PrintStream(FileOutputStream(File(args[i])))
                i += 1
        stream = FileInputStream(icdFile)
        SclParser.withOutput = False
        sclParser = SclParser(stream, False)
        createDynamicCode(sclParser)

    @classmethod
    def createDynamicCode(cls, sclParser):
        """ generated source for method createDynamicCode """
        declarations = sclParser.getTypeDeclarations()
        out = System.out
        doTypeDefs = HashSet()
        lnTypeDefs = HashSet()
        daTypeDefs = HashSet()
        functionPrototypes = LinkedList()
        for type_ in declarations.getTypeDeclarations():
            if type_.__class__ == LogicalNodeType.__class__:
                lnTypeDefs.add(type_)
            elif type_.__class__ == DataObjectType.__class__:
                doTypeDefs.add(type_)
            elif type_.__class__ == DataAttributeType.__class__:
                daTypeDefs.add(type_)
        for lnType in lnTypeDefs:
            functionPrototype = "LogicalNode*\nLN_" + lnType.getId() + "_createInstance(char* lnName, LogicalDevice* parent);"
            functionPrototypes.add(functionPrototype)
        for doType in doTypeDefs:
            functionPrototype = "DataObject*\nDO_" + doType.getId() + "_createInstance(char* doName, ModelNode* parent, int arrayCount);"
            functionPrototypes.add(functionPrototype)
        for daType in daTypeDefs:
            functionPrototype = "DataAttribute*\nDA_" + daType.getId() + "_createInstance(char* daName, ModelNode* parent, FunctionalConstraint fc, uint8_t triggerOptions);"
            functionPrototypes.add(functionPrototype)
        print("#include \"iec61850_server.h\"")
        print()
        for prototype in functionPrototypes:
            print(prototype)
            print()
        for lnType in lnTypeDefs:
            out.println("/**")
            out.printf(" * LN: %s ", lnType.getId())
            if lnType.getDesc() != None:
                out.printf("(%s)", lnType.getDesc())
            out.println()
            out.println(" */")
            out.println("LogicalNode*")
            out.printf("LN_%s_createInstance(char* lnName, LogicalDevice* parent)\n", lnType.getId())
            out.println("{")
            out.println("    LogicalNode* newLn = LogicalNode_create(lnName, parent);\n")
            doDefs = lnType.getDataObjectDefinitions()
            for objDef in doDefs:
                out.printf("    DO_%s_createInstance(\"%s\", (ModelNode*) newLn, %d);\n", objDef.getType(), objDef.__name__, objDef.getCount())
            out.println("\n    return newLn;")
            out.println("}\n\n")
        for doType in doTypeDefs:
            out.println("/**")
            out.printf(" * DO: %s ", doType.getId())
            if doType.getDesc() != None:
                out.printf("(%s)", doType.getDesc())
            out.println()
            out.println(" */")
            out.println("DataObject*")
            out.printf("DO_%s_createInstance(char* doName, ModelNode* parent, int arrayCount)\n", doType.getId())
            out.println("{")
            out.println("    DataObject* newDo = DataObject_create(doName, parent, arrayCount);\n")
            for dad in doType.getDataAttributes():
                if dad.getAttributeType() == AttributeType.CONSTRUCTED:
                    out.print_("    DA_" + dad.getType() + "_createInstance(\"" + dad.__name__ + "\", ")
                    out.print_("(ModelNode*) newDo, IEC61850_FC_" + dad.getFc().__str__())
                    out.print_(", " + dad.getTriggerOptions().getIntValue())
                    out.println(");")
                else:
                    out.print_("    DataAttribute_create(\"" + dad.__name__ + "\", ")
                    out.print_("(ModelNode*) newDo, IEC61850_" + dad.getAttributeType())
                    out.print_(", IEC61850_FC_" + dad.getFc().__str__())
                    out.print_(", " + dad.getTriggerOptions().getIntValue())
                    out.print_(", " + dad.getCount())
                    out.print_(", 0")
                    out.println(");")
            for dod in doType.getSubDataObjects():
                out.print_("    DO_" + dod.getType() + "_createInstance(\"" + dod.__name__ + "\", ")
                out.println("(ModelNode*) newDo, " + dod.getCount() + ");")
            out.println("\n    return newDo;")
            out.println("}\n\n")
        for daType in daTypeDefs:
            out.println("/**")
            out.printf(" * DA: %s ", daType.getId())
            if daType.getDesc() != None:
                out.printf("(%s)", daType.getDesc())
            out.println()
            out.println(" */")
            out.println("DataAttribute*")
            out.printf("DA_%s_createInstance(char* daName, ModelNode* parent, FunctionalConstraint fc, uint8_t triggerOptions)\n", daType.getId())
            out.println("{")
            out.println("    DataAttribute* newDa = DataAttribute_create(daName, parent, IEC61850_CONSTRUCTED, fc, triggerOptions, 0, 0);\n")
            for dad in daType.getSubDataAttributes():
                if dad.getAttributeType() == AttributeType.CONSTRUCTED:
                    out.print_("    DA_" + dad.getType() + "_createInstance(\"" + dad.__name__ + "\", ")
                    out.println("(ModelNode*) newDa, fc, triggerOptions);")
                else:
                    out.print_("    DataAttribute_create(\"" + dad.__name__ + "\", ")
                    out.print_("(ModelNode*) newDa, IEC61850_" + dad.getAttributeType())
                    out.print_(", fc")
                    out.print_(", triggerOptions")
                    out.print_(", " + dad.getCount())
                    out.print_(", 0")
                    out.println(");")
            out.println("\n    return newDa;")
            out.println("}\n\n")


if __name__ == '__main__':
    import sys
    DynamicCodeGenerator.main(sys.argv)

