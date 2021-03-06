# PySNMP SMI module. Autogenerated from smidump -f python CISCOTRAP-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 10:13:09 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( cisco, ) = mibBuilder.importSymbols("CISCO-SMI", "cisco")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( locIfReason, ) = mibBuilder.importSymbols("OLD-CISCO-INTERFACES-MIB", "locIfReason")
( authAddr, whyReload, ) = mibBuilder.importSymbols("OLD-CISCO-SYSTEM-MIB", "authAddr", "whyReload")
( loctcpConnElapsed, loctcpConnInBytes, loctcpConnOutBytes, ) = mibBuilder.importSymbols("OLD-CISCO-TCP-MIB", "loctcpConnElapsed", "loctcpConnInBytes", "loctcpConnOutBytes")
( tsLineUser, tslineSesType, ) = mibBuilder.importSymbols("OLD-CISCO-TS-MIB", "tsLineUser", "tslineSesType")
( NotificationType, ) = mibBuilder.importSymbols("RFC-1215", "NotificationType")
( egpNeighAddr, ifDescr, ifType, sysUpTime, tcpConnState, ) = mibBuilder.importSymbols("RFC1213-MIB", "egpNeighAddr", "ifDescr", "ifType", "sysUpTime", "tcpConnState")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Notifications

reload = NotificationType((1, 3, 6, 1, 4, 1, 9, 0, 0)).setObjects(*(("OLD-CISCO-SYSTEM-MIB", "whyReload"), ("RFC1213-MIB", "sysUpTime"), ) )
if mibBuilder.loadTexts: reload.setDescription("A reload trap signifies that the sending\nprotocol entity is reinitializing itself such\nthat the agent's configuration or the protocol\nentity implementation may be altered.")
tcpConnectionClose = NotificationType((1, 3, 6, 1, 4, 1, 9, 0, 1)).setObjects(*(("OLD-CISCO-TCP-MIB", "loctcpConnOutBytes"), ("OLD-CISCO-TCP-MIB", "loctcpConnInBytes"), ("OLD-CISCO-TS-MIB", "tslineSesType"), ("OLD-CISCO-TCP-MIB", "loctcpConnElapsed"), ("RFC1213-MIB", "tcpConnState"), ("OLD-CISCO-TS-MIB", "tsLineUser"), ) )
if mibBuilder.loadTexts: tcpConnectionClose.setDescription("A tty trap signifies that a TCP connection,\npreviously established with the sending\nprotocol entity for the purposes of a tty\nsession, has been terminated.")

# Exports

# Notifications
mibBuilder.exportSymbols("CISCOTRAP-MIB", reload=reload, tcpConnectionClose=tcpConnectionClose)

