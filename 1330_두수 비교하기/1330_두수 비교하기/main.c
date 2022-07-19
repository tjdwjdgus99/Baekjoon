//
//  main.c
//  1330_두수 비교하기
//
//  Created by 성정현 on 2022/07/11.
//

#include <stdio.h>

int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    if(a < b){
        printf("<");
    }else if (a > b){
        printf(">");
    }else{
        printf("==");
    }
    return 0;
}
