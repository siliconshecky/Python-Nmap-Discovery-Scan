import nmap
import sys

nm = nmap.PortScanner() #set as the variable to use for port scanning input
ipAddrlist = open('ip-list.txt', 'r') #get the list of ip addresses or ranges from a text file
ipAddr = ' '.join(ipAddrlist) #convert the ip address/range list to a string value that can be imported into nmap
path='.'


nm.scan(hosts=ipAddr, arguments='-sn -T4 -PS') #runs the simple ping scan of addresses/ranges
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()] #creates and arrayof hosts and their status and state
for host,status in hosts_list: #pull the hostname and status one by one, check if it is considered "up" and if so put it in the output csv file with a carriage return at the end
	if status == 'up':
		#print('{0}:{1}'.format(host, status)) #for testing to see the output remove the # before print
		hostout= host + ',' + status
		with open(path + '/Net-Discovery-Scan-Results.csv', 'a') as output:
			output.write(hostout)
			output.write('\n')

ipAddrlist.close()
