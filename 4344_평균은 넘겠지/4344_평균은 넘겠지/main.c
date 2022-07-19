//
//  main.c
//  4344_평균은 넘겠지
//
//  Created by 성정현 on 2022/07/17.
//

#include <stdio.h>

int main (void){
    int i , j ,k ;//    반복문
    int n;//    총 반복 횟수
    int a;//    학생수
    int q = 0; //   평균이 넘는 학생수
    int add = 0; // 총점
    int array[1001] = { 0 };    //학생들 점수
    double aver = 0;                //평균
    
    scanf("%d", &n);
    
    for(i = 0; i < n; i++){//   전체 반복 횟수
        scanf("%d", &a);
        q = 0;
        add = 0;
        for(j = 0; j < a; j++){
            scanf("%d", &array[j]);//   점수를 입력받기
            add += array[j];//  점수의 총합 구하기
        }
        aver = add / a; //  평균구하기
        for(k = 0; k < a; k++){
            if(array[k] > aver){//  평균 초과인원 선별
             q++;
            }
        }
        printf("%.3lf%\n" , ((double)q / (double)a)*100);
    }
    return 0;
}
