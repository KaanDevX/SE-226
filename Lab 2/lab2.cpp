#include <iostream>

using namespace std;

int main() {
    //Task 1

    int num;
    int stepCount = 0;

    cout << "give bigger number than 9 ";
    cin >> num;

    if (num > 9) {
        cout << num;

        while (num > 9) {
            int currentSum = 0;
            int temp = num;

            while (temp > 0) {
                currentSum += temp % 10;
                temp /= 10;
            }

            num = currentSum;
            stepCount++;
            cout << " -> " << num;
        }

        cout << "\n Final value: " << num << endl;
        cout << "Total step: " << stepCount << endl;

    } else {
        cout << num << " is not bigger than 9" << endl;
    }


    //TASK 2
    int n;
    int fizzCount = 0;
    int buzzCount = 0;
    int fizzbuzzCount = 0;

    cout << "Enter an integer between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Invalid input. Enter a value between 10 and 100: ";
        cin >> n;
    }



    for (int i = 1; i <= n; i++) {
        if (i % 7 == 0) {
            cout << "("<< i << " is skipped" << ")" << endl;
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzzCount++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizzCount++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzzCount++;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "\n--- Summary ---" << endl;
    cout << "Fizz: " << fizzCount << endl;
    cout << "Buzz: " << buzzCount << endl;
    cout << "FizzBuzz: " << fizzbuzzCount << endl;


    //Task 3
    int num1;

    cout << "Enter a number between 3 and 9: ";
    cin >> num1;

    if (num1 < 3 || num1 > 9) {
        cout << "give valid input\n";
        return 0;
    }

    for (int i = 1; i <= 2 * num1 - 1; i++) {

        int k;
        if (i <= num1) {
            k = i;
        } else {
            k = 2 * num1 - i;
        }

        for (int j = 1; j <= k; j++) {
            cout << j << " ";
        }
        cout << "\n";
    }

    return 0;
}