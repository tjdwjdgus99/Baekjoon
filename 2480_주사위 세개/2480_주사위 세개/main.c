//
//  main.c
//  2480_주사위 세개
//
//  Created by 성정현 on 2022/07/06.
//

#include<stdio.h>

int main() {

    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int result = 0;

    if (a == b && b == c) {
        result = a * 1000 + 10000;
    }

    else if (a == b) {
        result = a * 100 + 1000;
    }
    else if (b == c) {
        result = b * 100 + 1000;
    }
    else if (c == a) {
        result = c * 100 + 1000;
    }
    else if (a != b && b != c) {
        if (a >= b && a >= c) {
            result = a * 100;
        }
        if (b >= c && b >= a) {
            result = b * 100;
            }

        if (c >= a && c >= b) {
            result = c * 100;
        }
    }

    printf("%d", result);
    return 0;
}
