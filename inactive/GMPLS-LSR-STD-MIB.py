# PySNMP SMI module. Autogenerated from smidump -f python GMPLS-LSR-STD-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:39 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( GmplsSegmentDirectionTC, ) = mibBuilder.importSymbols("GMPLS-TC-STD-MIB", "GmplsSegmentDirectionTC")
( ifCounterDiscontinuityGroup, ifGeneralInformationGroup, ) = mibBuilder.importSymbols("IF-MIB", "ifCounterDiscontinuityGroup", "ifGeneralInformationGroup")
( mplsInSegmentGroup, mplsInSegmentIndex, mplsInterfaceGroup, mplsInterfaceIndex, mplsLsrNotificationGroup, mplsOutSegmentGroup, mplsOutSegmentIndex, mplsPerfGroup, mplsXCGroup, ) = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInSegmentGroup", "mplsInSegmentIndex", "mplsInterfaceGroup", "mplsInterfaceIndex", "mplsLsrNotificationGroup", "mplsOutSegmentGroup", "mplsOutSegmentIndex", "mplsPerfGroup", "mplsXCGroup")
( mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, zeroDotZero, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "zeroDotZero")
( RowPointer, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer")

# Objects

gmplsLsrStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 15)).setRevisions(("2007-02-27 00:00",))
if mibBuilder.loadTexts: gmplsLsrStdMIB.setOrganization("IETF Common Control And Measurement Plane (CCAMP) Working Group")
if mibBuilder.loadTexts: gmplsLsrStdMIB.setContactInfo("       Thomas D. Nadeau\nCisco Systems, Inc.\nEmail: tnadeau@cisco.com\nAdrian Farrel\nOld Dog Consulting\n\n\n\nEmail: adrian@olddog.co.uk\nComments about this document should be emailed directly to the\nCCAMP working group mailing list at ccamp@ops.ietf.org.")
if mibBuilder.loadTexts: gmplsLsrStdMIB.setDescription("Copyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4803; see the RFC itself for\nfull legal notices.\n\nThis MIB module contains managed object definitions for the\nGeneralized Multiprotocol (GMPLS) Label Switching Router as\ndefined in Generalized Multi-Protocol Label Switching (GMPLS)\nArchitecture, Mannie et al., RFC 3945, October 2004.")
gmplsLsrObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 1))
gmplsInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1))
if mibBuilder.loadTexts: gmplsInterfaceTable.setDescription("This table specifies per-interface GMPLS capability and\nassociated information.  It extends the information in the\nmplsInterfaceTable of MPLS-LSR-STD-MIB through a\nsparse augmentation relationship.")
gmplsInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"))
if mibBuilder.loadTexts: gmplsInterfaceEntry.setDescription("A conceptual row in this table is created automatically by an\nLSR for each interface that is both capable of supporting\nGMPLS and configured to support GMPLS.  Note that\nsupport of GMPLS is not limited to control plane signaling,\nbut may include data-plane-only function configured through\nSNMP SET commands performed on this MIB module.\n\n\n\nA conceptual row in this table may also be created via SNMP\nSET commands or automatically by the LSR to supplement a\nconceptual row in the mplsInterfaceTable where the interface\nis not capable of GMPLS but where the other objects carried\nin this row provide useful additional information for an\nMPLS interface.\n\nA conceptual row in this table will exist if and only if a\ncorresponding entry in the mplsInterfaceTable exists, and a\ncorresponding entry in the ifTable exists with ifType = mpls(166).\nIf the associated entry in the ifTable is operationally disabled\n(thus removing the GMPLS capabilities on the interface) or the\nentry in the mplsInterfaceTable is deleted, the corresponding entry\nin this table MUST be deleted shortly thereafter.\n\nThe indexes are the same as for the mplsInterfaceTable.  Thus, the\nentry with index 0 represents the per-platform label space and\ncontains parameters that apply to all interfaces that\nparticipate in the per-platform label space.")
gmplsInterfaceSignalingCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1, 1), Bits().subtype(namedValues=NamedValues(("unknown", 0), ("rsvpGmpls", 1), ("crldpGmpls", 2), ("otherGmpls", 3), )).clone(("rsvpGmpls",))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInterfaceSignalingCaps.setDescription("Defines the signaling capabilities on this interface.  Multiple\nbits may legitimately be set at once, but if 'unknown' is set\nthen no other bit may be set.  Setting no bits implies that GMPLS\nsignaling cannot be performed on this interface and all LSPs\nmust be manually provisioned or that this table entry is only\npresent to supplement an entry in the mplsInterfaceTable by\nproviding the information carried in other objects in this row.")
gmplsInterfaceRsvpHelloPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1, 2), Unsigned32().clone(3000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInterfaceRsvpHelloPeriod.setDescription("Period, in milliseconds, between sending Resource Reservation\nProtocol (RSVP) Hello messages on this interface.  A value of 0\nindicates that no Hello messages should be sent on this\ninterface.\n\nThis object is only valid if gmplsInterfaceSignalingCaps has no\nbits set or includes the rsvpGmpls bit.")
gmplsInSegmentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2))
if mibBuilder.loadTexts: gmplsInSegmentTable.setDescription("This table sparse augments the mplsInSegmentTable of\nMPLS-LSR-STD-MIB to provide GMPLS-specific information about\nincoming segments to an LSR.")
gmplsInSegmentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInSegmentIndex"))
if mibBuilder.loadTexts: gmplsInSegmentEntry.setDescription("An entry in this table extends the representation of an incoming\nsegment represented by an entry in the mplsInSegmentTable in\n\n\n\nMPLS-LSR-STD-MIB through a sparse augmentation.  An entry can be\ncreated by a network administrator via SNMP SET commands, or in\nresponse to signaling protocol events.\n\nNote that the storage type for this entry is given by the value\nof mplsInSegmentStorageType in the corresponding entry of the\nmplsInSegmentTable.")
gmplsInSegmentDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1, 1), GmplsSegmentDirectionTC().clone('forward')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInSegmentDirection.setDescription("This object indicates the direction of data flow on this\nsegment.  This object cannot be modified if\nmplsInSegmentRowStatus for the corresponding entry in the\nmplsInSegmentTable is active(1).")
gmplsInSegmentExtraParamsPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1, 2), RowPointer().clone('0.0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsInSegmentExtraParamsPtr.setDescription("Some tunnels will run over transports that can usefully support\ntechnology-specific additional parameters (for example,\nSynchronous Optical Network (SONET) resource usage).  Such can be\nsupplied from an external table and referenced from here.  A value\nof zeroDotZero in this attribute indicates that there is no such\nadditional information.")
gmplsOutSegmentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3))
if mibBuilder.loadTexts: gmplsOutSegmentTable.setDescription("This table sparse augments the mplsOutSegmentTable of\nMPLS-LSR-STD-MIB to provide GMPLS-specific information about\noutgoing segments from an LSR.")
gmplsOutSegmentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsOutSegmentIndex"))
if mibBuilder.loadTexts: gmplsOutSegmentEntry.setDescription("An entry in this table extends the representation of an outgoing\nsegment represented by an entry in the mplsOutSegmentTable of\nMPLS-LSR-STD-MIB through a sparse augmentation.  An entry can be\ncreated by a network administrator via SNMP SET commands, or in\nresponse to signaling protocol events.\n\nNote that the storage type for this entry is given by the value\nof mplsOutSegmentStorageType in the corresponding entry of the\nmplsOutSegmentTable.")
gmplsOutSegmentDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 1), GmplsSegmentDirectionTC().clone('forward')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsOutSegmentDirection.setDescription("This object indicates the direction of data flow on this\nsegment.  This object cannot be modified if\nmplsOutSegmentRowStatus for the corresponding entry in the\nmplsOutSegmentTable is active(1).")
gmplsOutSegmentTTLDecrement = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 2), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsOutSegmentTTLDecrement.setDescription("This object indicates the amount by which to decrement the Time\nto Live (TTL) of any payload packets forwarded on this segment if\nper-hop decrementing is being done.\n\nA value of zero indicates that no decrement should be made or\nthat per-hop decrementing is not in use.\n\nSee the gmplsTunnelTTLDecrement object in the gmplsTunnelTable\nof GMPLS-TE-STD-MIB for a value by which to decrement the TTL\nfor the whole of a tunnel.\n\nThis object cannot be modified if mplsOutSegmentRowStatus for\nthe associated entry in the mplsOutSegmentTable is active(1).")
gmplsOutSegmentExtraParamsPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 3), RowPointer().clone('0.0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsOutSegmentExtraParamsPtr.setDescription("Some tunnels will run over transports that can usefully support\ntechnology-specific additional parameters (for example, SONET\nresource usage).  Such can be supplied from an external table and\nreferenced from here.\n\nA value of zeroDotZero in this attribute indicates that there is\nno such additional information.")
gmplsLsrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 2))
gmplsLsrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1))
gmplsLsrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2))

