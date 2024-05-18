# Metasploit-script
This script demonstrates the usage of the Metasploit framework's RPC API to interact with a Metasploit instance and perform penetration testing tasks.

So the requirements for this project are:
- Python .x
- Metasploit framework
- 'metasploit' python package (pip install metasploit)

Usage: 
1. Start the Metasploit RPC service by running `msfrpcd -P your_password -S` in the command line. Replace `your_password` with your desired password.
2. Update the script with the appropriate values for the following variables:
   - `password`: The password used to authenticate with the Metasploit RPC service.
   - `exploit_name`: The name of the exploit module to use.
   - `target_ip`: The IP address of the target system.
   - `target_port`: The port number of the target system.
   - `payload_name`: The name of the payload to use.
3. Run the script: `python metasploit_script.py`.
4. View the console output to check if the exploit was successful.
5. Once finished, stop the Metasploit RPC service by running `msfrpcd --stop` in the command line.

I have only scripted this in one month, so feel free to tell me any improvements I can make on my email id: nalawaderudra1@gmail.com

For any collabs, reach out to me on email.
