#networking
import socket
import image_processing
import ipaddress
import pandas as pd
import numpy as np
import requests

def port_scanner(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.1)
	
	try:
		sock.connect((ip, port)) 
		return True
	except:
		#print (ip)
		return False

def main_Lan(ip0, ip1, password, chk_state):
	ip_0 = ipaddress.ip_address(ip0)
	ip_1 = ipaddress.ip_address(ip1)
	
	results =[]
	
	for ip_int in range(int(ip_0),int(ip_1)+1):
		ip = str(ipaddress.ip_address(ip_int))
		#print(ip)
		if port_scanner(ip, 554):
			temp_results = image_processing.process(password,ip,chk_state)	
			ip_0=+1
			results.append(temp_results)
		else:
			ip_0=+1	
	array=np.array(results)
	labels = ["IP", "Date", "Focus State"]
	report = pd.DataFrame(array, columns=labels)
	return report

def requests_to(x1,x2):
	values = {'Variance': x1, 'Noise': x2}
	r = requests.get('http://ec2-99-79-44-109.ca-central-1.compute.amazonaws.com:5000/api', json= values)
	json_response = r.json()
	return json_response['ESTIMATE']