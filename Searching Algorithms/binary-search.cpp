#include <iostream>
using namespace std;
int main(){
    int n = 6;
    int arr[] = {10, 20, 30, 40, 50, 60};
    int key = 30;
    int left = 0;
    int right = n - 1;
    while(left <= right){
        int mid = (left + right)/2;
        if(arr[mid] == key){
            cout << "key found";
            return 0;
        }
        else if(arr[mid] > key){
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }
    cout << "Key not found";
}