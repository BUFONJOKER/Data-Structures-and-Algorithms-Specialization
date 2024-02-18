#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::cin;
using std::cout;

long long max_pairwise_product(const vector<int>& numbers){
    long long result = 0;

    int n = numbers.size();

    for(int i = 0; i < n; ++i){
        
        for(int j = i + 1; j<n; ++j){

            if(((long long)numbers[i]) * numbers[j] > result){

                result = ((long long)numbers[i]) * numbers[j];
            }
        }
    }
    return result;
}

long long max_pairwise_product_fast(const vector<int>& numbers){
    
    int n = numbers.size();

    int max_index_1 = -1;

    for(int i = 0; i < n; ++i){
        
        if(max_index_1 == -1 || (numbers[i] > numbers[max_index_1])){
            max_index_1 = i;
        }
    }

    int max_index_2 = -1;

    for(int j = 0; j < n; ++j){

        if((j!=max_index_1) && (max_index_2 == -1 || (numbers[j] > numbers[max_index_2]))){
            max_index_2 = j;
        }
    }

    return ((long long)(numbers[max_index_1] * numbers[max_index_2]));
}

int main(){

    // stress test implementation
    while (true)
    {
        int n = rand() % 10 + 2;

        cout<< n << "\n";

        vector<int> a;

        for (int i = 0; i < n; ++i)
        {
            a.push_back(rand() % 10000);
        }

        for(int i = 0; i < n; ++i){
            cout<< a[i] << ' ';
        }

        cout << "\n";

        long long res_1 = max_pairwise_product(a);

        long long res_2 = max_pairwise_product_fast(a);

        if(res_1 != res_2){
            cout<<"Wrong answer " << res_1 << ' ' << res_2 << "\n";
            break;
        }

        else{
            cout<<"Ok\n";
        }
        
    }
    


    int n;
    
    cin >> n;

    vector<int> numbers(n);

    for (int i = 0; i<n; i++){
        cin >> numbers[i];
    }

    // long long result = max_pairwise_product(numbers);
    long long result = max_pairwise_product_fast(numbers);

    cout<< result << "\n";

    return 0;
}