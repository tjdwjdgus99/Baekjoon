//
//  main.c
//  2884_알람 시계
//
//  Created by 성정현 on 2022/07/12.
//

#include <stdio.h>

int main() {
    int hour,minute;
    scanf("%d %d",&hour,&minute);
    if(minute >= 45){
        minute = minute - 45;
        printf("%d %d",hour,minute);
    }else{
        minute = minute - 45 + 60;
        if(hour == 0){
            hour = 23;
        }else{
            hour -= 1;
        }
        printf("%d %d",hour,minute);
    }
    
    
    return 0;
}
