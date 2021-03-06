# PySNMP SMI module. Autogenerated from smidump -f python CISCO-CONFIG-MAN-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 10:19:21 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ciscoMgmt, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
( Unsigned64, ) = mibBuilder.importSymbols("CISCO-TC", "Unsigned64")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( DateAndTime, DisplayString, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TruthValue")

# Types

class HistoryEventMedium(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,8,7,4,9,3,1,6,5,)
    namedValues = NamedValues(("erase", 1), ("commandSource", 2), ("running", 3), ("startup", 4), ("local", 5), ("networkTftp", 6), ("networkRcp", 7), ("networkFtp", 8), ("networkScp", 9), )
    

# Objects

ciscoConfigManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 43)).setRevisions(("2007-04-27 00:00","2006-08-17 00:00","2004-06-18 00:00","2002-06-07 00:00","2002-03-12 00:00","1995-11-28 00:00",))
if mibBuilder.loadTexts: ciscoConfigManMIB.setOrganization("Cisco Systems, Inc.")
if mibBuilder.loadTexts: ciscoConfigManMIB.setContactInfo("Cisco Systems\nCustomer Service\n\n\nPostal: 170 W Tasman Drive\nSan Jose, CA  95134\nUSA\n\nTel: +1 800 553-NETS\n\nE-mail: cs-snmp@cisco.com")
if mibBuilder.loadTexts: ciscoConfigManMIB.setDescription("Configuration management MIB.\n\nThe MIB represents a model of configuration data that\nexists in various locations:\n\nrunning       in use by the running system\nterminal      saved to whatever is attached as the terminal        \nlocal         saved locally in NVRAM or flash\nremote        saved to some server on the network\n\nAlthough some of the system functions that relate here\ncan be used for general file storage and transfer, this\nMIB intends to include only such operations as clearly\nrelate to configuration.  Its primary emphasis is to\ntrack changes and saves of the running configuration.\n\nAs saved data moves further from startup use, such as\ninto different local flash files or onto the network,\ntracking becomes difficult to impossible, so the MIB's\ninterest and functions are confined in that area.\n\nInformation from ccmCLIHistoryCommandTable can be used\nto track the exact configuration changes that took\nplace within a particular Configuration History\nevent. NMS' can use this information to update \nthe related components. \nFor example:\n    If commands related only to MPLS are entered\n    then the NMS need to update only the MPLS related\n    management information rather than updating\n    all of its management information.\n    Acronyms and terms:\n\n    CLI   Command Line Interface.")
ciscoConfigManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1))
ccmHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1))
ccmHistoryRunningLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryRunningLastChanged.setDescription("The value of sysUpTime when the running configuration\nwas last changed.\n\n        If the value of ccmHistoryRunningLastChanged is\n        greater than ccmHistoryRunningLastSaved, the \n        configuration has been changed but not saved.")
ccmHistoryRunningLastSaved = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryRunningLastSaved.setDescription("The value of sysUpTime when the running configuration\nwas last saved (written).\n\nIf the value of ccmHistoryRunningLastChanged is \ngreater than ccmHistoryRunningLastSaved, the \nconfiguration has been changed but not saved.\n\nWhat constitutes a safe saving of the running\nconfiguration is a management policy issue beyond the\nscope of this MIB.  For some installations, writing the\nrunning configuration to a terminal may be a way of\ncapturing and saving it.  Others may use local or\nremote storage.  Thus ANY write is considered saving\nfor the purposes of the MIB.")
ccmHistoryStartupLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryStartupLastChanged.setDescription("The value of sysUpTime when the startup configuration\nwas last written to.  In general this is the\ndefault configuration used when cold starting the\nsystem.  It may have been changed by a save of the\nrunning configuration or by a copy from elsewhere.")
ccmHistoryMaxEventEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryMaxEventEntries.setDescription("The maximum number of entries that can be held in\nccmHistoryEventTable.\n\nThe recommended value for implementations is 10.")
ccmHistoryEventEntriesBumped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventEntriesBumped.setDescription("The number of times the oldest entry in\nccmHistoryEventTable was deleted to make room \nfor a new entry.")
ccmHistoryEventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6))
if mibBuilder.loadTexts: ccmHistoryEventTable.setDescription("A table of configuration events on this router.")
ccmHistoryEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1)).setIndexNames((0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"))
if mibBuilder.loadTexts: ccmHistoryEventEntry.setDescription("Information about a configuration event on this\nrouter.")
ccmHistoryEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ccmHistoryEventIndex.setDescription("A monotonically increasing integer for the sole\npurpose of indexing events.  When it reaches the \nmaximum value, an extremely unlikely event, the agent \nwraps the value back to 1 and may flush existing \nentries.")
ccmHistoryEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTime.setDescription("The value of sysUpTime when the event occurred.")
ccmHistoryEventCommandSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("commandLine", 1), ("snmp", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSource.setDescription("The source of the command that instigated the event.")
ccmHistoryEventConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 4), HistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventConfigSource.setDescription("The configuration data source for the event.")
ccmHistoryEventConfigDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 5), HistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventConfigDestination.setDescription("The configuration data destination for the event.")
ccmHistoryEventTerminalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(3,6,2,5,4,1,)).subtype(namedValues=NamedValues(("notApplicable", 1), ("unknown", 2), ("console", 3), ("terminal", 4), ("virtual", 5), ("auxiliary", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalType.setDescription("If ccmHistoryEventCommandSource is 'commandLine',\nthe terminal type, otherwise 'notApplicable'.")
ccmHistoryEventTerminalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalNumber.setDescription("If ccmHistoryEventCommandSource is 'commandLine',\nthe terminal number.  The value is -1 if not available\nor not applicable.")
ccmHistoryEventTerminalUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalUser.setDescription("If ccmHistoryEventCommandSource is 'commandLine',\nthe name of the logged in user.  The length is zero if\nnot available or not applicable.")
ccmHistoryEventTerminalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalLocation.setDescription("If ccmHistoryEventCommandSource is 'commandLine',\nthe hard-wired location of the terminal or the remote \nhost for an incoming connection.  The length is zero \nif not available or not applicable.")
ccmHistoryEventCommandSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddress.setDescription("If ccmHistoryEventTerminalType is 'virtual', the\ninternet address of the connected system.\n\nIf ccmHistoryEventCommandSource is 'snmp', the internet\naddress of the requester.\n\nThe value is 0.0.0.0 if not available or not \napplicable.\n\nThis object is deprecated by\nccmHistoryEventCommandSourceAddrRev1")
ccmHistoryEventVirtualHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventVirtualHostName.setDescription("If ccmHistoryEventTerminalType is 'virtual', the host\nname of the connected system.  The length is zero if\nnot available or not applicable.")
ccmHistoryEventServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddress.setDescription("If ccmHistoryEventConfigSource or\nccmHistoryEventConfigDestination is 'networkTftp' or\n'networkRcp', the internet address of the storage file\nserver.  The value is 0.0.0.0 if not applicable or not\n        available.\n        This object is deprecated by\n        ccmHistoryEventServerAddrRev1")
ccmHistoryEventFile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventFile.setDescription("If ccmHistoryEventConfigSource or\nccmHistoryEventConfigDestination is 'networkTftp' or\n'networkRcp', the configuration file name at the\nstorage file server.  The length is zero if not\navailable or not applicable.")
ccmHistoryEventRcpUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventRcpUser.setDescription("If ccmHistoryEventConfigSource or\nccmHistoryEventConfigDestination is 'networkRcp', the\nremote user name.  The length is zero if not applicable\nor not available.")
ccmHistoryCLICmdEntriesBumped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryCLICmdEntriesBumped.setDescription("The number of times the oldest entry in\nccmCLIHistoryCommandTable with first index as \nccmHistoryEventIndex was deleted to make \nroom for a new entry.\n\nThis object is applicable only if \nccmHistoryEventCommandSource has a value \nof 'commandLine'.")
ccmHistoryEventCommandSourceAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 16), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrType.setDescription("This object indicates the transport type of the\naddress contained in\nccmHistoryEventCommandSourceAddrRev1.\n\nThe value will be zero if not available or not\napplicable.")
ccmHistoryEventCommandSourceAddrRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 17), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrRev1.setDescription("If ccmHistoryEventTerminalType is 'virtual', the\ninternet address of the connected system.\n\nIf ccmHistoryEventCommandSource is 'snmp', the\ninternet address of the requester.\n\nThe value of all bit's is zero  if not available or\nnot applicable.\n\nThe Format of this address depends on the value of the\nccmHistoryEventCommandSourceAddrType object.\n\nThis object deprecates\nccmHistoryEventCommandSourceAddress")
ccmHistoryEventServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 18), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddrType.setDescription("This object indicates the transport type of the\naddress contained in ccmHistoryEventServerAddrRev1.\n\nThe value will be zero if not available or not\naplicable.")
ccmHistoryEventServerAddrRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 19), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddrRev1.setDescription("If ccmHistoryEventConfigSource or\nccmHistoryEventConfigDestination is 'networkTftp' or\n'networkRcp', the internet address of the storage file\nserver. \n\nThe value of all bits is 0s if not applicable or not\navailable.\n\nThe Format of this address depends on the value of the\nccmHistoryEventServerAddrType object.\n\nThis object deprecates ccmHistoryEventServerAddress.")
ccmCLIHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2))
ccmCLIHistoryMaxCmdEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCLIHistoryMaxCmdEntries.setDescription("The maximum number of entries that can be held in\nccmCLIHistoryCommandTable.\n\nThe recommended value for implementations is 100.\n\nIf the number of entries in ccmCLIHistoryCommandTable \nexceeds the value of this object, old entries will be \nbumped to make room for new entries.\n\nThe ccmCLIHistoryCommandTable will not be populated\nif the value of this object is 0.")
ccmCLIHistoryCmdEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntries.setDescription("The current number of entries in\nccmCLIHistoryCommandTable.")
ccmCLIHistoryCmdEntriesAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntriesAllowed.setDescription("This object indicates the upper limit on the\nnumber of entries allowed in \nccmCLIHistoryCommandTable by the managed system.")
ccmCLIHistoryCommandTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4))
if mibBuilder.loadTexts: ccmCLIHistoryCommandTable.setDescription("A table of CLI commands that took effect during\nconfiguration events.")
ccmCLIHistoryCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1)).setIndexNames((0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"), (0, "CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommandIndex"))
if mibBuilder.loadTexts: ccmCLIHistoryCommandEntry.setDescription("Information about the CLI commands that took effect\nduring the configuration event pointed by \nccmCLIHistoryEventIndex.\n\nA set of rows in this table having the first\nindex as ccmHistoryEventIndex will store the\nCLI commands entered during the corresponding \nconfiguration event in ccmHistoryEventTable.\n\nAn entry will be created in this table only if \nthe corresponding entry in ccmHistoryEventTable has \na value of 'commandLine' for \nccmHistoryEventCommandSource.")
ccmCLIHistoryCommandIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ccmCLIHistoryCommandIndex.setDescription("A monotonically increasing integer for the\npurpose of indexing CLI commands which took effect\nduring a configuration event.")
ccmCLIHistoryCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCommand.setDescription("The CLI command entered which took effect\nduring the configuration event pointed by \nccmHistoryEventIndex.")
ccmCLICfg = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3))
ccmCLICfgRunConfNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCLICfgRunConfNotifEnable.setDescription("This variable indicates whether the system produces\nthe ccmCLIRunningConfigChanged notification. A false \nvalue will prevent notifications from being generated \nby this system.")
ccmCTIDObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4))
ccmCTID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 1), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTID.setDescription("This object indicates the Config Change Tracking ID which\nuniquely represents version-incrementing changes to the IOS \nrunning configuration.")
ccmCTIDLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTIDLastChangeTime.setDescription("This object indicates the time when the Config Change Tracking\nID last changed.")
ccmCTIDWhoChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTIDWhoChanged.setDescription("This object indicates the user who last reset the Config Change\nTracking ID.")
ccmCTIDRolledOverNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCTIDRolledOverNotifEnable.setDescription("This variable indicates whether the system produces the\nccmCTIDRolledOver notification. A false value will prevent\nnotifications from being generated by this system.")
ciscoConfigManMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 2))
ciscoConfigManMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0))
ciscoConfigManMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3))
ciscoConfigManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1))
ciscoConfigManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2))

