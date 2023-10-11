N = int(input())
n = format(N, '010b')
print(n)

    #C言語の場合は
    ##include <stdio.h>
    
    #void main(){
    #    int N;
    #    scanf("%d", &N);
    #    int n[9];
    #    for(int i = 0; i <10; i++){
    #        n[i] = N % 2;
    #        N = N / 2;
    #    }
    #    for(int j = 0; j < 10; j++){
    #       printf("%d", n[j]);
    #    }
    #}