//
//  main.c
//  2562_최댓값
//
//  Created by 성정현 on 2022/07/15.
//

#include <stdio.h>

int main() {
    char num[9];
    int Maxnum = 0;
    int count = 0;
    for (int i = 0; i < 9; i++) {
        scanf("%d",&num[i]);
        if (Maxnum < num[i]) {
            Maxnum = num[i];
            count = i;
        }
    }
    printf("%d\n%d",Maxnum,count + 1);
    
    
    return 0;
}
