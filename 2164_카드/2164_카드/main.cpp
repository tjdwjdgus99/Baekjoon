//
//  main.cpp
//  2164_카드
//
//  Created by 성정현 on 2022/07/19.
//

#include <iostream>
#include <algorithm>
#include<utility>
#include <queue>

using namespace std;

int main() {
    queue <int>q;// 선입선출 뒤에서 추가하면 앞에서 삭제하는 터널형 형태로 바꿔줌
    int num;//  카드 갯수
    cin>>num;
    
    for(int i=1; i < num + 1; i++){
        q.push(i);//    1 ~ 카드 최대 갯수 까지 차래로 채우기
    }
    if (num == 1) {
        cout << 1;
    }else{
        for (int j = 0; j < num - 2; j++) {
            q.pop();//  제일 윗 수를 삭제함
            q.push(q.front());//    다음수를 복사해서 아래로 가져가고
            q.pop();//  복사했던 원본 수를 삭제함
        }
        q.pop();
        cout << q.front();
    }
    return 0;
}
