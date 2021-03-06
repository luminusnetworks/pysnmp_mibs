# PySNMP SMI module. Autogenerated from smidump -f python RSTP-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:10 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( dot1dStp, dot1dStpPortEntry, ) = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStp", "dot1dStpPortEntry")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue")

# Objects

dot1dStpVersion = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 16), Integer().subtype(subtypeSpec=SingleValueConstraint(0,2,)).subtype(namedValues=NamedValues(("stpCompatible", 0), ("rstp", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpVersion.setDescription("The version of Spanning Tree Protocol the bridge is\ncurrently running.  The value 'stpCompatible(0)'\nindicates the Spanning Tree Protocol specified in\nIEEE 802.1D-1998 and 'rstp(2)' indicates the Rapid\nSpanning Tree Protocol specified in IEEE 802.1w and\nclause 17 of 802.1D-2004.  The values are directly from\nthe IEEE standard.  New values may be defined as future\nversions of the protocol become available.\n\nThe value of this object MUST be retained across\nreinitializations of the management system.")
dot1dStpTxHoldCount = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpTxHoldCount.setDescription("The value used by the Port Transmit state machine to limit\nthe maximum transmission rate.\n\nThe value of this object MUST be retained across\nreinitializations of the management system.")
dot1dStpExtPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 2, 19))
if mibBuilder.loadTexts: dot1dStpExtPortTable.setDescription("A table that contains port-specific Rapid Spanning Tree\ninformation.")
dot1dStpExtPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 2, 19, 1))
if mibBuilder.loadTexts: dot1dStpExtPortEntry.setDescription("A list of Rapid Spanning Tree information maintained by\neach port.")
dot1dStpPortProtocolMigration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortProtocolMigration.setDescription("When operating in RSTP (version 2) mode, writing true(1)\nto this object forces this port to transmit RSTP BPDUs.\nAny other operation on this object has no effect and\nit always returns false(2) when read.")
dot1dStpPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminEdgePort.setDescription("The administrative value of the Edge Port parameter.  A\nvalue of true(1) indicates that this port should be\nassumed as an edge-port, and a value of false(2) indicates\nthat this port should be assumed as a non-edge-port.\n\n\n\nSetting this object will also cause the corresponding\ninstance of dot1dStpPortOperEdgePort to change to the\nsame value.  Note that even when this object's value\nis true, the value of the corresponding instance of\ndot1dStpPortOperEdgePort can be false if a BPDU has\nbeen received.\n\nThe value of this object MUST be retained across\nreinitializations of the management system.")
dot1dStpPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortOperEdgePort.setDescription("The operational value of the Edge Port parameter.  The\nobject is initialized to the value of the corresponding\ninstance of dot1dStpPortAdminEdgePort.  When the\ncorresponding instance of dot1dStpPortAdminEdgePort is\nset, this object will be changed as well.  This object\nwill also be changed to false on reception of a BPDU.")
dot1dStpPortAdminPointToPoint = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,2,)).subtype(namedValues=NamedValues(("forceTrue", 0), ("forceFalse", 1), ("auto", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminPointToPoint.setDescription("The administrative point-to-point status of the LAN segment\nattached to this port, using the enumeration values of the\nIEEE 802.1w clause.  A value of forceTrue(0) indicates\nthat this port should always be treated as if it is\nconnected to a point-to-point link.  A value of\nforceFalse(1) indicates that this port should be treated as\nhaving a shared media connection.  A value of auto(2)\nindicates that this port is considered to have a\npoint-to-point link if it is an Aggregator and all of its\n\n\n\nmembers are aggregatable, or if the MAC entity\nis configured for full duplex operation, either through\nauto-negotiation or by management means.  Manipulating this\nobject changes the underlying adminPortToPortMAC.\n\nThe value of this object MUST be retained across\nreinitializations of the management system.")
dot1dStpPortOperPointToPoint = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortOperPointToPoint.setDescription("The operational point-to-point status of the LAN segment\nattached to this port.  It indicates whether a port is\nconsidered to have a point-to-point connection.\nIf adminPointToPointMAC is set to auto(2), then the value\nof operPointToPointMAC is determined in accordance with the\nspecific procedures defined for the MAC entity concerned,\nas defined in IEEE 802.1w, clause 6.5.  The value is\ndetermined dynamically; that is, it is re-evaluated whenever\nthe value of adminPointToPointMAC changes, and whenever\nthe specific procedures defined for the MAC entity evaluate\na change in its point-to-point status.")
dot1dStpPortAdminPathCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminPathCost.setDescription("The administratively assigned value for the contribution\nof this port to the path cost of paths toward the spanning\ntree root.\n\nWriting a value of '0' assigns the automatically calculated\ndefault Path Cost value to the port.  If the default Path\nCost is being used, this object returns '0' when read.\n\nThis complements the object dot1dStpPortPathCost or\ndot1dStpPortPathCost32, which returns the operational value\nof the path cost.\n\n\n\nThe value of this object MUST be retained across\nreinitializations of the management system.")
rstpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 134)).setRevisions(("2005-12-07 00:00",))
if mibBuilder.loadTexts: rstpMIB.setOrganization("IETF Bridge MIB Working Group")
if mibBuilder.loadTexts: rstpMIB.setContactInfo("Email: Bridge-mib@ietf.org")
if mibBuilder.loadTexts: rstpMIB.setDescription("The Bridge MIB Extension module for managing devices\nthat support the Rapid Spanning Tree Protocol defined\nby IEEE 802.1w.\n\nCopyright (C) The Internet Society (2005).  This version of\nthis MIB module is part of RFC 4318; See the RFC itself for\nfull legal notices.")
rstpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 0))
rstpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 1))
rstpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 2))
rstpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 2, 1))
rstpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 2, 2))