# Augmentions

# Notifications

ciscoConfigManEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 1)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ) )
if mibBuilder.loadTexts: ciscoConfigManEvent.setDescription("Notification of a configuration management event as\nrecorded in ccmHistoryEventTable.")
ccmCLIRunningConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 2)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ) )
if mibBuilder.loadTexts: ccmCLIRunningConfigChanged.setDescription("This notification indicates that the running\nconfiguration of the managed system has changed\nfrom the CLI.\n\nIf the managed system supports a separate \nconfiguration mode(where the configuration commands \nare entered under a  configuration session which \naffects the running configuration of the system), \nthen this notification is sent when the configuration \nmode is exited.\nDuring this configuration session there can be \none or more running configuration changes.")
ccmCTIDRolledOver = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 3)).setObjects(*() )
if mibBuilder.loadTexts: ccmCTIDRolledOver.setDescription("This notification indicates that the Config Change Tracking\nID has rolled over and will be reset.")

# Groups

ciscoConfigManHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 1)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ) )
if mibBuilder.loadTexts: ciscoConfigManHistoryGroup.setDescription("Configuration history.")
ciscoConfigManHistoryGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 2)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ) )
if mibBuilder.loadTexts: ciscoConfigManHistoryGroupRev1.setDescription("Configuration history.")
ciscoConfigManHistNotifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 3)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManEvent"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIRunningConfigChanged"), ) )
if mibBuilder.loadTexts: ciscoConfigManHistNotifyGroup.setDescription("Notifications of a configuration management event.")
ciscoConfigManCLIHistCmdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 4)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommand"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntriesAllowed"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryMaxCmdEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmCLICfgRunConfNotifEnable"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntries"), ) )
if mibBuilder.loadTexts: ciscoConfigManCLIHistCmdGroup.setDescription("CLI commands entered during a configuration history\nevent.")
ciscoConfigManHistoryGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 5)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrRev1"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrRev1"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ) )
if mibBuilder.loadTexts: ciscoConfigManHistoryGroupRev2.setDescription("Configuration history.\n\nThis group deprecates the old group\nciscoConfigManHistoryGroupRev1")
ciscoConfigManCTIDNotifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 6)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOver"), ) )
if mibBuilder.loadTexts: ciscoConfigManCTIDNotifyGroup.setDescription("Notifications of a Config Change Tracking ID event.")
ciscoConfigManCTIDObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 7)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOverNotifEnable"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDWhoChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmCTID"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDLastChangeTime"), ) )
if mibBuilder.loadTexts: ciscoConfigManCTIDObjectGroup.setDescription("Information about the current CTID value, when CTID last\nchanged, and who last changed the CTID.")

