def func():
    print()
    c=10
    i=0
    while(i<=5):
        j=1
        while(j<=20):
            print(' ',end=' ')
            if(j>=10-i and j<=10+i):
                print('*',end=" ")
            else:
                print(' ',end=" ")
            j=j+1
        print('\n')
        i=i+1
func()



"""""

                                      *                                         

                                  *   *   *                                     

                              *   *   *   *   *                                 

                          *   *   *   *   *   *   *                             

                      *   *   *   *   *   *   *   *   *                         

                  *   *   *   *   *   *   *   *   *   *   *   
  """""
