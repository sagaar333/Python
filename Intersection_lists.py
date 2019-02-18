#WAP to find Intersection of L1 & L2(means comman in Both)
def Intersection_Sets(l1,l2):
    l3=[]
    for i in range(0,len(l1)):
        if l1[i] in l2:
            l3.append(l1[i])
    return l3
        


def main():
    l1=eval(input("Enter values of first List :"))
    l2=eval(input("Enter values of 2nd List :"))
    print("Intersection of Both List's is =:",Intersection_Sets(l1,l2))


if __name__=='__main__':
    main()    
