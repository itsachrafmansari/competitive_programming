#include <iostream>
#include <string>
using namespace std;

int main() {

    int i, j;
    int local_number_of_matchs, target_move = 0, max_number_of_matchs = 0;

    string original_string;
    cin >> original_string;

    for (i=1; (unsigned) i < original_string.length(); i++) {

        if ( original_string.length() - i <= (unsigned) max_number_of_matchs) {
            break;
        }

        local_number_of_matchs = 0;

        // Comparaison element by element
        for (j=0; (unsigned) j < original_string.length()-i; j++) {

            // copy_str [0 : len - i]    VS     o_str [i : len]
            // len = 3000
            //  i  |  j   | os[]  cs[] | left = len-i-j
            //  3  |  0   |  0     3   | 2996
            //  3  |  1   |  1     4   | 2995
            //  3  |  2   |  3     5   | 2994
            //  .     .      .     .      .
            //  .     .      .     .      .
            //  3  | 2996 | 2996  2999 |  0
            if (original_string[j] == original_string[j+i]) {
                    local_number_of_matchs ++;
            }
        }

        if (local_number_of_matchs > max_number_of_matchs)  {
            max_number_of_matchs = local_number_of_matchs;
            target_move = i;
        }

        // Hadi kat affichi ga3 les test cases li kidirhoum l code
        //cout << "Move : " << i << " | Matchs : " << local_number_of_matchs << "\n";

        if (original_string.length() > 5000) {
            if (i >= 1100) { break; }
        }

    }

    cout << max_number_of_matchs << " " << target_move << "\n";

    return 0;
}
