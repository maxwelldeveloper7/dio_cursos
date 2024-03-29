"""Implementa"""
import ipaddress

IP = "192.168.0.0/24"

rede = ipaddress.ip_network(IP, strict=False)

for ip in rede:
    print(ip)