# Compliances

ciscoConfigManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 1)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroup"), ) )
if mibBuilder.loadTexts: ciscoConfigManMIBCompliance.setDescription("The compliance statement for entities which implement\nthe Cisco Configuration Management MIB")
ciscoConfigManMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 2)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev1"), ) )
if mibBuilder.loadTexts: ciscoConfigManMIBComplianceRev2.setDescription("The compliance statement for entities which implement\nthe Cisco Configuration Management MIB")
ciscoConfigManMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 3)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev2"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ) )
if mibBuilder.loadTexts: ciscoConfigManMIBComplianceRev3.setDescription("The compliance statement for entities which implement\nthe Cisco Configuration Management MIB.\n\nThis compliance module deprecates\nciscoConfigManMIBCompliance.")
ciscoConfigManMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 4)).setObjects(*(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCTIDNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev2"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCTIDObjectGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ) )
if mibBuilder.loadTexts: ciscoConfigManMIBComplianceRev4.setDescription("The compliance statement for entities which implement\nthe Cisco Configuration Management MIB.\n\nThis compliance module deprecates\nciscoConfigManMIBCompliance.")

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", PYSNMP_MODULE_ID=ciscoConfigManMIB)

# Types
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", HistoryEventMedium=HistoryEventMedium)

# Objects
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", ciscoConfigManMIB=ciscoConfigManMIB, ciscoConfigManMIBObjects=ciscoConfigManMIBObjects, ccmHistory=ccmHistory, ccmHistoryRunningLastChanged=ccmHistoryRunningLastChanged, ccmHistoryRunningLastSaved=ccmHistoryRunningLastSaved, ccmHistoryStartupLastChanged=ccmHistoryStartupLastChanged, ccmHistoryMaxEventEntries=ccmHistoryMaxEventEntries, ccmHistoryEventEntriesBumped=ccmHistoryEventEntriesBumped, ccmHistoryEventTable=ccmHistoryEventTable, ccmHistoryEventEntry=ccmHistoryEventEntry, ccmHistoryEventIndex=ccmHistoryEventIndex, ccmHistoryEventTime=ccmHistoryEventTime, ccmHistoryEventCommandSource=ccmHistoryEventCommandSource, ccmHistoryEventConfigSource=ccmHistoryEventConfigSource, ccmHistoryEventConfigDestination=ccmHistoryEventConfigDestination, ccmHistoryEventTerminalType=ccmHistoryEventTerminalType, ccmHistoryEventTerminalNumber=ccmHistoryEventTerminalNumber, ccmHistoryEventTerminalUser=ccmHistoryEventTerminalUser, ccmHistoryEventTerminalLocation=ccmHistoryEventTerminalLocation, ccmHistoryEventCommandSourceAddress=ccmHistoryEventCommandSourceAddress, ccmHistoryEventVirtualHostName=ccmHistoryEventVirtualHostName, ccmHistoryEventServerAddress=ccmHistoryEventServerAddress, ccmHistoryEventFile=ccmHistoryEventFile, ccmHistoryEventRcpUser=ccmHistoryEventRcpUser, ccmHistoryCLICmdEntriesBumped=ccmHistoryCLICmdEntriesBumped, ccmHistoryEventCommandSourceAddrType=ccmHistoryEventCommandSourceAddrType, ccmHistoryEventCommandSourceAddrRev1=ccmHistoryEventCommandSourceAddrRev1, ccmHistoryEventServerAddrType=ccmHistoryEventServerAddrType, ccmHistoryEventServerAddrRev1=ccmHistoryEventServerAddrRev1, ccmCLIHistory=ccmCLIHistory, ccmCLIHistoryMaxCmdEntries=ccmCLIHistoryMaxCmdEntries, ccmCLIHistoryCmdEntries=ccmCLIHistoryCmdEntries, ccmCLIHistoryCmdEntriesAllowed=ccmCLIHistoryCmdEntriesAllowed, ccmCLIHistoryCommandTable=ccmCLIHistoryCommandTable, ccmCLIHistoryCommandEntry=ccmCLIHistoryCommandEntry, ccmCLIHistoryCommandIndex=ccmCLIHistoryCommandIndex, ccmCLIHistoryCommand=ccmCLIHistoryCommand, ccmCLICfg=ccmCLICfg, ccmCLICfgRunConfNotifEnable=ccmCLICfgRunConfNotifEnable, ccmCTIDObjects=ccmCTIDObjects, ccmCTID=ccmCTID, ccmCTIDLastChangeTime=ccmCTIDLastChangeTime, ccmCTIDWhoChanged=ccmCTIDWhoChanged, ccmCTIDRolledOverNotifEnable=ccmCTIDRolledOverNotifEnable, ciscoConfigManMIBNotificationPrefix=ciscoConfigManMIBNotificationPrefix, ciscoConfigManMIBNotifications=ciscoConfigManMIBNotifications, ciscoConfigManMIBConformance=ciscoConfigManMIBConformance, ciscoConfigManMIBCompliances=ciscoConfigManMIBCompliances, ciscoConfigManMIBGroups=ciscoConfigManMIBGroups)

# Notifications
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", ciscoConfigManEvent=ciscoConfigManEvent, ccmCLIRunningConfigChanged=ccmCLIRunningConfigChanged, ccmCTIDRolledOver=ccmCTIDRolledOver)

# Groups
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", ciscoConfigManHistoryGroup=ciscoConfigManHistoryGroup, ciscoConfigManHistoryGroupRev1=ciscoConfigManHistoryGroupRev1, ciscoConfigManHistNotifyGroup=ciscoConfigManHistNotifyGroup, ciscoConfigManCLIHistCmdGroup=ciscoConfigManCLIHistCmdGroup, ciscoConfigManHistoryGroupRev2=ciscoConfigManHistoryGroupRev2, ciscoConfigManCTIDNotifyGroup=ciscoConfigManCTIDNotifyGroup, ciscoConfigManCTIDObjectGroup=ciscoConfigManCTIDObjectGroup)

# Compliances
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", ciscoConfigManMIBCompliance=ciscoConfigManMIBCompliance, ciscoConfigManMIBComplianceRev2=ciscoConfigManMIBComplianceRev2, ciscoConfigManMIBComplianceRev3=ciscoConfigManMIBComplianceRev3, ciscoConfigManMIBComplianceRev4=ciscoConfigManMIBComplianceRev4)
