
// local verible is related only that specific function.
//globle veriable is related all function in that program.
#include <stdio.h>
int e=8;//global veriable
int add()
{
    int a=2,b=5; //local variable
    return a+b;
}
int main() {
    int c=4,d=5 //local variable
    print("%d",c+d);

    return 0;
}