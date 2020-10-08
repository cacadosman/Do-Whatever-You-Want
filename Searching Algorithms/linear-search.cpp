#include <iostream>
using namespace std;

bool isPresent(int *arr, int n, int element){
    for(int i = 0; i < n; i++){
        if(arr[i] == element){
            return true;
        }
    }
    return false;
}

int main(){
    int n; 
    cin >> n; // take input size of array
    int *arr = new int[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];   // taking input to an array       
    }
    int element;
    cin >> element; // Element which you want to search
    if(isPresent(arr, n, element)){
        cout << "Yes element is present";
    }
    else {
        cout << "Element is not present";
    }
}