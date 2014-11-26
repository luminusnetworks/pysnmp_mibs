# PySNMP SMI module. Autogenerated from smidump -f python ADSL-LINE-EXT-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:30 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( adslAtucIntervalEntry, adslAtucPerfDataEntry, adslAturIntervalEntry, adslAturPerfDataEntry, adslLineAlarmConfProfileEntry, adslLineConfProfileEntry, adslLineEntry, adslMIB, ) = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAtucIntervalEntry", "adslAtucPerfDataEntry", "adslAturIntervalEntry", "adslAturPerfDataEntry", "adslLineAlarmConfProfileEntry", "adslLineConfProfileEntry", "adslLineEntry", "adslMIB")
( AdslPerfCurrDayCount, AdslPerfPrevDayCount, ) = mibBuilder.importSymbols("ADSL-TC-MIB", "AdslPerfCurrDayCount", "AdslPerfPrevDayCount")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( PerfCurrentCount, PerfIntervalCount, ) = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class AdslTransmissionModeType(Bits):
    namedValues = NamedValues(("ansit1413", 0), ("etsi", 1), ("q9922tcmIsdnNonOverlapped", 10), ("q9922tcmIsdnOverlapped", 11), ("q9921tcmIsdnSymmetric", 12), ("q9921PotsNonOverlapped", 2), ("q9921PotsOverlapped", 3), ("q9921IsdnNonOverlapped", 4), ("q9921isdnOverlapped", 5), ("q9921tcmIsdnNonOverlapped", 6), ("q9921tcmIsdnOverlapped", 7), ("q9922potsNonOverlapeed", 8), ("q9922potsOverlapped", 9), )
    

# Objects

adslExtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 3)).setRevisions(("2002-12-10 00:00",))
if mibBuilder.loadTexts: adslExtMIB.setOrganization("IETF ADSL MIB Working Group")
if mibBuilder.loadTexts: adslExtMIB.setContactInfo("\nFaye Ly\nPedestal Networks\n6503 Dumbarton Circle,\nFremont, CA 94555\nTel: +1 510-578-0158\nFax: +1 510-744-5152\nE-Mail: faye@pedestalnetworks.com\n\nGregory Bathrick\nNokia Networks\n2235 Mercury Way,\nFax: +1 707-535-7300\nE-Mail: greg.bathrick@nokia.com\n\nGeneral Discussion:adslmib@ietf.org\nTo Subscribe: https://www1.ietf.org/mailman/listinfo/adslmib\nArchive: https://www1.ietf.org/mailman/listinfo/adslmib")
if mibBuilder.loadTexts: adslExtMIB.setDescription("Copyright (C) The Internet Society (2002). This version of\nthis MIB module is part of RFC 3440; see the RFC itself for\nfull legal notices.\n\nThis MIB Module is a supplement to the ADSL-LINE-MIB\n[RFC2662].")
adslExtMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1))
adslLineExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17))
if mibBuilder.loadTexts: adslLineExtTable.setDescription("This table is an extension of RFC 2662.  It\ncontains ADSL line configuration and\nmonitoring information. This includes the ADSL\nline's capabilities and actual ADSL transmission\nsystem.")
adslLineExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1))
if mibBuilder.loadTexts: adslLineExtEntry.setDescription("An entry extends the adslLineEntry defined in\n[RFC2662].  Each entry corresponds to an ADSL\nline.")
adslLineTransAtucCap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 1), AdslTransmissionModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslLineTransAtucCap.setDescription("The transmission modes, represented by a\nbitmask that the ATU-C is capable of\nsupporting.  The modes available are limited\nby the design of the equipment.")
adslLineTransAtucConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 2), AdslTransmissionModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adslLineTransAtucConfig.setDescription("The transmission modes, represented by a bitmask,\ncurrently enabled by the ATU-C.  The manager can\nonly set those modes that are supported by the\n\n\n\nATU-C.  An ATU-C's supported modes are provided by\nAdslLineTransAtucCap.")
adslLineTransAtucActual = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 3), AdslTransmissionModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslLineTransAtucActual.setDescription("The actual transmission mode of the ATU-C.\nDuring ADSL line initialization, the ADSL\nTransceiver Unit - Remote terminal end (ATU-R)\nwill determine the mode used for the link.\nThis value will be limited a single transmission\nmode that is a subset of those modes enabled\nby the ATU-C and denoted by\nadslLineTransAtucConfig. After an initialization\nhas occurred, its mode is saved as the 'Current'\nmode and is persistence should the link go\ndown. This object returns 0 (i.e. BITS with no\nmode bit set) if the mode is not known.")
adslLineGlitePowerState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,4,2,)).subtype(namedValues=NamedValues(("none", 1), ("l0", 2), ("l1", 3), ("l3", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslLineGlitePowerState.setDescription("The value of this object specifies the power\nstate of this interface.  L0 is power on, L1 is\npower on but reduced and L3 is power off.  Power\nstate cannot be configured by an operator but it\ncan be viewed via the ifOperStatus object for the\nmanaged ADSL interface.  The value of the object\nifOperStatus is set to down(2) if the ADSL\ninterface is in power state L3 and is set to up(1)\nif the ADSL line interface is in power state L0 or\nL1. If the object adslLineTransAtucActual is set to\na G.992.2 (G.Lite)-type transmission mode, the\nvalue of this object will be one of the valid power\nstates: L0(2), L1(3), or L3(4).  Otherwise, its\n\n\n\nvalue will be none(1).")
adslLineConfProfileDualLite = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adslLineConfProfileDualLite.setDescription("This object extends the definition an ADSL line and\nassociated channels (when applicable) for cases\nwhen it is configured in dual mode, and operating\nin a G.Lite-type mode as denoted by\nadslLineTransAtucActual.  Dual mode exists when the\nobject, adslLineTransAtucConfig, is configured with\none or more full-rate modes and one or more G.Lite\nmodes simultaneously.\n\nWhen 'dynamic' profiles are implemented, the value\nof object is equal to the index of the applicable\nrow in the ADSL Line Configuration Profile Table,\nAdslLineConfProfileTable defined in ADSL-MIB\n[RFC2662].\n\nIn the case when dual-mode has not been enabled,\nthe value of the object will be equal to the value\nof the object adslLineConfProfile [RFC2662].\n\nWhen `static' profiles are implemented, in much\nlike the case of the object,\nadslLineConfProfileName [RFC2662], this object's\nvalue will need to algorithmically represent the\ncharacteristics of the line.  In this case, the\nvalue of the line's ifIndex plus a value indicating\nthe line mode type (e.g., G.Lite, Full-rate) will\nbe used. Therefore, the profile's name is a string\nconcatenating the ifIndex and one of the follow\nvalues: Full or Lite. This string will be\nfixed-length (i.e., 14) with leading zero(s).  For\nexample, the profile name for ifIndex that equals\n'15' and is a full rate line, it will be\n'0000000015Full'.")
adslAtucPerfDataExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18))
if mibBuilder.loadTexts: adslAtucPerfDataExtTable.setDescription("This table extends adslAtucPerfDataTable [RFC2662]\nwith additional ADSL physical line counter\ninformation such as unavailable seconds-line and\nseverely errored seconds-line.")
adslAtucPerfDataExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1))
if mibBuilder.loadTexts: adslAtucPerfDataExtEntry.setDescription("An entry extends the adslAtucPerfDataEntry defined\nin [RFC2662].  Each entry corresponds to an ADSL\nline.")
adslAtucPerfStatFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatFastR.setDescription("The value of this object reports the count of\nthe number of fast line bs since last\nagent reset.")
adslAtucPerfStatFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatFailedFastR.setDescription("The value of this object reports the count of\nthe number of failed fast line retrains since\nlast agent reset.")
adslAtucPerfStatSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatSesL.setDescription("The value of this object reports the count of\nthe number of severely errored seconds-line since\nlast agent reset.")
adslAtucPerfStatUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatUasL.setDescription("The value of this object reports the count of\nthe number of unavailable seconds-line since\nlast agent reset.")
adslAtucPerfCurr15MinFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinFastR.setDescription("For the current 15-minute interval,\nadslAtucPerfCurr15MinFastR reports the current\nnumber of seconds during which there have been\n\n\n\nfast retrains.")
adslAtucPerfCurr15MinFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinFailedFastR.setDescription("For the current 15-minute interval,\nadslAtucPerfCurr15MinFailedFastR reports the\ncurrent number of seconds during which there\nhave been failed fast retrains.")
adslAtucPerfCurr15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinSesL.setDescription("For the current 15-minute interval,\nadslAtucPerfCurr15MinSesL reports the current\nnumber of seconds during which there have been\nseverely errored seconds-line.")
adslAtucPerfCurr15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 8), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinUasL.setDescription("For the current 15-minute interval,\nadslAtucPerfCurr15MinUasL reports the current\nnumber of seconds during which there have been\nunavailable seconds-line.")
adslAtucPerfCurr1DayFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 9), AdslPerfCurrDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DayFastR.setDescription("For the current day as measured by\nadslAtucPerfCurr1DayTimeElapsed [RFC2662],\nadslAtucPerfCurr1DayFastR reports the number\nof seconds during which there have been\nfast retrains.")
adslAtucPerfCurr1DayFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 10), AdslPerfCurrDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DayFailedFastR.setDescription("For the current day as measured by\nadslAtucPerfCurr1DayTimeElapsed [RFC2662],\nadslAtucPerfCurr1DayFailedFastR reports the\nnumber of seconds during which there have been\nfailed fast retrains.")
adslAtucPerfCurr1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 11), AdslPerfCurrDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DaySesL.setDescription("For the current day as measured by\nadslAtucPerfCurr1DayTimeElapsed [RFC2662],\nadslAtucPerfCurr1DaySesL reports the\nnumber of seconds during which there have been\nseverely errored seconds-line.")
adslAtucPerfCurr1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 12), AdslPerfCurrDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DayUasL.setDescription("For the current day as measured by\nadslAtucPerfCurr1DayTimeElapsed [RFC2662],\nadslAtucPerfCurr1DayUasL reports the\nnumber of seconds during which there have been\nunavailable seconds-line.")
adslAtucPerfPrev1DayFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 13), AdslPerfPrevDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DayFastR.setDescription("For the previous day, adslAtucPerfPrev1DayFastR\nreports the number of seconds during which there\nwere fast retrains.")
adslAtucPerfPrev1DayFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 14), AdslPerfPrevDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DayFailedFastR.setDescription("For the previous day,\nadslAtucPerfPrev1DayFailedFastR reports the number\nof seconds during which there were failed fast\nretrains.")
adslAtucPerfPrev1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 15), AdslPerfPrevDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DaySesL.setDescription("For the previous day, adslAtucPerfPrev1DaySesL\nreports the number of seconds during which there\nwere severely errored seconds-line.")
adslAtucPerfPrev1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 16), AdslPerfPrevDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DayUasL.setDescription("For the previous day, adslAtucPerfPrev1DayUasL\nreports the number of seconds during which there\n\n\n\nwere unavailable seconds-line.")
adslAtucIntervalExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19))
if mibBuilder.loadTexts: adslAtucIntervalExtTable.setDescription("This table provides one row for each ATU-C\nperformance data collection interval for\nADSL physical interfaces whose\nIfEntries' ifType is equal to adsl(94).")
adslAtucIntervalExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1))
if mibBuilder.loadTexts: adslAtucIntervalExtEntry.setDescription("An entry in the\nadslAtucIntervalExtTable.")
adslAtucIntervalFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalFastR.setDescription("For the current interval, adslAtucIntervalFastR\nreports the current number of seconds during which\nthere have been fast retrains.")
adslAtucIntervalFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalFailedFastR.setDescription("For the each interval, adslAtucIntervalFailedFastR\nreports the number of seconds during which\nthere have been failed fast retrains.")
adslAtucIntervalSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalSesL.setDescription("For the each interval, adslAtucIntervalSesL\nreports the number of seconds during which\nthere have been severely errored seconds-line.")
adslAtucIntervalUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalUasL.setDescription("For the each interval, adslAtucIntervalUasL\nreports the number of seconds during which\nthere have been unavailable seconds-line.")
adslAturPerfDataExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20))
if mibBuilder.loadTexts: adslAturPerfDataExtTable.setDescription("This table contains ADSL physical line counters\nnot defined in the adslAturPerfDataTable\nfrom the ADSL-LINE-MIB [RFC2662].")
adslAturPerfDataExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1))
if mibBuilder.loadTexts: adslAturPerfDataExtEntry.setDescription("An entry extends the adslAturPerfDataEntry defined\nin [RFC2662].  Each entry corresponds to an ADSL\nline.")
adslAturPerfStatSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfStatSesL.setDescription("The value of this object reports the count of\nseverely errored second-line since the last agent\nreset.")
adslAturPerfStatUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfStatUasL.setDescription("The value of this object reports the count of\nunavailable seconds-line since the last agent\nreset.")
adslAturPerfCurr15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr15MinSesL.setDescription("For the current 15-minute interval,\nadslAturPerfCurr15MinSesL reports the current\nnumber of seconds during which there have been\nseverely errored seconds-line.")
adslAturPerfCurr15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr15MinUasL.setDescription("For the current 15-minute interval,\nadslAturPerfCurr15MinUasL reports the current\nnumber of seconds during which there have been\navailable seconds-line.")
adslAturPerfCurr1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 5), AdslPerfCurrDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr1DaySesL.setDescription("For the current day as measured by\nadslAturPerfCurr1DayTimeElapsed [RFC2662],\nadslAturPerfCurr1DaySesL reports the\nnumber of seconds during which there have been\nseverely errored seconds-line.")
adslAturPerfCurr1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 6), AdslPerfCurrDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr1DayUasL.setDescription("For the current day as measured by\nadslAturPerfCurr1DayTimeElapsed [RFC2662],\nadslAturPerfCurr1DayUasL reports the\nnumber of seconds during which there have been\nunavailable seconds-line.")
adslAturPerfPrev1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 7), AdslPerfPrevDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfPrev1DaySesL.setDescription("For the previous day, adslAturPerfPrev1DaySesL\nreports the number of seconds during which there\nwere severely errored seconds-line.")
adslAturPerfPrev1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 8), AdslPerfPrevDayCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfPrev1DayUasL.setDescription("For the previous day, adslAturPerfPrev1DayUasL\nreports the number of seconds during which there\nwere severely errored seconds-line.")
adslAturIntervalExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21))
if mibBuilder.loadTexts: adslAturIntervalExtTable.setDescription("This table provides one row for each ATU-R\nperformance data collection interval for\nADSL physical interfaces whose\nIfEntries' ifType is equal to adsl(94).")
adslAturIntervalExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1))
if mibBuilder.loadTexts: adslAturIntervalExtEntry.setDescription("An entry in the\nadslAturIntervalExtTable.")
adslAturIntervalSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturIntervalSesL.setDescription("For the each interval, adslAturIntervalSesL\nreports the number of seconds during which\nthere have been severely errored seconds-line.")
adslAturIntervalUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturIntervalUasL.setDescription("For the each interval, adslAturIntervalUasL\nreports the number of seconds during which\nthere have been unavailable seconds-line.")
adslConfProfileExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22))
if mibBuilder.loadTexts: adslConfProfileExtTable.setDescription("The adslConfProfileExtTable extends the ADSL line\nprofile configuration information in the\nadslLineConfProfileTable from the ADSL-LINE-MIB\n[RFC2662] by adding the ability to configure the\nADSL physical line mode.")
adslConfProfileExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1))
if mibBuilder.loadTexts: adslConfProfileExtEntry.setDescription("An entry extends the adslLineConfProfileEntry\ndefined in [RFC2662].  Each entry corresponds to an\nADSL line profile.")
adslConfProfileLineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,4,5,)).subtype(namedValues=NamedValues(("noChannel", 1), ("fastOnly", 2), ("interleavedOnly", 3), ("fastOrInterleaved", 4), ("fastAndInterleaved", 5), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslConfProfileLineType.setDescription("This object is used to configure the ADSL physical\nline mode.  It has following valid values:\n\nnoChannel(1), when no channels exist.\nfastOnly(2), when only fast channel exists.\ninterleavedOnly(3), when only interleaved channel\n    exist.\nfastOrInterleaved(4), when either fast or\n    interleaved channels can exist, but only one\n    at any time.\nfastAndInterleaved(5), when both the fast channel\n    and the interleaved channel exist.\n\nIn the case when no value has been set, the default\nValue is noChannel(1).")
adslAlarmConfProfileExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23))
if mibBuilder.loadTexts: adslAlarmConfProfileExtTable.setDescription("This table extends the\nadslLineAlarmConfProfileTable and provides\nthreshold parameters for all the counters defined\nin this MIB module.")
adslAlarmConfProfileExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1))
if mibBuilder.loadTexts: adslAlarmConfProfileExtEntry.setDescription("An entry extends the adslLineAlarmConfProfileTable\ndefined in [RFC2662].  Each entry corresponds to\nan ADSL alarm profile.")
adslAtucThreshold15MinFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAtucThreshold15MinFailedFastR.setDescription("The first time the value of the corresponding\ninstance of adslAtucPerfCurr15MinFailedFastR\nreaches or exceeds this value within a given\n15-minute performance data collection period,\nan adslAtucFailedFastRThreshTrap  notification\nwill be generated. The value '0' will disable\nthe notification. The default value of this\nobject is '0'.")
adslAtucThreshold15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAtucThreshold15MinSesL.setDescription("The first time the value of the corresponding\ninstance of adslAtucPerf15MinSesL reaches or\nexceeds this value within a given 15-minute\nperformance data collection period, an\nadslAtucSesLThreshTrap notification will be\ngenerated. The value '0' will disable the\nnotification.  The default value of this\nobject is '0'.")
adslAtucThreshold15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAtucThreshold15MinUasL.setDescription("The first time the value of the corresponding\ninstance of adslAtucPerf15MinUasL reaches or\nexceeds this value within a given 15-minute\nperformance data collection period, an\nadslAtucUasLThreshTrap notification will be\ngenerated. The value '0' will disable the\nnotification.  The default value of this\nobject is '0'.")
adslAturThreshold15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAturThreshold15MinSesL.setDescription("The first time the value of the corresponding\ninstance of adslAturPerf15MinSesL reaches or\nexceeds this value within a given 15-minute\nperformance data collection period, an\nadslAturSesLThreshTrap notification will be\ngenerated. The value '0' will disable the\nnotification.  The default value of this\nobject is '0'.")
adslAturThreshold15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAturThreshold15MinUasL.setDescription("The first time the value of the corresponding\ninstance of adslAturPerf15MinUasL reaches or\nexceeds this value within a given 15-minute\nperformance data collection period, an\n\n\n\nadslAturUasLThreshTrap notification will be\ngenerated. The value '0' will disable the\nnotification.  The default value of this\nobject is '0'.")
adslExtTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24))
adslExtAtucTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1))
adslExtAtucTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0))
adslExtAturTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2))
adslExtAturTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0))
adslExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2))
adslExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1))
adslExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 2))

