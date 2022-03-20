#!/bin/bash
~/bin/response-policy.py > /var/named/rpz-adblock
named-compilezone -f text -F raw -o /var/named/rpz-adblock.db "rpz-adblock" /var/named/rpz-adblock
rndc reload rpz-adblock
