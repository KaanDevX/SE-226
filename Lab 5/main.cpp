#include <iostream>
#include <cmath>

double solve_gn(int n, double r) {
    if (n == 0) {
        return 1;
    }
    return std::pow(r, n) + solve_gn(n - 1, r);
}

int main() {
    int n;
    double r;

    std::cout << "Enter n (power): ";
    std::cin >> n;
    std::cout << "Enter r (ratio): ";
    std::cin >> r;


    std::cout << "Result: " << solve_gn(n, r) << std::endl;

    return 0;
}