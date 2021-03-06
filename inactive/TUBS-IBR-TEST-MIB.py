# PySNMP SMI module. Autogenerated from smidump -f python TUBS-IBR-TEST-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")
( ibr, ) = mibBuilder.importSymbols("TUBS-SMI", "ibr")

# Types

class BinaryValue(TextualConvention, Integer32):
    displayHint = "b"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class Dot3Value(TextualConvention, Integer32):
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class HexValue(TextualConvention, Integer32):
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class NumValue(OctetString):
    pass

class OctalValue(TextualConvention, Integer32):
    displayHint = "o"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    

# Objects

testMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 7)).setRevisions(("2000-02-09 00:00","1998-10-09 17:11",))
if mibBuilder.loadTexts: testMIB.setOrganization("TU Braunschweig")
if mibBuilder.loadTexts: testMIB.setContactInfo("Juergen Schoenwaelder\nTU Braunschweig\nBueltenweg 74/75\n38106 Braunschweig\nGermany\n\nTel: +49 531 391 3283\nFax: +49 531 391 5936\nE-mail: schoenw@ibr.cs.tu-bs.de")
if mibBuilder.loadTexts: testMIB.setDescription("A MIB module which is only used for testing purposes.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("TUBS-IBR-TEST-MIB", PYSNMP_MODULE_ID=testMIB)

# Types
mibBuilder.exportSymbols("TUBS-IBR-TEST-MIB", BinaryValue=BinaryValue, Dot3Value=Dot3Value, HexValue=HexValue, NumValue=NumValue, OctalValue=OctalValue)

# Objects
mibBuilder.exportSymbols("TUBS-IBR-TEST-MIB", testMIB=testMIB)

