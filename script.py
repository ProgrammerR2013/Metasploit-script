from metasploi.msfrpc import MsfRpcClient

# establish connection to the metasploit RPC service
client = MsfRpcClient(password="your_password")

# get a list of available modules
modules = client.modules.exploits

# print the names of the available exploits
for module in modules:
  print(module)

# select an exploit module
exploit = client.modules.use("exploit", "exploit-name")

# configure the necessary options for the exploit
exploit["RHOST"] = "target_ip"
explit["RHOST"] = "target_port"

# execute the exploit
exploit.execute(payload="payload_name")

# check if the exploit was successful
if exploit.success:
  print("Exploit successful")
else:
  print("Exploit failed")

# Once finished, stop the Metasploit RPC client
client.stop()
               
