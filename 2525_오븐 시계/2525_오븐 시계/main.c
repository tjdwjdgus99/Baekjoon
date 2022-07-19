//
//  main.c
//  2525_오븐 시계
//
//  Created by 성정현 on 2022/07/05.
//

#include <stdio.h>

int main() {
    int A,B,C = 0;
    scanf("%d %d",&A,&B);
    scanf("%d",&C);
    B += C;
    while (B >= 60) {
        B -= 60;
        A += 1;
        while( A >= 24 ){
            A -= 24;
        }
    }
    printf("%d %d",A,B);
    
    return 0;
}
