from mod_exp import fast_exp
p=17 #prime
g=3 #primitive root of 17
 
def send_key(private_number):
    pub_key = fast_exp(g,private_number,p)
    return pub_key
def key_real(private_number,received_key):
    key_real = fast_exp(received_key,private_number,p)
    return key_real

print("Hi Alice ! enter your secret number\n")
x=int(input())
snet_number=send_key(x)
print(snet_number," has been sent to Bob")
y=int(input("What number did you receive from Bob ? \n"))
real_key=key_real(x,y)
print("The key that you all will be using is: ",real_key)