# Augmentions

# Groups

gmplsInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 1)).setObjects(*(("GMPLS-LSR-STD-MIB", "gmplsInterfaceSignalingCaps"), ("GMPLS-LSR-STD-MIB", "gmplsInterfaceRsvpHelloPeriod"), ) )
if mibBuilder.loadTexts: gmplsInterfaceGroup.setDescription("Collection of objects that provide additional\ninformation for an MPLS interface and are needed\nfor GMPLS interface configuration and performance\ninformation.")
gmplsInSegmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 2)).setObjects(*(("GMPLS-LSR-STD-MIB", "gmplsInSegmentExtraParamsPtr"), ("GMPLS-LSR-STD-MIB", "gmplsInSegmentDirection"), ) )
if mibBuilder.loadTexts: gmplsInSegmentGroup.setDescription("Collection of objects that provide additional\ninformation for an MPLS in-segment and are needed\nfor GMPLS in-segment configuration and performance\ninformation.")
gmplsOutSegmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 3)).setObjects(*(("GMPLS-LSR-STD-MIB", "gmplsOutSegmentDirection"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentTTLDecrement"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentExtraParamsPtr"), ) )
if mibBuilder.loadTexts: gmplsOutSegmentGroup.setDescription("Collection of objects that provide additional\ninformation for an MPLS out-segment and are needed\nfor GMPLS out-segment configuration and performance\ninformation.")

