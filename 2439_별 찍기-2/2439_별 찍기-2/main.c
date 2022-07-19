//
//  main.c
//  2439_별 찍기-2
//
//  Created by 성정현 on 2022/07/13.
//

#include <stdio.h>

int main() {
    int star;
    scanf("%d",&star);
    for (int i = 1; i < star + 1; i++) {
        for (int j = 0; j < star - i; j++) {
            printf(" ");
        }
        for (int k = 1; k < i + 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    
    
    return 0;
}