# Augmentions
dot1dStpPortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPortEntry")
dot1dStpPortEntry.registerAugmentions(("RSTP-MIB", "dot1dStpExtPortEntry"))
dot1dStpExtPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Groups

rstpBridgeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 134, 2, 1, 1)).setObjects(*(("RSTP-MIB", "dot1dStpTxHoldCount"), ("RSTP-MIB", "dot1dStpVersion"), ) )
if mibBuilder.loadTexts: rstpBridgeGroup.setDescription("Rapid Spanning Tree information for the bridge.")
rstpPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 134, 2, 1, 2)).setObjects(*(("RSTP-MIB", "dot1dStpPortOperPointToPoint"), ("RSTP-MIB", "dot1dStpPortOperEdgePort"), ("RSTP-MIB", "dot1dStpPortProtocolMigration"), ("RSTP-MIB", "dot1dStpPortAdminEdgePort"), ("RSTP-MIB", "dot1dStpPortAdminPointToPoint"), ("RSTP-MIB", "dot1dStpPortAdminPathCost"), ) )
if mibBuilder.loadTexts: rstpPortGroup.setDescription("Rapid Spanning Tree information for individual ports.")

# Compliances

rstpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 134, 2, 2, 1)).setObjects(*(("RSTP-MIB", "rstpBridgeGroup"), ("RSTP-MIB", "rstpPortGroup"), ) )
if mibBuilder.loadTexts: rstpCompliance.setDescription("The compliance statement for device support of Rapid\nSpanning Tree Protocol (RSTP) bridging services.")

# Exports

# Module identity
mibBuilder.exportSymbols("RSTP-MIB", PYSNMP_MODULE_ID=rstpMIB)

# Objects
mibBuilder.exportSymbols("RSTP-MIB", dot1dStpVersion=dot1dStpVersion, dot1dStpTxHoldCount=dot1dStpTxHoldCount, dot1dStpExtPortTable=dot1dStpExtPortTable, dot1dStpExtPortEntry=dot1dStpExtPortEntry, dot1dStpPortProtocolMigration=dot1dStpPortProtocolMigration, dot1dStpPortAdminEdgePort=dot1dStpPortAdminEdgePort, dot1dStpPortOperEdgePort=dot1dStpPortOperEdgePort, dot1dStpPortAdminPointToPoint=dot1dStpPortAdminPointToPoint, dot1dStpPortOperPointToPoint=dot1dStpPortOperPointToPoint, dot1dStpPortAdminPathCost=dot1dStpPortAdminPathCost, rstpMIB=rstpMIB, rstpNotifications=rstpNotifications, rstpObjects=rstpObjects, rstpConformance=rstpConformance, rstpGroups=rstpGroups, rstpCompliances=rstpCompliances)

# Groups
mibBuilder.exportSymbols("RSTP-MIB", rstpBridgeGroup=rstpBridgeGroup, rstpPortGroup=rstpPortGroup)

# Compliances
mibBuilder.exportSymbols("RSTP-MIB", rstpCompliance=rstpCompliance)