# Augmentions
adslLineConfProfileEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslLineConfProfileEntry")
adslLineConfProfileEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslConfProfileExtEntry"))
adslConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
adslLineEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslLineEntry")
adslLineEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslLineExtEntry"))
adslLineExtEntry.setIndexNames(*adslLineEntry.getIndexNames())
adslAtucPerfDataEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAtucPerfDataEntry")
adslAtucPerfDataEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAtucPerfDataExtEntry"))
adslAtucPerfDataExtEntry.setIndexNames(*adslAtucPerfDataEntry.getIndexNames())
adslAturIntervalEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAturIntervalEntry")
adslAturIntervalEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAturIntervalExtEntry"))
adslAturIntervalExtEntry.setIndexNames(*adslAturIntervalEntry.getIndexNames())
adslAturPerfDataEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAturPerfDataEntry")
adslAturPerfDataEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAturPerfDataExtEntry"))
adslAturPerfDataExtEntry.setIndexNames(*adslAturPerfDataEntry.getIndexNames())
adslLineAlarmConfProfileEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslLineAlarmConfProfileEntry")
adslLineAlarmConfProfileEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAlarmConfProfileExtEntry"))
adslAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())
adslAtucIntervalEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAtucIntervalEntry")
adslAtucIntervalEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAtucIntervalExtEntry"))
adslAtucIntervalExtEntry.setIndexNames(*adslAtucIntervalEntry.getIndexNames())

