# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-ATM-COS-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:48 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( atmVclVci, atmVclVpi, ) = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( jnxCosFcId, ) = mibBuilder.importSymbols("JUNIPER-COS-MIB", "jnxCosFcId")
( jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
( Bits, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

jnxAtmCos = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 21)).setRevisions(("2003-06-20 00:00","2003-04-09 00:00","2003-04-09 00:00","2002-09-04 00:00",))
if mibBuilder.loadTexts: jnxAtmCos.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxAtmCos.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxAtmCos.setDescription("The Juniper enterprise MIB for ATM COS (Class Of\nService) infrastructure. For detailed information on ATM\nCOS, Junos Documentation is recommended as the\nreference.\n\n Abbreviations:\n     COS  - Class Of Service\n     RED  - Random Early Detection\n     PLP  - Packet Loss Priority")
jnxCosAtmVcTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 1))
if mibBuilder.loadTexts: jnxCosAtmVcTable.setDescription("A table of ATM VCs which have COS configured.")
jnxCosAtmVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: jnxCosAtmVcEntry.setDescription("This entry contains COS info specific to an ATM VC.\nEach entry is indexed using ifIndex, vpi and vci of\nthe VC.")
jnxCosAtmVcCosMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 1, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("strict", 0), ("alternate", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcCosMode.setDescription("The mode of COS queue priority for the VC.\n\nstrict mode :\nOne queue of the four queues has strict high priority and\nis always serviced before the rest of the queues. The\nremaining queues are serviced in round robin fashion.\n\nalternate mode :\n One queue has high priority, but the servicing of the\n queues alternates between the high priority queue and the\n rest of the queues.")
jnxCosAtmVcScTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2))
if mibBuilder.loadTexts: jnxCosAtmVcScTable.setDescription("A table of rows representing atm-scheduler config\nparameters for each forwarding class within a specified VC.\n\nNOTE: These schedulers are specific to an atm interface and\nare different from the typical schedulers specified under\nclass-of-service config in CLI. Hence, hereafter, through\nout this mib, scheduler will be referred to as atm-scheduler\nto avoid any confusion.")
jnxCosAtmVcScEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "JUNIPER-COS-MIB", "jnxCosFcId"))
if mibBuilder.loadTexts: jnxCosAtmVcScEntry.setDescription("This entry represents atm-scheduler config parameters per\nforwarding class and per VC.")
jnxCosAtmVcScPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,)).subtype(namedValues=NamedValues(("low", 0), ("high", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScPriority.setDescription("The atm-scheduler priority for the queue associated with\nthe specified forwarding class within the specified VC.")
jnxCosAtmVcScTxWeightType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("cells", 0), ("percent", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScTxWeightType.setDescription("The atm-scheduler transmit-weight-type for the queue\nassociated with the specified forwarding class inside the\nspecified VC.\n\nAn atm-scheduler can specify the transmit-weight-type either\nas number of cells or as a percentage of the queue size.")
jnxCosAtmVcScTxWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScTxWeight.setDescription("The atm-scheduler's transmit weight for the queue\nassociated with the specified forwarding class and the\nspecified VC. This object value is either expressed in\nunits of cells or as a percentage of the total VC\nbandwidth. The unit (value-type) can be determined using\nthe object jnxCosAtmVcScTxWeightType.")
jnxCosAtmVcScDpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("linearRed", 0), ("epd", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScDpType.setDescription("The type of RED drop profile configured for the specified\nforwarding class within the specified VC. A scheduler can\nspecify either linear or constant drop profile.\n\nA constant type drop profile (aka EPD) specifies that when\nthe number of queued cells exceeds a threshold, all the\ncells should be dropped. Whereas a linear type drop profile\nspecifies that only a percentage of cells be dropped based\non the number of queued cells at any time.")
jnxCosAtmVcScLrdpQueueDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScLrdpQueueDepth.setDescription("The maximum queue size in cells, as specified by the linear\nRED drop profile associated with the specified forwarding\nclass within the specified VC.\n\nThis object is valid only when value of object\njnxCosAtmVcScDpType is 'linearRed(0)'.")
jnxCosAtmVcScLrdpLowPlpThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScLrdpLowPlpThresh.setDescription("The threshold percentage of fill-level beyond which low PLP\n(Packet Loss Priority) packets belonging to the specified\nforwarding class within the specified VC are randomly\ndropped. This value is specified by linear RED drop profile\nconfig. \n\nThis object is valid only when value of object\njnxCosAtmVcScDpType is 'linearRed(0)'.")
jnxCosAtmVcScLrdpHighPlpThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcScLrdpHighPlpThresh.setDescription("The threshold percentage of fill-level beyond which high\nPLP (Packet Loss Priority) packets belonging to the\nspecified forwarding class within the specified VC are\nrandomly dropped. This value is specified by linear RED drop\nprofile config. \n\nThis object is valid only when jnxCosAtmVcScDpType is\n'linearRed(0)'.")
jnxCosAtmVcEpdThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcEpdThreshold.setDescription("If a EPD type drop profile is configured for this scheduler\nand if the number of cells queued exceeds this threshold\nvalue, all the cells in the queue are dropped.\n\nThis object has valid value only when jnxCosAtmVcScDpType\nis 'epd(1)'.")
jnxCosAtmVcQstatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3))
if mibBuilder.loadTexts: jnxCosAtmVcQstatsTable.setDescription("A table of per VC and per forwarding class queue stats\nentries.")
jnxCosAtmVcQstatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "JUNIPER-COS-MIB", "jnxCosFcId"))
if mibBuilder.loadTexts: jnxCosAtmVcQstatsEntry.setDescription("This entry contains queue stats for a specified\nforwarding class and specified VC.")
jnxCosAtmVcQstatsOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutPackets.setDescription("The number of packets belonging to the specified\nforwarding class transmitted on the specified VC.")
jnxCosAtmVcQstatsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutBytes.setDescription("The number of bytes belonging to the specified forwarding\nclass that were transmitted on the specified VC.")
jnxCosAtmVcQstatsOutRedDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutRedDropPkts.setDescription("The number of outgoing packets on the specified VC and\nbelonging to the specified forwarding class, that were\nRED-dropped.")
jnxCosAtmVcQstatsOutNonRedDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutNonRedDrops.setDescription("The number of outgoing packets on the specified VC and\nbelonging to the specified forwarding class, that were\ndropped not as a result of RED mechanism, but because of\nerrors in packets.")
jnxCosAtmVcQstatsOutLpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpBytes.setDescription("The number of low PLP (PLP0) bytes transmitted.")
jnxCosAtmVcQstatsOutLpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpPkts.setDescription("The number of low PLP (PLP0) packets transmitted.")
jnxCosAtmVcQstatsOutLpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpDropBytes.setDescription("The number of low PLP (PLP0) bytes dropped at the output\nqueue.")
jnxCosAtmVcQstatsOutHpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutHpDropBytes.setDescription("The number of high PLP (PLP1) bytes dropped at the output\nqueue.")
jnxCosAtmVcQstatsOutLpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutLpDropPkts.setDescription("The number of low PLP (PLP0) packets dropped at the\noutput queue.")
jnxCosAtmVcQstatsOutHpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmVcQstatsOutHpDropPkts.setDescription("The number of high PLP (PLP1) packets dropped at the\noutput queue.")
jnxCosAtmTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4))
if mibBuilder.loadTexts: jnxCosAtmTrunkTable.setDescription("A table of all ATM Trunk CoS entries. Stats and configuration\ninformation is provided for each ATM Trunk CoS interface.")
jnxCosAtmTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-COS-MIB", "jnxCosFcId"))
if mibBuilder.loadTexts: jnxCosAtmTrunkEntry.setDescription("A single ATM Trunk CoS Entry.")
jnxCosAtmTrunkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("strict", 1), ("alternate", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkMode.setDescription("The mode of COS queue priority for the Trunk.\n\nstrict mode :\nOne queue of the four queues has strict high priority and\nis always serviced before the rest of the queues. The\nremaining queues are serviced in round robin fashion.\n\nalternate mode :\nOne queue has high priority, but the servicing of the\nqueues alternates between the high priority queue and the\nrest of the queues.")
jnxCosAtmTrunkScPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("low", 1), ("high", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkScPriority.setDescription("The atm-scheduler priority for the queue associated with\nthe specified forwarding class within the specified Trunk.")
jnxCosAtmTrunkScTxWeightType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("cells", 1), ("percent", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkScTxWeightType.setDescription("The atm-scheduler transmit-weight-type for the queue\nassociated with the specified forwarding class inside the\nspecified Trunk.\n\nAn atm-scheduler can specify the transmit-weight-type either\nas number of cells or as a percentage of the queue size.")
jnxCosAtmTrunkScTxWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkScTxWeight.setDescription("The atm-scheduler's transmit weight for the queue\nassociated with the specified forwarding class and the\nspecified Trunk. This object value is either expressed in\nunits of cells or as a percentage of the total Trunk\nbandwidth. The unit (value-type) can be determined using\nthe object jnxCosAtmTrunkScTxWeightType.")
jnxCosAtmTrunkQaType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,)).subtype(namedValues=NamedValues(("red", 1), ("singleEpd", 2), ("dualEpd", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQaType.setDescription("The atm queue admission type used for the specified Trunk.")
jnxCosAtmTrunkEpdThresholdPlp0 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkEpdThresholdPlp0.setDescription("If an EPD type drop profile is configured for this\nscheduler and if the number of cells queued exceeds this \nthreshold value, all the cells which have plp equal to 0 \nwill be dropped.\n\nThis object has valid value only when jnxCosAtmTrunkQaType\nis singleEpd or dualEpd.")
jnxCosAtmTrunkEpdThresholdPlp1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkEpdThresholdPlp1.setDescription("If a EPD type drop profile is configured for this scheduler\nand if the number of cells queued exceeds this threshold\nvalue, all the cells which have plp equal to 1 will be\ndropped.\n\nThis object has valid value only when jnxCosAtmTrunkQaType\nis dualEpd.")
jnxCosAtmTrunkQstatsOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutPackets.setDescription("The number of packets belonging to the specified\nforwarding class transmitted on the specified Trunk.")
jnxCosAtmTrunkQstatsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutBytes.setDescription("The number of bytes belonging to the specified forwarding\nclass that were transmitted on the specified Trunk.")
jnxCosAtmTrunkQstatsOutDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutDrops.setDescription("The number of outgoing packets on the specified Trunk and\nbelonging to the specified forwarding class, that were\ndropped.")
jnxCosAtmTrunkQstatsOutLpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpBytes.setDescription("The number of low PLP (PLP0) bytes transmitted.")
jnxCosAtmTrunkQstatsOutLpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpPkts.setDescription("The number of low PLP (PLP0) packets transmitted.")
jnxCosAtmTrunkQstatsOutLpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpDropBytes.setDescription("The number of low PLP (PLP0) bytes dropped at the output\nqueue.")
jnxCosAtmTrunkQstatsOutHpDropBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpDropBytes.setDescription("The number of high PLP (PLP1) bytes dropped at the output\nqueue.")
jnxCosAtmTrunkQstatsOutLpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutLpDropPkts.setDescription("The number of low PLP (PLP0) packets dropped at the\noutput queue.")
jnxCosAtmTrunkQstatsOutHpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpDropPkts.setDescription("The number of high PLP (PLP1) packets dropped at the\noutput queue.")
jnxCosAtmTrunkQstatsOutHpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpBytes.setDescription("The number of high PLP (PLP1) bytes transmitted.")
jnxCosAtmTrunkQstatsOutHpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 21, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCosAtmTrunkQstatsOutHpPkts.setDescription("The number of high PLP (PLP1) packets transmitted.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-ATM-COS-MIB", PYSNMP_MODULE_ID=jnxAtmCos)

# Objects
mibBuilder.exportSymbols("JUNIPER-ATM-COS-MIB", jnxAtmCos=jnxAtmCos, jnxCosAtmVcTable=jnxCosAtmVcTable, jnxCosAtmVcEntry=jnxCosAtmVcEntry, jnxCosAtmVcCosMode=jnxCosAtmVcCosMode, jnxCosAtmVcScTable=jnxCosAtmVcScTable, jnxCosAtmVcScEntry=jnxCosAtmVcScEntry, jnxCosAtmVcScPriority=jnxCosAtmVcScPriority, jnxCosAtmVcScTxWeightType=jnxCosAtmVcScTxWeightType, jnxCosAtmVcScTxWeight=jnxCosAtmVcScTxWeight, jnxCosAtmVcScDpType=jnxCosAtmVcScDpType, jnxCosAtmVcScLrdpQueueDepth=jnxCosAtmVcScLrdpQueueDepth, jnxCosAtmVcScLrdpLowPlpThresh=jnxCosAtmVcScLrdpLowPlpThresh, jnxCosAtmVcScLrdpHighPlpThresh=jnxCosAtmVcScLrdpHighPlpThresh, jnxCosAtmVcEpdThreshold=jnxCosAtmVcEpdThreshold, jnxCosAtmVcQstatsTable=jnxCosAtmVcQstatsTable, jnxCosAtmVcQstatsEntry=jnxCosAtmVcQstatsEntry, jnxCosAtmVcQstatsOutPackets=jnxCosAtmVcQstatsOutPackets, jnxCosAtmVcQstatsOutBytes=jnxCosAtmVcQstatsOutBytes, jnxCosAtmVcQstatsOutRedDropPkts=jnxCosAtmVcQstatsOutRedDropPkts, jnxCosAtmVcQstatsOutNonRedDrops=jnxCosAtmVcQstatsOutNonRedDrops, jnxCosAtmVcQstatsOutLpBytes=jnxCosAtmVcQstatsOutLpBytes, jnxCosAtmVcQstatsOutLpPkts=jnxCosAtmVcQstatsOutLpPkts, jnxCosAtmVcQstatsOutLpDropBytes=jnxCosAtmVcQstatsOutLpDropBytes, jnxCosAtmVcQstatsOutHpDropBytes=jnxCosAtmVcQstatsOutHpDropBytes, jnxCosAtmVcQstatsOutLpDropPkts=jnxCosAtmVcQstatsOutLpDropPkts, jnxCosAtmVcQstatsOutHpDropPkts=jnxCosAtmVcQstatsOutHpDropPkts, jnxCosAtmTrunkTable=jnxCosAtmTrunkTable, jnxCosAtmTrunkEntry=jnxCosAtmTrunkEntry, jnxCosAtmTrunkMode=jnxCosAtmTrunkMode, jnxCosAtmTrunkScPriority=jnxCosAtmTrunkScPriority, jnxCosAtmTrunkScTxWeightType=jnxCosAtmTrunkScTxWeightType, jnxCosAtmTrunkScTxWeight=jnxCosAtmTrunkScTxWeight, jnxCosAtmTrunkQaType=jnxCosAtmTrunkQaType, jnxCosAtmTrunkEpdThresholdPlp0=jnxCosAtmTrunkEpdThresholdPlp0, jnxCosAtmTrunkEpdThresholdPlp1=jnxCosAtmTrunkEpdThresholdPlp1, jnxCosAtmTrunkQstatsOutPackets=jnxCosAtmTrunkQstatsOutPackets, jnxCosAtmTrunkQstatsOutBytes=jnxCosAtmTrunkQstatsOutBytes, jnxCosAtmTrunkQstatsOutDrops=jnxCosAtmTrunkQstatsOutDrops, jnxCosAtmTrunkQstatsOutLpBytes=jnxCosAtmTrunkQstatsOutLpBytes, jnxCosAtmTrunkQstatsOutLpPkts=jnxCosAtmTrunkQstatsOutLpPkts, jnxCosAtmTrunkQstatsOutLpDropBytes=jnxCosAtmTrunkQstatsOutLpDropBytes, jnxCosAtmTrunkQstatsOutHpDropBytes=jnxCosAtmTrunkQstatsOutHpDropBytes, jnxCosAtmTrunkQstatsOutLpDropPkts=jnxCosAtmTrunkQstatsOutLpDropPkts, jnxCosAtmTrunkQstatsOutHpDropPkts=jnxCosAtmTrunkQstatsOutHpDropPkts, jnxCosAtmTrunkQstatsOutHpBytes=jnxCosAtmTrunkQstatsOutHpBytes, jnxCosAtmTrunkQstatsOutHpPkts=jnxCosAtmTrunkQstatsOutHpPkts)

