#include "header/stdc++.h"
using namespace std;

int sumNumbers(int a, int b);

struct TrafficLight
{
    int flash;
    int on;
    int off;
};

class Vehicle{
private:
    
public:
    Vehicle();
    void SpeedStrength();
};

Vehicle::Vehicle(){}

void Vehicle::SpeedStrength(){

}




class Car : private Vehicle{
private:
    int modelNumber;
public:
     //constructor
     Car(int num);
};

Car::Car(int num){
    modelNumber = num;
    cout << modelNumber;
}


int main(int argc, char const *argv[])
{
    cout << "hello world" << endl;

    //one dimension
    vector<int> numbers = {1, 2, 3, 4};

    //one dimension array
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int nums[10];

    for(int i = 0; i < 10; i++){
       nums[i] = i;
    }

    for(auto y : nums){
        cout << y;
    }

    cout << endl;

    for(auto x : arr){
        cout << x;
    }

    cout << endl;

    for(int i = 0; i < numbers.size(); i++){
        cout << numbers[i];
    }

    cout << endl;

    int counter[] = {0, 2, 4, 6, 8};
    int index;
    do
    {
        index++;
        cout << counter[index];
    } while (index < 5);
    
    cout << endl;
    // int name;
    // cin >> name;
    // cout << name;
    int sum = sumNumbers(2, 4);
    cout << sum;

    cout << endl;

    TrafficLight traficLight;
    traficLight.flash = 5;
    traficLight.on = 1;
    traficLight.off = 0;

    cout << traficLight.flash << traficLight.on << traficLight.off;

    cout << endl;

    Car car(20);
    return 0;
}

int sumNumbers(int a, int b){
    return a + b;
}

