# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:53 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressPrefixLength, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType", "InetPortNumber")
( Ipv6Address, Ipv6AddressIfIdentifier, Ipv6AddressPrefix, ) = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address", "Ipv6AddressIfIdentifier", "Ipv6AddressPrefix")
( jnxExampleMibRoot, ) = mibBuilder.importSymbols("JUNIPER-EXPERIMENT-MIB", "jnxExampleMibRoot")
( EnabledStatus, ) = mibBuilder.importSymbols("JUNIPER-MIMSTP-MIB", "EnabledStatus")
( Bits, Counter32, Counter64, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")

# Objects

jnxMobileGatewayExampleMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2)).setRevisions(("2010-11-22 12:00",))
if mibBuilder.loadTexts: jnxMobileGatewayExampleMib.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxMobileGatewayExampleMib.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxMobileGatewayExampleMib.setDescription("This module defines some sample objects pertaining to Mobile-Edge Services.")
jnxMobileGatewayExampleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1))
jnxMobileGatewayExampleSyncStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1))
jnxMobileGatewayTotalRequests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalRequests.setDescription("Total requests made.")
jnxMobileGatewayTotalAccepts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalAccepts.setDescription("Total requests that were accepted.")
jnxMobileGatewayTotalRejects = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalRejects.setDescription("Total requests that were rejected.")
jnxMobileGatewayTotalChallenges = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalChallenges.setDescription("Total challenges received.")
jnxMobileGatewayExampleAsyncStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2))
jnxMobileGatewayTotalRequestTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalRequestTimeouts.setDescription("Total  requests that timed out.")
jnxMobileGatewayTotalRequestTxErrors = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalRequestTxErrors.setDescription("Total  requests transmit errors.")
jnxMobileGatewayTotalResponseErrors = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalResponseErrors.setDescription("Total  response errors.")
jnxMobileGatewayTotalPendingRequests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayTotalPendingRequests.setDescription("Total pending requests.")
jnxMobileGatewayProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3))
if mibBuilder.loadTexts: jnxMobileGatewayProfileTable.setDescription("The table listing Mobile Gateway Test Profiles, key is Profile Name.")
jnxMobileGatewayProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1)).setIndexNames((0, "JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayProfileName"))
if mibBuilder.loadTexts: jnxMobileGatewayProfileEntry.setDescription("An entry representing a Mobile Gateway Test Profile.")
jnxMobileGatewayProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxMobileGatewayProfileName.setDescription("A string that uniquely identifies the Test Profile.")
jnxMobileGatewayProfileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayProfileDescription.setDescription("A string that describes the Test Profile.")
jnxMobileGatewayProfileType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMobileGatewayProfileType.setDescription("Test Profile Type.")
jnxMobileGatewayExampleNotificationVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4))
jnxMobileGatewayExampleServerName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4, 1), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxMobileGatewayExampleServerName.setDescription("The name identifies an external server (charging,AAA,etc) on mobile-gateway.")
jnxMobileGatewayExampleServicePicName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4, 2), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxMobileGatewayExampleServicePicName.setDescription("This identifies the session-pic, in the form ms-a/b/0, where\n<a> is the slot and <b> could be either 0 or 1.")
jnxMobileGatewayExampleServerState = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4, 3), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxMobileGatewayExampleServerState.setDescription("This indicates whether the server status is Up or Down")
jnxMobileGatewayExampleNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 2))

# Augmentions

# Notifications

jnxMobileGatewayExampleServerStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 2, 1)).setObjects(*(("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayExampleServerState"), ("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayExampleServicePicName"), ("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayExampleServerName"), ) )
if mibBuilder.loadTexts: jnxMobileGatewayExampleServerStatus.setDescription("This notification signifies that the specified server has \nchanged state. The ServerName identifies the server, the \nServicePicName identifies the session-pic that originated this\nnotification and ServerState indicates whether server came up or went down.")

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", PYSNMP_MODULE_ID=jnxMobileGatewayExampleMib)

# Objects
mibBuilder.exportSymbols("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", jnxMobileGatewayExampleMib=jnxMobileGatewayExampleMib, jnxMobileGatewayExampleObjects=jnxMobileGatewayExampleObjects, jnxMobileGatewayExampleSyncStats=jnxMobileGatewayExampleSyncStats, jnxMobileGatewayTotalRequests=jnxMobileGatewayTotalRequests, jnxMobileGatewayTotalAccepts=jnxMobileGatewayTotalAccepts, jnxMobileGatewayTotalRejects=jnxMobileGatewayTotalRejects, jnxMobileGatewayTotalChallenges=jnxMobileGatewayTotalChallenges, jnxMobileGatewayExampleAsyncStats=jnxMobileGatewayExampleAsyncStats, jnxMobileGatewayTotalRequestTimeouts=jnxMobileGatewayTotalRequestTimeouts, jnxMobileGatewayTotalRequestTxErrors=jnxMobileGatewayTotalRequestTxErrors, jnxMobileGatewayTotalResponseErrors=jnxMobileGatewayTotalResponseErrors, jnxMobileGatewayTotalPendingRequests=jnxMobileGatewayTotalPendingRequests, jnxMobileGatewayProfileTable=jnxMobileGatewayProfileTable, jnxMobileGatewayProfileEntry=jnxMobileGatewayProfileEntry, jnxMobileGatewayProfileName=jnxMobileGatewayProfileName, jnxMobileGatewayProfileDescription=jnxMobileGatewayProfileDescription, jnxMobileGatewayProfileType=jnxMobileGatewayProfileType, jnxMobileGatewayExampleNotificationVars=jnxMobileGatewayExampleNotificationVars, jnxMobileGatewayExampleServerName=jnxMobileGatewayExampleServerName, jnxMobileGatewayExampleServicePicName=jnxMobileGatewayExampleServicePicName, jnxMobileGatewayExampleServerState=jnxMobileGatewayExampleServerState, jnxMobileGatewayExampleNotifications=jnxMobileGatewayExampleNotifications)

# Notifications
mibBuilder.exportSymbols("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", jnxMobileGatewayExampleServerStatus=jnxMobileGatewayExampleServerStatus)
