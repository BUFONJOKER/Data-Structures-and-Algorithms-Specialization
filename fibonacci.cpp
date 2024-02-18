#include <iostream>
using namespace std;


unsigned long long int fibonacci(unsigned long long int n){

    unsigned long long int first = 0;
    unsigned long long int second = 1;
    unsigned long long int result;

    if(n<=1){
        return n;
    }

    else{
        for(unsigned long long int i = 2; i<=n;++i){
            result = first + second;
            first = second;
            second = result;
        }

        return result;
    }
    

}

int main(){
    unsigned long long int answer = fibonacci(100);
    cout<<answer<<"\n";
    return 0;
}