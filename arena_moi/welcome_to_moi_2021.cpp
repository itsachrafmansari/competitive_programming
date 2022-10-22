#include <iostream>
#include <vector>
using namespace std;

int main ()
{
    long int num_lines;
    cin >> num_lines;

    if (num_lines != 0) {

        std::vector<int> list;
        for (int i = 0; i < num_lines; ++i) {
            long int line;
            cin >> line;
            list.push_back(line);
        }

        for (std::vector<int>::iterator it = list.begin(); it != list.end(); ++it) {
            int a;
            if (*it % 3 == 0) {
                a = 0;
            } else {
                a = 1;
            }   
            long int r = *it / 3;
            std::cout << r + a << "\n\n";
        }

    }
    else {
        std::cout << 0 << "\n\n";
    }
    return 0;
}
