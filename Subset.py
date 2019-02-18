# WAP to find if L2 is Subset of L1, means all elements of L2 are presnet in L1
def Subset(l1,l2):
    p=1
    for i in range(0,len(l2)):
        if l2[i] not in l1:
            p=0

    if p ==1:
        print("Yes")
    else:
        print("No")


def main():
    l1=eval(input("Enter values of first List :"))
    l2=eval(input("Enter values of 2nd List :"))
    Subset(l1,l2)


if __name__=='__main__':
    main()
