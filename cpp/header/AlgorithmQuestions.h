#include "header/stdc++.h"
#define arrLength 100
using namespace std;

class AlgorithmQuestions
{
private:
  
public:
    AlgorithmQuestions();
    vector<string> bigSort(vector<string> unsorted);
};


AlgorithmQuestions::AlgorithmQuestions(){}

/*
sorts a string array in order of ascending.
*/
vector<string> AlgorithmQuestions::bigSort(vector<string> unsorted){
       int arr[arrLength];
       vector<string> sorted;
       int size = unsorted.size();
       for(int i = 0; i<size; i++){
           arr[i] = stoi(unsorted[i]);
       } 
       sort(arr, arr + unsorted.size());
       for(int x = 0; x < unsorted.size(); x++){
           sorted.push_back(to_string(arr[x]));
       }
       return sorted;
}
