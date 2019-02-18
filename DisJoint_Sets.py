#WAP to find if L1 and L2 both sets are Disjoint(Means all the elements in both sets are Uncommon)

def DisJoint(l1,l2):
    flag=0
    for i in range(0, len(l1)):
        if l1[i] in l2:
            flag=1
    if flag==0:
        return True
    else:
        return False
    
            
        


def main():
    l1=eval(input("Enter values of first List :"))
    l2=eval(input("Enter values of 2nd List :"))
    a=DisJoint(l1,l2)
    if a:
        print("Both are DisJoint")
    else:
        print("Both are not DisJoint")
    


if __name__=='__main__':
    main()
