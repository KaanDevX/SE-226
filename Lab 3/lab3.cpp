#include <iostream>

using namespace std;

void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}

int findMax(int* arr, int size) {
    if (size <= 0) return 0;

    int maxVal = *arr;
    for (int i = 1; i < size; ++i) {
        if (*(arr + i) > maxVal) {
            maxVal = *(arr + i);
        }
    }
    return maxVal;
}

void reverseArray(int* arr, int size) {
    int* start = arr;
    int* end = arr + size - 1;

    while (start < end) {
        swapValues(start, end);
        start++;
        end--;
    }
}

int* createArray(int size) {
    return new int[size];
}

void deleteArray(int* arr) {
    delete[] arr;
    cout << "Memory released successfully." << endl;
}

int main() {
    cout << "Creating dynamic array..." << endl;

    int size;
    cout << "Enter array size: ";
    cin >> size;

    int* myArray = createArray(size);

    cout << "Enter values: ";
    for (int i = 0; i < size; ++i) {
        cin >> *(myArray + i);
    }

    cout << "Array elements:" << endl;
    printArray(myArray, size);

    cout << "Maximum element: " << findMax(myArray, size) << endl;
    cout << "----------------------------------" << endl;
    cout << "Swapping two numbers" << endl;
    int a = 5;
    int b = 8;
    cout << "Before swap" << endl;
    cout << "a=" << a << endl;
    cout << "b=" << b << endl;

    swapValues(&a, &b);

    cout << "After swap" << endl;
    cout << "a=" << a << endl;
    cout << "b=" << b << endl;
    cout << "----------------------------------" << endl;

    cout << "Reversing array...." << endl;
    reverseArray(myArray, size);

    cout << "Array after reverseArray:" << endl;
    printArray(myArray, size);
    cout << "----------------------------------" << endl;

    cout << "Deleting array..." << endl;
    deleteArray(myArray);

    return 0;
}