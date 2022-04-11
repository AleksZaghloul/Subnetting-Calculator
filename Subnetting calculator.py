#Subnetting calculator
def how_many_bits(number):
    #finds the smallest number of bits needed for desired subnets
    count = 1
    while number > 2 :
        number = number/2
        count += 1
    if number == 1:
        return 0
    else:
        return count

def valid_number(num):
    try:
        return int(num) > 0
    except:
        print("Please type a positive number using digits")


cidr_dict = {8: "255.0.0.0",
            9: "255.128.0.0",
            10: "255.192.0.0",
            11: "255.224.0.0",
            12: "255.240.0.0",
            13: "255.248.0.0",
            14: "255.252.0.0",
            15: "255.254.0.0",
            16: "255.255.0.0",
            17: "255.255.128.0",
            18: "255.255.192.0",
            19: "255.255.224.0",
            20: "255.255.240.0",
            21: "255.255.248.0",
            22: "255.255.252.0",
            23: "255.255.254.0",
            24: "255.255.255.0",
            25: "255.255.255.128",
            26: "255.255.255.192",
            27: "255.255.255.224",
            28: "255.255.255.240",
            29: "255.255.255.248",
            30: "255.255.255.252",
            31: "255.255.255.254",
            }


calculator = True
class_collect = True


print("\n\n\n\n******Type q to quit******\n\n")


#Collect information about network class
while class_collect == True:   
    net_class = input("What is the network class youre working with? (A, B or C): ").lower()
    if net_class == "a":
        print("You have about 17 million hosts available in total and your default network mask is 255.0.0.0.")
        hosts = (2**24)
        cidr = 8
        class_collect = False
    elif net_class == "b":
        print("You have about 65 thousand hosts available in total and your default network mask is 255.255.0.0")
        hosts = (2**16) 
        cidr = 16
        class_collect = False
    elif net_class == "c":
        print("You have up to 256 hosts available in total and your default network mask is 255.255.255.0")
        hosts = (2**8)
        cidr = 24
        class_collect = False
    elif net_class == "q":
        class_collect = False
        calculator = False
    else:
        calculator = False
        print("No such class")
    

#calculator  
#collect information about subnets  and reserved hosts
while calculator == True:
    subnets = input("How many subnets do you need?: ")
    if subnets.lower() == "q":
        calculator = False
    elif valid_number(subnets):
        if int(subnets) > hosts/2:
           print("You can't have that many subnets in this class (remeber that some hosts will need to be reserved as well.")
        else:
            reserved = input("How many adresses are reserved per subnet? (Usually at least 2): ")
            if reserved.lower() == "q":
                calculator = False
            elif valid_number(reserved):
                bits_borrowed = how_many_bits(int(subnets))
                subnet_cidr = cidr + bits_borrowed
                host_per_net = int(hosts/(2**bits_borrowed)- int(reserved))
                if host_per_net < 1:
                    print("You will not have any hosts with this combination of subnets and reserved hosts.")
                else:
                    new_subnet_mask = cidr_dict[subnet_cidr]
                    print("Your new CIDR is " + str(subnet_cidr))
                    print("Your new subnet mask is " + new_subnet_mask)
                    print("You will have " + str(host_per_net) + " usable hosts per subnet")
                    print("Try another combination or press q. ")
            else:
                print("Not a valid input, please try again")