# Notifications

adslAtucFailedFastRThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 1)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR"), ) )
if mibBuilder.loadTexts: adslAtucFailedFastRThreshTrap.setDescription("Failed Fast Retrains 15-minute threshold reached.")
adslAtucSesLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 2)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL"), ) )
if mibBuilder.loadTexts: adslAtucSesLThreshTrap.setDescription("Severely errored seconds-line 15-minute threshold\nreached.")
adslAtucUasLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 3)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL"), ) )
if mibBuilder.loadTexts: adslAtucUasLThreshTrap.setDescription("Unavailable seconds-line 15-minute threshold\nreached.")
adslAturSesLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 1)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL"), ) )
if mibBuilder.loadTexts: adslAturSesLThreshTrap.setDescription("Severely errored seconds-line 15-minute threshold\nreached.")
adslAturUasLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 2)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL"), ) )
if mibBuilder.loadTexts: adslAturUasLThreshTrap.setDescription("Unavailable seconds-line 15-minute threshold\nreached.")

# Groups

adslExtLineGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 1)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslLineConfProfileDualLite"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucConfig"), ("ADSL-LINE-EXT-MIB", "adslLineGlitePowerState"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucCap"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucActual"), ) )
if mibBuilder.loadTexts: adslExtLineGroup.setDescription("A collection of objects providing extended\nconfiguration information about an ADSL Line.")
adslExtAtucPhysPerfCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 2)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFastR"), ) )
if mibBuilder.loadTexts: adslExtAtucPhysPerfCounterGroup.setDescription("A collection of objects providing raw performance\ncounts on an ADSL Line (ATU-C end).")
adslExtAturPhysPerfCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 3)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAturPerfStatUasL"), ("ADSL-LINE-EXT-MIB", "adslAturIntervalUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfStatSesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAturIntervalSesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DayUasL"), ) )
if mibBuilder.loadTexts: adslExtAturPhysPerfCounterGroup.setDescription("A collection of objects providing raw performance\ncounts on an ADSL Line (ATU-C end).")
adslExtLineConfProfileControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 4)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslConfProfileLineType"), ) )
if mibBuilder.loadTexts: adslExtLineConfProfileControlGroup.setDescription("A collection of objects providing profile\ncontrol for the ADSL system.")
adslExtLineAlarmConfProfileGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 5)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinSesL"), ) )
if mibBuilder.loadTexts: adslExtLineAlarmConfProfileGroup.setDescription("A collection of objects providing alarm profile\ncontrol for the ADSL system.")
adslExtNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 6)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslAtucFailedFastRThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAturUasLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAturSesLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAtucSesLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAtucUasLThreshTrap"), ) )
if mibBuilder.loadTexts: adslExtNotificationsGroup.setDescription("The collection of ADSL extension notifications.")

