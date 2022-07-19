//
//  main.c
//  10872_팩토리얼
//
//  Created by 성정현 on 2022/07/08.
//

#include <stdio.h>

int factorall(int n){
    if (n < 1) {
        return 1;
    }
    else {
        return n*factorall(n-1);
    }
}

int main() {
    int number;
    scanf("%d",&number);
    printf("%d",factorall(number));
    return 0;
}
