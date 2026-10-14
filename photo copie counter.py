c=int(input("donner moi le nombre de photo copie "))
c1=10*0.10+((c-10)*0.09)
c2=(10*0.10)+(20*0.09)+((c-30)*0.08)
if c<=10:
    print("le prix est ",c*0.10)
elif c>10 and c<=30:
    print("le prix est ",c1)
elif c>30:
    print("le prix est ",c2)
