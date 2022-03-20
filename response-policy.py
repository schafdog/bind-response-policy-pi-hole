# main.py
import urllib.request
commentChar = "#"
specialnets = ("127.0.0.1", "255.255.255.255", "::1", "f")
defaultRoute = "0.0.0.0"
blocklist = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
zoneHeader = """$TTL 2w
@ IN SOA localhost. root.localhost. (
       3   ; serial 
       2w  ; refresh 
       2w  ; retry 
       2w  ; expiry 
       2w) ; minimum 
    IN NS localhost."""
print(zoneHeader)

with urllib.request.urlopen(blocklist) as f:
 for bytes in f:
 
  line = bytes.decode("utf-8").strip()
  
  if (not line or line.startswith(commentChar) or line.startswith(specialnets)):
   continue

  list = line.split(commentChar)
  
  
  # ignore the ip address; extract the domain
  domain = list[0][8:]
  comment = ""
  if len(list) > 1:
   comment = "# " + list[1]
   
  if domain == defaultRoute:
   continue
  
  print(domain, " CNAME . ", comment, sep="")
  print("*.", domain, " CNAME .", sep="")
