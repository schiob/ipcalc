__author__ = 'Francisco Ramos'
class IpCalc(object):

    res = []

    def __init__(self,input_network):
        ip_to_bin = lambda ip: ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
        if len(input_network.split("/")) == 2:
            self.netmask_cidr = input_network.split("/")[1]
            self.ip_str = input_network.split("/")[0]
        else:
            self.netmask_cidr = str(ip_to_bin(input_network.split(" ")[1]).find("0"))
            self.ip_str = input_network.split(" ")[0]
        self.ip_bin = ip_to_bin(self.ip_str)
        self.netmask_str = ""
        self.broadcast_str = ""
        self.network_str = ""
        self.ip_min_str = ""
        self.quantity_host = 0
        self.res = self.__calc()

    def __calc(self):
        bin_to_int = lambda bin_str: int(bin_str, base=2)
        bin_to_ip = lambda bin_str: str(int(bin_str[0:8],base=2))+"."+str(int(bin_str[8:16],base=2))+"."+str(int(bin_str[16:24],base=2))+"."+str(int(bin_str[24:32],base=2))
        broadcast_bin = ""
        netmask_bin = ""
        network_bin = ""
        for key in range(0,32):
            if key > int(self.netmask_cidr)-1:
                netmask_bin += "0"
                broadcast_bin += "1"
                network_bin += "0"

            else:
                netmask_bin += "1"
                network_bin += self.ip_bin[key]
                broadcast_bin += self.ip_bin[key]
        self.netmask_str = bin_to_ip(netmask_bin)
        self.broadcast_str = bin_to_ip(broadcast_bin)
        self.network_str = bin_to_ip(network_bin)
        self.ip_min_str = bin_to_ip(str(bin(bin_to_int(network_bin)+1))[2:])
        self.ip_max_str = bin_to_ip(str(bin(bin_to_int(broadcast_bin)-1))[2:])
        self.quantity_host = bin_to_int(broadcast_bin) - bin_to_int(network_bin)-1
        if self.quantity_host > 1000:
            return ["Many Hosts"]
        else:
            for key in range(bin_to_int(network_bin)+1,bin_to_int(broadcast_bin)):
                self.res.append(bin_to_ip(str(bin(key))[2:]))
            return self.res

if __name__ == "__main__":
    ips = IpCalc("192.168.1.34 255.255.255.240")
    print "\n\nIP", ips.ip_str
    print "Netmask", ips.netmask_str
    print "Network", ips.network_str
    print "Ip Minima", ips.ip_min_str
    print "Ip Maxima", ips.ip_max_str
    print "Broadcast", ips.broadcast_str
    print "Cantidad de Host", ips.quantity_host

    ips = IpCalc("192.168.1.34/22")
    print "\n\nIP", ips.ip_str
    print "Netmask", ips.netmask_str
    print "Network", ips.network_str
    print "Ip Minima", ips.ip_min_str
    print "Ip Maxima", ips.ip_max_str
    print "Broadcast", ips.broadcast_str
    print "Cantidad de Host", ips.quantity_host