# Compliances

adslExtLineMibAtucCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 2, 1)).setObjects(*(("ADSL-LINE-EXT-MIB", "adslExtAturPhysPerfCounterGroup"), ("ADSL-LINE-EXT-MIB", "adslExtLineConfProfileControlGroup"), ("ADSL-LINE-EXT-MIB", "adslExtLineAlarmConfProfileGroup"), ("ADSL-LINE-EXT-MIB", "adslExtAtucPhysPerfCounterGroup"), ("ADSL-LINE-EXT-MIB", "adslExtLineGroup"), ("ADSL-LINE-EXT-MIB", "adslExtNotificationsGroup"), ) )
if mibBuilder.loadTexts: adslExtLineMibAtucCompliance.setDescription("The compliance statement for SNMP entities which\nrepresent ADSL ATU-C interfaces.")

# Exports

# Module identity
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", PYSNMP_MODULE_ID=adslExtMIB)

# Types
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", AdslTransmissionModeType=AdslTransmissionModeType)

# Objects
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslExtMIB=adslExtMIB, adslExtMibObjects=adslExtMibObjects, adslLineExtTable=adslLineExtTable, adslLineExtEntry=adslLineExtEntry, adslLineTransAtucCap=adslLineTransAtucCap, adslLineTransAtucConfig=adslLineTransAtucConfig, adslLineTransAtucActual=adslLineTransAtucActual, adslLineGlitePowerState=adslLineGlitePowerState, adslLineConfProfileDualLite=adslLineConfProfileDualLite, adslAtucPerfDataExtTable=adslAtucPerfDataExtTable, adslAtucPerfDataExtEntry=adslAtucPerfDataExtEntry, adslAtucPerfStatFastR=adslAtucPerfStatFastR, adslAtucPerfStatFailedFastR=adslAtucPerfStatFailedFastR, adslAtucPerfStatSesL=adslAtucPerfStatSesL, adslAtucPerfStatUasL=adslAtucPerfStatUasL, adslAtucPerfCurr15MinFastR=adslAtucPerfCurr15MinFastR, adslAtucPerfCurr15MinFailedFastR=adslAtucPerfCurr15MinFailedFastR, adslAtucPerfCurr15MinSesL=adslAtucPerfCurr15MinSesL, adslAtucPerfCurr15MinUasL=adslAtucPerfCurr15MinUasL, adslAtucPerfCurr1DayFastR=adslAtucPerfCurr1DayFastR, adslAtucPerfCurr1DayFailedFastR=adslAtucPerfCurr1DayFailedFastR, adslAtucPerfCurr1DaySesL=adslAtucPerfCurr1DaySesL, adslAtucPerfCurr1DayUasL=adslAtucPerfCurr1DayUasL, adslAtucPerfPrev1DayFastR=adslAtucPerfPrev1DayFastR, adslAtucPerfPrev1DayFailedFastR=adslAtucPerfPrev1DayFailedFastR, adslAtucPerfPrev1DaySesL=adslAtucPerfPrev1DaySesL, adslAtucPerfPrev1DayUasL=adslAtucPerfPrev1DayUasL, adslAtucIntervalExtTable=adslAtucIntervalExtTable, adslAtucIntervalExtEntry=adslAtucIntervalExtEntry, adslAtucIntervalFastR=adslAtucIntervalFastR, adslAtucIntervalFailedFastR=adslAtucIntervalFailedFastR, adslAtucIntervalSesL=adslAtucIntervalSesL, adslAtucIntervalUasL=adslAtucIntervalUasL, adslAturPerfDataExtTable=adslAturPerfDataExtTable, adslAturPerfDataExtEntry=adslAturPerfDataExtEntry, adslAturPerfStatSesL=adslAturPerfStatSesL, adslAturPerfStatUasL=adslAturPerfStatUasL, adslAturPerfCurr15MinSesL=adslAturPerfCurr15MinSesL, adslAturPerfCurr15MinUasL=adslAturPerfCurr15MinUasL, adslAturPerfCurr1DaySesL=adslAturPerfCurr1DaySesL, adslAturPerfCurr1DayUasL=adslAturPerfCurr1DayUasL, adslAturPerfPrev1DaySesL=adslAturPerfPrev1DaySesL, adslAturPerfPrev1DayUasL=adslAturPerfPrev1DayUasL, adslAturIntervalExtTable=adslAturIntervalExtTable, adslAturIntervalExtEntry=adslAturIntervalExtEntry, adslAturIntervalSesL=adslAturIntervalSesL, adslAturIntervalUasL=adslAturIntervalUasL, adslConfProfileExtTable=adslConfProfileExtTable, adslConfProfileExtEntry=adslConfProfileExtEntry, adslConfProfileLineType=adslConfProfileLineType, adslAlarmConfProfileExtTable=adslAlarmConfProfileExtTable, adslAlarmConfProfileExtEntry=adslAlarmConfProfileExtEntry, adslAtucThreshold15MinFailedFastR=adslAtucThreshold15MinFailedFastR, adslAtucThreshold15MinSesL=adslAtucThreshold15MinSesL, adslAtucThreshold15MinUasL=adslAtucThreshold15MinUasL, adslAturThreshold15MinSesL=adslAturThreshold15MinSesL, adslAturThreshold15MinUasL=adslAturThreshold15MinUasL, adslExtTraps=adslExtTraps, adslExtAtucTraps=adslExtAtucTraps, adslExtAtucTrapsPrefix=adslExtAtucTrapsPrefix, adslExtAturTraps=adslExtAturTraps, adslExtAturTrapsPrefix=adslExtAturTrapsPrefix, adslExtConformance=adslExtConformance, adslExtGroups=adslExtGroups, adslExtCompliances=adslExtCompliances)

# Notifications
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslAtucFailedFastRThreshTrap=adslAtucFailedFastRThreshTrap, adslAtucSesLThreshTrap=adslAtucSesLThreshTrap, adslAtucUasLThreshTrap=adslAtucUasLThreshTrap, adslAturSesLThreshTrap=adslAturSesLThreshTrap, adslAturUasLThreshTrap=adslAturUasLThreshTrap)

# Groups
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslExtLineGroup=adslExtLineGroup, adslExtAtucPhysPerfCounterGroup=adslExtAtucPhysPerfCounterGroup, adslExtAturPhysPerfCounterGroup=adslExtAturPhysPerfCounterGroup, adslExtLineConfProfileControlGroup=adslExtLineConfProfileControlGroup, adslExtLineAlarmConfProfileGroup=adslExtLineAlarmConfProfileGroup, adslExtNotificationsGroup=adslExtNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslExtLineMibAtucCompliance=adslExtLineMibAtucCompliance)