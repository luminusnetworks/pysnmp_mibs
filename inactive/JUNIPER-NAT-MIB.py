# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-NAT-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( InetAddress, InetAddressIPv4, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv4", "InetAddressType")
( jnxSvcsMibRoot, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxSvcsMibRoot")
( Bits, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DateAndTime, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString")

# Objects

jnxNatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1)).setRevisions(("2010-07-12 20:22",))
if mibBuilder.loadTexts: jnxNatMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxNatMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\n\nE-mail: support@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: jnxNatMIB.setDescription("This module defines the object that are used to monitor\nnetwork address translation attributes.")
jnxNatNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 0))
jnxNatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1))
jnxSrcNatStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1))
if mibBuilder.loadTexts: jnxSrcNatStatsTable.setDescription("This table exposes the source NAT translation\nattributes of the translated addresses.\n\nWhen performing source IP address translation, the services pic\ntranslates the original source IP address and/or port\nnumber to different one.  The resource, address source pools\nprovide the service pic with a supply of addresses from\nwhich to draw when performing source network address translation.\n\nThis table contains information on source IP address\ntranslation only.")
jnxSrcNatStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1)).setIndexNames((0, "JUNIPER-NAT-MIB", "jnxNatSrcPoolName"))
if mibBuilder.loadTexts: jnxSrcNatStatsEntry.setDescription("Source NAT address entries.  It is indexed by the address\npool table and the address allocated. ")
jnxNatSrcPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxNatSrcPoolName.setDescription("The name of dynamic source IP address pool.\n\nThis is the address pool where the translated\naddress is allocated from. ")
jnxNatSrcXlatedAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatSrcXlatedAddrType.setDescription("The type of dynamic source IP address allocated from\nthe address pool used in the NAT translation.\nFor NAT MIB, supporting ipv4(1) and ipv6(2) only.")
jnxNatSrcPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(3,11,26,22,14,13,25,23,24,19,16,1,20,12,15,18,17,21,2,)).subtype(namedValues=NamedValues(("static", 1), ("basic-nat44", 11), ("dynamic-nat44", 12), ("napt-44", 13), ("dnat-44", 14), ("stateful-nat64", 15), ("stateless-nat64", 16), ("basic-nat-pt", 17), ("napt-pt", 18), ("basic-nat66", 19), ("dynamic-napt", 2), ("stateless-nat66", 20), ("napt-66", 21), ("twice-napt-44", 22), ("twice-basic-nat-44", 23), ("twice-dynamic-nat-44", 24), ("det-napt44", 25), ("sd-napt44", 26), ("dynamic-nat", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatSrcPoolType.setDescription("Source NAT can do address translation with or without port\ntranslation.  The source port pool type indicates\nwhether the address translation is done with port or without\nthe port, or if it is a static translation.")
jnxNatSrcNumPortAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatSrcNumPortAvail.setDescription("The number of ports available with this pool.")
jnxNatSrcNumPortInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatSrcNumPortInuse.setDescription("The number of ports in use for this NAT address entry.\nThis attribute is only applicable to translation with\nport translation.")
jnxNatSrcNumAddressAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatSrcNumAddressAvail.setDescription("The total number of addresses available in this pool.")
jnxNatSrcNumAddressInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatSrcNumAddressInUse.setDescription("The number of addresses in use from this pool.\nThis attribute is only applicable to pools used with\nsource dynamic translations.")
jnxNatSrcNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatSrcNumSessions.setDescription("The number of sessions are in use based on this NAT address\nentry.")
jnxNatRuleTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2))
if mibBuilder.loadTexts: jnxNatRuleTable.setDescription("This table monitors NAT rule hits  ")
jnxNatRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1)).setIndexNames((0, "JUNIPER-NAT-MIB", "jnxNatRuleName"))
if mibBuilder.loadTexts: jnxNatRuleEntry.setDescription("NAT rule hit entries.  It is indexed by the rule index")
jnxNatRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxNatRuleName.setDescription("NAT rule name")
jnxNatRuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(20,4,26,3,22,1,13,25,16,18,24,11,12,23,14,15,2,17,21,19,)).subtype(namedValues=NamedValues(("static-source", 1), ("basic-nat44", 11), ("dynamic-nat44", 12), ("napt-44", 13), ("dnat-44", 14), ("stateful-nat64", 15), ("stateless-nat64", 16), ("basic-nat-pt", 17), ("napt-pt", 18), ("basic-nat66", 19), ("static-destination", 2), ("stateless-nat66", 20), ("napt-66", 21), ("twice-napt-44", 22), ("twice-basic-nat-44", 23), ("twice-dynamic-nat-44", 24), ("det-napt44", 25), ("sd-napt44", 26), ("dynamic-source", 3), ("napt", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatRuleType.setDescription("NAT types: Static Source, Static Destination,\nDynamic Source and NAPT")
jnxNatRuleTransHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatRuleTransHits.setDescription("The number of hits on this NAT rule")
jnxNatPoolTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3))
if mibBuilder.loadTexts: jnxNatPoolTable.setDescription("This table monitors NAT pool hits  ")
jnxNatPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1)).setIndexNames((0, "JUNIPER-NAT-MIB", "jnxNatPoolName"))
if mibBuilder.loadTexts: jnxNatPoolEntry.setDescription("NAT pool hit entries.  It is indexed by the pool index")
jnxNatPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxNatPoolName.setDescription("NAT Pool name")
jnxNatPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(20,4,26,3,22,1,13,25,16,18,24,11,12,23,14,15,2,17,21,19,)).subtype(namedValues=NamedValues(("static-source", 1), ("basic-nat44", 11), ("dynamic-nat44", 12), ("napt-44", 13), ("dnat-44", 14), ("stateful-nat64", 15), ("stateless-nat64", 16), ("basic-nat-pt", 17), ("napt-pt", 18), ("basic-nat66", 19), ("static-destination", 2), ("stateless-nat66", 20), ("napt-66", 21), ("twice-napt-44", 22), ("twice-basic-nat-44", 23), ("twice-dynamic-nat-44", 24), ("det-napt44", 25), ("sd-napt44", 26), ("dynamic-source", 3), ("napt", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatPoolType.setDescription("NAT types: Static Source, Static Destination,\nDynamic Source and NAPT")
jnxNatPoolTransHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxNatPoolTransHits.setDescription("The number of hits on this NAT Pool")
jnxNatTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2))
jnxNatAddrPoolUtil = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxNatAddrPoolUtil.setDescription("The dynamic address pool utilization in percentage.")
jnxNatTrapSrcPoolName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxNatTrapSrcPoolName.setDescription("Source NAT Pool name who issues trap")

# Augmentions

# Notifications

jnxNatAddrPoolThresholdStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 0, 1)).setObjects(*(("JUNIPER-NAT-MIB", "jnxNatTrapSrcPoolName"), ("JUNIPER-NAT-MIB", "jnxNatAddrPoolUtil"), ) )
if mibBuilder.loadTexts: jnxNatAddrPoolThresholdStatus.setDescription("The Source NAT address pool utilization threshold status\ntrap signifies that the address pool utilization\nis either exceeds certain percentage, or clear of \nthat percentage.\n				\n		  jnxNatTrapPoolName is the name of the resource pool\n		  jnxNatAddrPoolUtil is the percentage of utilization \nof the address pool.")

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-NAT-MIB", PYSNMP_MODULE_ID=jnxNatMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-NAT-MIB", jnxNatMIB=jnxNatMIB, jnxNatNotifications=jnxNatNotifications, jnxNatObjects=jnxNatObjects, jnxSrcNatStatsTable=jnxSrcNatStatsTable, jnxSrcNatStatsEntry=jnxSrcNatStatsEntry, jnxNatSrcPoolName=jnxNatSrcPoolName, jnxNatSrcXlatedAddrType=jnxNatSrcXlatedAddrType, jnxNatSrcPoolType=jnxNatSrcPoolType, jnxNatSrcNumPortAvail=jnxNatSrcNumPortAvail, jnxNatSrcNumPortInuse=jnxNatSrcNumPortInuse, jnxNatSrcNumAddressAvail=jnxNatSrcNumAddressAvail, jnxNatSrcNumAddressInUse=jnxNatSrcNumAddressInUse, jnxNatSrcNumSessions=jnxNatSrcNumSessions, jnxNatRuleTable=jnxNatRuleTable, jnxNatRuleEntry=jnxNatRuleEntry, jnxNatRuleName=jnxNatRuleName, jnxNatRuleType=jnxNatRuleType, jnxNatRuleTransHits=jnxNatRuleTransHits, jnxNatPoolTable=jnxNatPoolTable, jnxNatPoolEntry=jnxNatPoolEntry, jnxNatPoolName=jnxNatPoolName, jnxNatPoolType=jnxNatPoolType, jnxNatPoolTransHits=jnxNatPoolTransHits, jnxNatTrapVars=jnxNatTrapVars, jnxNatAddrPoolUtil=jnxNatAddrPoolUtil, jnxNatTrapSrcPoolName=jnxNatTrapSrcPoolName)

# Notifications
mibBuilder.exportSymbols("JUNIPER-NAT-MIB", jnxNatAddrPoolThresholdStatus=jnxNatAddrPoolThresholdStatus)

