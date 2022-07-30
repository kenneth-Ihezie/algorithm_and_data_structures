/*
#include "header/stdc++.h"
#define length 7
using namespace std;

template<class T>
T* pointerFunc(T a, T b){
    T* ptr;
    T c = (T) a + b;
    ptr = &c;
    return ptr;
}

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    vector<int> vec{9, 3, 6, 6, 3, 8, 0};
    int arr[length];
    for(int i = 0; i < length; i++){
        arr[i] = vec[i];
    }
    sort(arr, arr + length);
    for (auto x : arr)
    {
        cout << x << endl;
    }
    int* ptr;
    ptr = &arr[0];
    cout << *(ptr + 1) << endl;

    int parm = 45;
    int arg = 45;
    int* out = pointerFunc(parm, arg);
    cout << *out << endl;
}
*/

#include "header/AlgorithmQuestions.h"
using namespace std;

int main(){
   vector<string> unsorted = {"4", "9", "7", "1", "0"};
   AlgorithmQuestions algorithmQuestions;
   algorithmQuestions.bigSort(unsorted);
}

