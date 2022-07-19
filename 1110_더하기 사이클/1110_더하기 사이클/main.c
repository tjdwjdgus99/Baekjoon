//
//  main.c
//  1110_더하기 사이클
//
//  Created by 성정현 on 2022/07/14.
//

#include <stdio.h>

int main() {
    int num,a,b,newnum,count,i;
    scanf("%d", &num);//    26
    
    if (num > 9) {
        a = num / 10;// 2
        b = num % 10;// 6
    }else{
        a = 0;
        b = num;
    }
    newnum = b * 10 + ((a + b)%10);//  68
    if(num == 0){
        count = 0;
    }else{
        count = 1;
    }
    i = 0;
    while (i != 1) {
        if (newnum > 9) {
            a = newnum / 10;//  6
            b = newnum % 10;//  8
        }else{
            a = 0;
            b = newnum;
        }
        count++;
        newnum = b * 10 + ((a + b)%10);//  84
        if (newnum == num) {
            break;
        }
    }
    printf("%d",count);
}
