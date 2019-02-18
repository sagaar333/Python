#WAP to find Symetric Difference of L1 & L2 means((L1-L2) Union(L2-L1))

import Difference_Lists
import union_sets

def Symetric_Difference(l1,l2):
    s1=Difference_Lists.Difference_Lists(l1,l2)
    s2=Difference_Lists.Difference_Lists(l2,l1)
    s3=union_sets.Unioun_Sets(s1,s2)
    return s3


def main():
    l1=eval(input("Enter values of first List :"))
    l2=eval(input("Enter values of 2nd List :"))
    print("Symetric Difference =:",Symetric_Difference(l1,l2))


if __name__=='__main__':
    main()
