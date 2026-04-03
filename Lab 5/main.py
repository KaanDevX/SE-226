def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

calc_abs_term = lambda x, i: (x ** (2 * i)) / factorial(2 * i)

def exp_x(x, n):
    total = 0
    for i in range(n):
        sign = (-1) ** i
        term = sign * calc_abs_term(x, i)
        total += term
    return total


variable = 0
def solve_gn(r,n):
    """
        Calculates Gn = 1 + r + r^2 + ... + r^n.

        Recursive Logic:
         Adds r^n to the global variable.
         calls itself with n-1 until n < 0.

        Sign Handling:
        If r is negative, the power (**) handles signs automatically.

    """
    global variable
    if n >= 0:
        variable += (r ** n)
        solve_gn(r, n - 1)

if __name__ == '__main__':
    x_girisi = float(input("Enter x: "))
    n_girisi = int(input("Enter n "))
    sonuc = exp_x(x_girisi, n_girisi)
    print(f"Result (S): {sonuc}")
    solve_gn(2,3)
    print("Sonuç:", variable)