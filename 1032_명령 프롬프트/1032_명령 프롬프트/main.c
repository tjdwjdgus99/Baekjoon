//
//  main.c
//  1032_명령 프롬프트
//
//  Created by 성정현 on 2022/07/08.
//

#include <stdio.h>
#include <string.h>
void priStr(char str[]);

int main(void) {
   char str[52][52], res[52];
   int i, j, n, length;
   
   scanf("%d", &n);
   while (getchar() != '\n'); //    버퍼 초기화
   for(i = 0; i < n; i++)
      fgets(str[i], 52, stdin); //  문자열 입력

   length = strlen(str[0]);

   for (i = 0; i < length; i++) {
      res[i] = str[0][i];

      for (j = 1; j < n; j++) {
         if (str[j-1][i] != str[j][i]) {
            res[i] = '?';
            break;
         }
      }
   }
   priStr(res);//   문자열 출력 함수
   return 0;
}

void priStr(char str[]) {
   int i = 0;
   while (str[i] != '\n')
      printf("%c", str[i++]);
   printf("\n");
}
