#include <iostream>

using namespace std;
int main() {

    int givenSecond;
    cout << "Give me seconds and I'll convert it to hours,minutes,seconds" << endl;

    cin >> givenSecond;

    int hour, minute , second;
    second = 1;
    minute = 60 * second;
    hour = minute * 60;

    hour = givenSecond / 3600;
    minute = (givenSecond % 3600) / 60;
    second = givenSecond % 60;
    cout << hour << " Hour " << minute << " Minute " << second << " Second" << endl;

    return 0;
}