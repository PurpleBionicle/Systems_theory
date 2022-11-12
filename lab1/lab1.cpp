#include <iostream>
#include <cmath>

double f_x(double &x) {
    double f = x * x * exp(sin(x));
    return f;
}

int main() {
    double a = 9, b = 14;// точки интервала
    double e = 0.1;//-интервал неопределнности
    double inaccuracy = e / 2; // погрешность
    double x, min_x, min_f;

    std::cout << "Стартовое значение интервала неопределенности=" << b - a << std::endl;

    /// опт пассивный поиск
    int N = 2 * (b - a) / e - 1;// находим количество точек
    std::cout << "Метод оптимального пассивного поиска для нахождения минимума" << std::endl;\
    std::cout << "N\t\tx\t\tf(x)" << std::endl;

    for (int i = 0; i <= N; ++i) {
        x = (b - a) / (N + 1) * i + a;
        double f = f_x(x);

        if (i == 0) {
            min_x = x;
            min_f = f;
        }
        if (f < min_f) {
            min_x = x;
            min_f = f;
        }
        std::cout << i << "\t\t" << x << "\t\t" << f << std::endl;
    }
    std::cout << "минимальное значение функции в точке  " << min_x << " +-"
              << inaccuracy << " равно " << min_f << std::endl;

    // дихотомия
    double d = 0.01;
    int j = 0; //счетчик числа итераций
    std::cout << "Дихотомия" << std::endl;
    std::cout << "N\t\tstart\t\tend\t\tlenght\t\tleft\t\tright\t\tf(left)\t\tf(right)" << std::endl;
    while (b - a > e) {
        ++j;
        double x1 = (a + b) / 2 - d;
        double x2 = (a + b) / 2 + d;

        std::cout << j << "\t  " << a << "\t\t " << b << "\t  "
                  << b - a << "\t\t" << x1 << "\t\t" << x2 << "\t\t"
                  << f_x(x1) << "\t\t" << f_x(x2) << std::endl;
        if (f_x(x1) >= f_x(x2)) { a = x1; }
        else { b = x2; }
    }
    double x_max_2 = (a + b) / 2;
    std::cout << "минимальное значение функции в точке  " << x_max_2 << " +-"
              << b - a << " равно " << f_x(x_max_2) << std::endl;
}
