#include<stdio.h>
int main(){
    char name[20];
    float units,charge;
    printf("enter the custemer name\n");
    scanf("%s",name);
    printf("enter the number of units\n");
    scanf("%f",&units);
    if(units<=200)
    {
        charge= units*0.8+100;
    }
    if (units>200 && units<=300)
    {
      charge=260+(units-200)*0.9;

    }
    if(units>300)
    {
      charge=350+(units-300);

    }
    if(units>400)
    {
        charge=charge+charge*0.15;

    }
   printf("total chrge = %f",charge);
   return 0;
}