# Compliances

gmplsLsrModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2, 1)).setObjects(*(("GMPLS-LSR-STD-MIB", "gmplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("IF-MIB", "ifCounterDiscontinuityGroup"), ("GMPLS-LSR-STD-MIB", "gmplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentGroup"), ("IF-MIB", "ifGeneralInformationGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ) )
if mibBuilder.loadTexts: gmplsLsrModuleFullCompliance.setDescription("Compliance statement for agents that provide full support for\nGMPLS-LSR-STD-MIB.\n\nThe mandatory group has to be implemented by all LSRs that\noriginate, terminate, or act as transit for TE-LSPs/tunnels.\nIn addition, depending on the type of tunnels supported, other\ngroups become mandatory as explained below.")
gmplsLsrModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2, 2)).setObjects(*(("GMPLS-LSR-STD-MIB", "gmplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("IF-MIB", "ifGeneralInformationGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("GMPLS-LSR-STD-MIB", "gmplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentGroup"), ("IF-MIB", "ifCounterDiscontinuityGroup"), ) )
if mibBuilder.loadTexts: gmplsLsrModuleReadOnlyCompliance.setDescription("Compliance requirement for implementations that only provide\nread-only support for GMPLS-LSR-STD-MIB.  Such devices can then\nbe monitored but cannot be configured using this MIB module.")

# Exports

# Module identity
mibBuilder.exportSymbols("GMPLS-LSR-STD-MIB", PYSNMP_MODULE_ID=gmplsLsrStdMIB)

# Objects
mibBuilder.exportSymbols("GMPLS-LSR-STD-MIB", gmplsLsrStdMIB=gmplsLsrStdMIB, gmplsLsrObjects=gmplsLsrObjects, gmplsInterfaceTable=gmplsInterfaceTable, gmplsInterfaceEntry=gmplsInterfaceEntry, gmplsInterfaceSignalingCaps=gmplsInterfaceSignalingCaps, gmplsInterfaceRsvpHelloPeriod=gmplsInterfaceRsvpHelloPeriod, gmplsInSegmentTable=gmplsInSegmentTable, gmplsInSegmentEntry=gmplsInSegmentEntry, gmplsInSegmentDirection=gmplsInSegmentDirection, gmplsInSegmentExtraParamsPtr=gmplsInSegmentExtraParamsPtr, gmplsOutSegmentTable=gmplsOutSegmentTable, gmplsOutSegmentEntry=gmplsOutSegmentEntry, gmplsOutSegmentDirection=gmplsOutSegmentDirection, gmplsOutSegmentTTLDecrement=gmplsOutSegmentTTLDecrement, gmplsOutSegmentExtraParamsPtr=gmplsOutSegmentExtraParamsPtr, gmplsLsrConformance=gmplsLsrConformance, gmplsLsrGroups=gmplsLsrGroups, gmplsLsrCompliances=gmplsLsrCompliances)

# Groups
mibBuilder.exportSymbols("GMPLS-LSR-STD-MIB", gmplsInterfaceGroup=gmplsInterfaceGroup, gmplsInSegmentGroup=gmplsInSegmentGroup, gmplsOutSegmentGroup=gmplsOutSegmentGroup)

# Compliances
mibBuilder.exportSymbols("GMPLS-LSR-STD-MIB", gmplsLsrModuleFullCompliance=gmplsLsrModuleFullCompliance, gmplsLsrModuleReadOnlyCompliance=gmplsLsrModuleReadOnlyCompliance)
