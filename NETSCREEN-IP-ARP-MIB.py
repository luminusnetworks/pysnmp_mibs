# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-IP-ARP-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:55 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenIp, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenIp")
( Bits, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, PhysAddress, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress")

# Objects

nsIpArp = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 17, 1)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-10 00:00","2001-09-28 00:00","2001-05-02 00:00",))
if mibBuilder.loadTexts: nsIpArp.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: nsIpArp.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: nsIpArp.setDescription("This module defines NetScreen private MIBs for ARP")
nsIpArpAOD = MibScalar((1, 3, 6, 1, 4, 1, 3224, 17, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsIpArpAOD.setDescription("ARP always on destination.")
nsIpArpCachUpdate = MibScalar((1, 3, 6, 1, 4, 1, 3224, 17, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsIpArpCachUpdate.setDescription("ARP cache update.")
nsIpArpTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3))
if mibBuilder.loadTexts: nsIpArpTable.setDescription("This table collects all the ARP entries existing in NetScreen\ndevice.")
nsIpArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1)).setIndexNames((0, "NETSCREEN-IP-ARP-MIB", "nsIpArpIndex"))
if mibBuilder.loadTexts: nsIpArpEntry.setDescription("An entry containing attributes of arp info")
nsIpArpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpIndex.setDescription("A unique value for arp table.  Its value ranges between 0 and\n65535 and may not be contiguous.")
nsIpArpIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpIp.setDescription("IP address.")
nsIpArpMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpMac.setDescription("MAC address.")
nsIpArpVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpVsys.setDescription("Virtual system id this entry belongs to.")
nsIpArpIfIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpIfIdx.setDescription("Interface location.")
nsIpArpState = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,4,1,)).subtype(namedValues=NamedValues(("pending", 1), ("valid", 2), ("delete", 3), ("static", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpState.setDescription("ARP entry state.")
nsIpArpAge = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpAge.setDescription("ARP entry age.")
nsIpArpRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpRetry.setDescription("ARP entry retry time.")
nsIpArpPakQue = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 17, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsIpArpPakQue.setDescription("ARP entry package queue.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-IP-ARP-MIB", PYSNMP_MODULE_ID=nsIpArp)

# Objects
mibBuilder.exportSymbols("NETSCREEN-IP-ARP-MIB", nsIpArp=nsIpArp, nsIpArpAOD=nsIpArpAOD, nsIpArpCachUpdate=nsIpArpCachUpdate, nsIpArpTable=nsIpArpTable, nsIpArpEntry=nsIpArpEntry, nsIpArpIndex=nsIpArpIndex, nsIpArpIp=nsIpArpIp, nsIpArpMac=nsIpArpMac, nsIpArpVsys=nsIpArpVsys, nsIpArpIfIdx=nsIpArpIfIdx, nsIpArpState=nsIpArpState, nsIpArpAge=nsIpArpAge, nsIpArpRetry=nsIpArpRetry, nsIpArpPakQue=nsIpArpPakQue)

