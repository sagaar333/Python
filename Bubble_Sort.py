def BubbleSort(l1=[]):
    i=0
    
    for i in range(len(l1)-1):
        #print("value of i=",i)
        flag =0
        for j in range(len(l1)-i-1):
            #print("value of j = ",j)
            if l1[j]>l1[j+1]:
                flag=1
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
            #print("At j=",j,end='')
            #print(l1)
        if flag==0:
            print("breaking loop at ",i,j)
            break
    #print(l1)
    return l1


def main():
    l1=eval(input("Enter list to Sort :"))
    print("Sorted List = :",BubbleSort(l1))
    #BubbleSort(l1)

if __name__=='__main__':
    main()

            
