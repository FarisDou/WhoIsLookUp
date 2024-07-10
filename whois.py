# Query and Response DB; IP/DN in a simple format. 1st step in recon. 
import socket

def whois_lookup(domain: str): # Socket 1 Address Family  Internet, Socket 2 Declares TCP socket type via stream.
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("whois.iana.org", 43)) #IANA and port, query and encode
  s.send(f"{domain}\r\n".encode()) 
  response = s.recv(4096).decode() # response variable to get info from whois server.
  s.close()
  return response

print(whois_lookup("linkedin.com"))
