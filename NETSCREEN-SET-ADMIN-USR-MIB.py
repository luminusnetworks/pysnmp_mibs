# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-SET-ADMIN-USR-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenSetting, netscreenSettingMibModule, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
( Bits, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenSetAdminUsrMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 11)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-10 00:00","2001-09-28 00:00","2001-05-27 00:00",))
if mibBuilder.loadTexts: netscreenSetAdminUsrMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenSetAdminUsrMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenSetAdminUsrMibModule.setDescription("This module defines the object that are used to monitor admin \nuser")
nsSetAdminUser = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 11))
nsSetAdminUserLocalTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 7, 11, 1))
if mibBuilder.loadTexts: nsSetAdminUserLocalTable.setDescription("This table collects all administration user information stored\nin  local user database.")
nsSetAdminUserLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 7, 11, 1, 1)).setIndexNames((0, "NETSCREEN-SET-ADMIN-USR-MIB", "nsAdminUserLocalIndex"))
if mibBuilder.loadTexts: nsSetAdminUserLocalEntry.setDescription("Local database administration user attributes.")
nsAdminUserLocalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserLocalIndex.setDescription("A unique value for user info table.  Its value ranges between\n0 and 65535 and may not be contiguous.")
nsAdminUserLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 11, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserLocalName.setDescription("Administration user name.")
nsAdminUserLocalPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 11, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserLocalPriv.setDescription("Administration user's privileges. The smaller the value,  the\nhigher the privileges.")
nsAdminUserRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 11, 2))
nsAdminUserRadiusEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 11, 2, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserRadiusEnabled.setDescription("Enable external radius server to authenticate admin user")
nsAdminUserRadiusServer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 11, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserRadiusServer.setDescription("External radius server name")
nsSetAdminUserClientTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 7, 11, 3))
if mibBuilder.loadTexts: nsSetAdminUserClientTable.setDescription("Management Client IP addresses is used to restrict the\nadministration  ability from one or multiple addresses of a\nsubnet.")
nsSetAdminUserClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 7, 11, 3, 1)).setIndexNames((0, "NETSCREEN-SET-ADMIN-USR-MIB", "nsAdminUserClientIndex"))
if mibBuilder.loadTexts: nsSetAdminUserClientEntry.setDescription("An entry containing admin client ip information")
nsAdminUserClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 11, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserClientIndex.setDescription("A unique value for client ip table.  Its value ranges between\n0 and 65535 and may not be contiguous.")
nsAdminUserClientIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 11, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserClientIp.setDescription("Management client ip")
nsAdminUserClientNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 11, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserClientNetmask.setDescription("Management client ip netmask")
nsAdminUserVSYS = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 11, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsAdminUserVSYS.setDescription("Vsys ID of the admin user")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-SET-ADMIN-USR-MIB", PYSNMP_MODULE_ID=netscreenSetAdminUsrMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-SET-ADMIN-USR-MIB", netscreenSetAdminUsrMibModule=netscreenSetAdminUsrMibModule, nsSetAdminUser=nsSetAdminUser, nsSetAdminUserLocalTable=nsSetAdminUserLocalTable, nsSetAdminUserLocalEntry=nsSetAdminUserLocalEntry, nsAdminUserLocalIndex=nsAdminUserLocalIndex, nsAdminUserLocalName=nsAdminUserLocalName, nsAdminUserLocalPriv=nsAdminUserLocalPriv, nsAdminUserRadius=nsAdminUserRadius, nsAdminUserRadiusEnabled=nsAdminUserRadiusEnabled, nsAdminUserRadiusServer=nsAdminUserRadiusServer, nsSetAdminUserClientTable=nsSetAdminUserClientTable, nsSetAdminUserClientEntry=nsSetAdminUserClientEntry, nsAdminUserClientIndex=nsAdminUserClientIndex, nsAdminUserClientIp=nsAdminUserClientIp, nsAdminUserClientNetmask=nsAdminUserClientNetmask, nsAdminUserVSYS=nsAdminUserVSYS)

