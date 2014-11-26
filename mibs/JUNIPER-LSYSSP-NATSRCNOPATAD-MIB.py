# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-LSYSSP-NATSRCNOPATAD-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:52 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxLsysSpNATsrcnopatad, ) = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATsrcnopatad")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxLsysSpNATsrcnopatadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1)).setRevisions(("2010-05-19 16:44",))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\n\nE-mail: support@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setDescription("This module defines the NAT-src-no-pat-address-specific MIB for \nJuniper Enterprise Logical-System (LSYS) security profiles.  \nJuniper documentation is recommended as the reference. \n\nThe LSYS security profile provides various static and dynamic \nresource management by observing resource quota limits. \nSecurity NAT-src-no-pat-address resource is the focus in this MIB. ")
jnxLsysSpNATsrcnopatadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1))
jnxLsysSpNATsrcnopatadTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadTable.setDescription("LSYSPROFILE NAT-src-no-pat-address objects for NAT-src-no-pat-\naddress resource consumption per LSYS.")
jnxLsysSpNATsrcnopatadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1)).setIndexNames((1, "JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", "jnxLsysSpNATsrcnopatadLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadEntry.setDescription("An entry in NAT-src-no-pat-address resource table.")
jnxLsysSpNATsrcnopatadLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLsysName.setDescription("The name of the logical system for which NAT-src-no-pat-address \nresource information is retrieved. ")
jnxLsysSpNATsrcnopatadProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadProfileName.setDescription("The security profile name string for the LSYS.")
jnxLsysSpNATsrcnopatadUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsage.setDescription("The current resource usage count for the LSYS.")
jnxLsysSpNATsrcnopatadReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadReserved.setDescription("The reserved resource count for the LSYS.")
jnxLsysSpNATsrcnopatadMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaximum.setDescription("The maximum allowed resource usage count for the LSYS.")
jnxLsysSpNATsrcnopatadSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2))
jnxLsysSpNATsrcnopatadUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsedAmount.setDescription("The NAT-src-no-pat-address resource consumption over all LSYS.")
jnxLsysSpNATsrcnopatadMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaxQuota.setDescription("The NAT-src-no-pat-address resource maximum quota for the whole \ndevice for all LSYS.")
jnxLsysSpNATsrcnopatadAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadAvailableAmount.setDescription("The NAT-src-no-pat-address resource available in the whole device.")
jnxLsysSpNATsrcnopatadHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUsage.setDescription("The most amount of NAT-src-no-pat-address resource consumed of a \nLSYS.")
jnxLsysSpNATsrcnopatadHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUser.setDescription("The LSYS name that consume the most NAT-src-no-pat-address resource.")
jnxLsysSpNATsrcnopatadLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUsage.setDescription("The least amount of NAT-src-no-pat-address resource consumed of a \nLSYS.")
jnxLsysSpNATsrcnopatadLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUser.setDescription("The LSYS name that consume the least NAT-src-no-pat-address resource.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", PYSNMP_MODULE_ID=jnxLsysSpNATsrcnopatadMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", jnxLsysSpNATsrcnopatadMIB=jnxLsysSpNATsrcnopatadMIB, jnxLsysSpNATsrcnopatadObjects=jnxLsysSpNATsrcnopatadObjects, jnxLsysSpNATsrcnopatadTable=jnxLsysSpNATsrcnopatadTable, jnxLsysSpNATsrcnopatadEntry=jnxLsysSpNATsrcnopatadEntry, jnxLsysSpNATsrcnopatadLsysName=jnxLsysSpNATsrcnopatadLsysName, jnxLsysSpNATsrcnopatadProfileName=jnxLsysSpNATsrcnopatadProfileName, jnxLsysSpNATsrcnopatadUsage=jnxLsysSpNATsrcnopatadUsage, jnxLsysSpNATsrcnopatadReserved=jnxLsysSpNATsrcnopatadReserved, jnxLsysSpNATsrcnopatadMaximum=jnxLsysSpNATsrcnopatadMaximum, jnxLsysSpNATsrcnopatadSummary=jnxLsysSpNATsrcnopatadSummary, jnxLsysSpNATsrcnopatadUsedAmount=jnxLsysSpNATsrcnopatadUsedAmount, jnxLsysSpNATsrcnopatadMaxQuota=jnxLsysSpNATsrcnopatadMaxQuota, jnxLsysSpNATsrcnopatadAvailableAmount=jnxLsysSpNATsrcnopatadAvailableAmount, jnxLsysSpNATsrcnopatadHeaviestUsage=jnxLsysSpNATsrcnopatadHeaviestUsage, jnxLsysSpNATsrcnopatadHeaviestUser=jnxLsysSpNATsrcnopatadHeaviestUser, jnxLsysSpNATsrcnopatadLightestUsage=jnxLsysSpNATsrcnopatadLightestUsage, jnxLsysSpNATsrcnopatadLightestUser=jnxLsysSpNATsrcnopatadLightestUser)
