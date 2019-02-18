#WAP to find L1- L2 differnece (Means remove elements from L1 which are present in L2)


def Difference_Lists(l1,l2):
    l3=[]
    for i in range(0,len(l1)):
        if l1[i]not in l2:
            l3.append(l1[i])
            
    return l3
        


def main():
    l1=eval(input("Enter values of first List :"))
    l2=eval(input("Enter values of 2nd List :"))
    print("Differnecr of L1 - L2 =:",Difference_Lists(l1,l2))


if __name__=='__main__':
    main()  
