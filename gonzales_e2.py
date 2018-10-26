import sys 

sw = sys.argv[1]


sw = float(sw)
print("Your input: {}".format(sw)+" km/h")
    
if sw >= 220.0:
        
    print("There's a Super Typhoon")

elif sw >= 118.0:
    print("There's a Typhoon")

elif sw >= 117.0:
    print ("There's a Severe Tropical Storm")

elif sw >= 88.0:
    print ("There's a Tropical Storm")

else:
    print("There's a Tropical Depression")

