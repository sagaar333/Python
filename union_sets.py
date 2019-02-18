#WAP to find Union of both the sets(Means comman elements of l1 which are presnet in l2 should come only once)

def Unioun_Sets(l1,l2):
    l3=[]
    for i in range(0,len(l1)):
        while(l1[i] in l2):
            l2.remove(l1[i])
    l3.extend(l1)
    l3.extend(l2)
    return(l3)



def main():
    l1=eval(input("Enter values of first List :"))
    l2=eval(input("Enter values of 2nd List :"))
    print("Union of Both List's is =:",Unioun_Sets(l1,l2))


if __name__=='__main__':
    main()
