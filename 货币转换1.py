M=input()
if M[0:3]in["RMB"]:
    USD=eval(M[3:])/6.78
    print("USD{:.2f}".format(USD))
if M[0:3]in["USD"]:
    RMB=eval(M[3:])*6.78
    print("RMB{:.2f}".format(RMB))
