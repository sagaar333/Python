
def ListSort(l1):
    for i in range(len(l1)-1):
        if(l1[i]>=l1[i+1]):
            return False
    return True

def main():
    if(ListSort([1,99,-99.0001])==1):
        print("Sorted")
    else:
        print("Not Sorted")

if __name__=='__main__':
    main()
