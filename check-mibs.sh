#!/usr/bin/env bash

MIBS="mibs"
INACTIVE="inactive"

for MIB in `grep import $MIBS/* | sed 's/.*importSymbols(//g' | cut -f1 -d, | sort -u | grep ^\" | sed 's/"//g'`; do
    if [[ $MIB != "ASN1" && $MIB != "ASN1-ENUMERATION" && $MIB != "ASN1-REFINEMENT" ]]; then
        if [[ -f $MIBS/$MIB.py ]]; then
            echo "Found required MIB $MIBS/$MIB.py"
        else
            echo "** Required MIB $MIBS/$MIB.py missing"
            if [[ -f $INACTIVE/$MIB.py ]]; then
                echo "** Try 'mv $INACTIVE/$MIB.py $MIBS/'"
            fi
        fi
    fi
done

