import os
def total_size_dir(path):
    total=0
    for filename in os.listdir(path):
        total+=os.path.getsize(os.path.join(path,filename))
        #print(filename)

    return total
        



def main():
    path=eval(input(" Enter absolute path of dir to check total size :"))
    print(" Total size of Directory :",total_size_dir(path))

if __name__=='__main__':
    main()
