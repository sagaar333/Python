import Bubble_Sort
def mergeSort(l1,l2):
    l3=[]
    i=0
    j=0
    while(i<len(l1))&(j<len(l2)):
        if(l1[i]<l2[j]):
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1

    if(i<len(l1)):
        l3.extend(l1[i:])
    else:
        l3.extend(l2[j:])

    print(l3)

def main():
    l1=eval(input("Enter 1st List :"))
    l2=eval(input("Enter 2nd List :"))
    Bubble_Sort.BubbleSort(l1)
    Bubble_Sort.BubbleSort(l2)
    mergeSort(l1,l2)



if __name__=='__main__':
    main()
