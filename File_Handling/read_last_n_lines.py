# Python script to read a file and print it's last n lines
def read_last_n_lines_of_file(n):
    fd= open('C:\\Users\\Sagar M\\AppData\\Local\\Programs\\Python\\Python37\\LICENSE.txt')
    l=fd.readlines()
    no=len(l)
    start=no-n
    for i in range(start-1, no):
        print(l[i])
    
    
    



def main():
    n=int(input(" Enter no of lines to read from bottom"))
    read_last_n_lines_of_file(n)


if __name__=='__main__':
    main()
