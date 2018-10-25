import sys 

sw = sys.argv[1]

sw = float(sw)
    
if sw >= 220.0:
        
    print("Super Typhoon")

elif sw >= 118.0:
    print("Typhoon")

elif sw >= 117.0:
    print ("Severe Tropical Storm")

elif sw >= 88.0:
    print ("Tropical Storm")

else:
    print("Tropical Depression")

