#!/bin/bash
FILE=/var/named/rpz-adblock
FILTERED=${FILE}.filtered
if iamactive.sh ; then
    ~/bin/response-policy.py > $FILE
    grep -v bbc /var/named/rpz-adblock |grep -v fundingchoicesmessages.google.com |grep -v redirectingat.com |grep -v googletagmanager > $FILTERED
    /usr/sbin/named-compilezone -f text -F raw -o /var/named/rpz-adblock.db "rpz-adblock" $FILTERED && rndc reload rpz-adblock
fi
