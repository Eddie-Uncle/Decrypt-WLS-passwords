# Decrypt or Encrypting WebLogic passwords
Decrypt or Encrypt WLS Passwords

Copy the $WLS_DOMAIN_HOME/security folder to another location! Copy the boot.properties of your domain as well. (Usually is encrypted, and from inside this folder location you might run the commands below: 

         Decrypt
	 /opt/oracle/Middleware/Oracle_Home/wlserver/common/bin/wlst.sh wlsdecrypt.py boot.properties
	 
	 Encrypt
	 /opt/oracle/Middleware/Oracle_Home/wlserver/common/bin/wlst.sh wlsencrypt.py boot.properties
   
You have the WebLogic password clear for you!!   
