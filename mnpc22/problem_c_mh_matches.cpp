#include <iostream>
#include <string>
using namespace std;

int main() {

    int i, j, local_number_of_matchs, target_move = 0, max_number_of_matchs = 0;

    string original_string;

    cin >> original_string;

    // lmoves ki mchiw mn 1 [ i = 0 ] tal length dial Original_String [ i = original_string.length()-1 ]
    for (i=1; i < original_string.length(); i++) {

        if ( original_string.length()-i <= max_number_of_matchs ) {
            break;
        }

        local_number_of_matchs = 0;

        // f kol move STRING_COPY kit7aid mno akhir character

        // lcomparaison dial lcharacters ktbda mn akhir char f STRING_COPY w akhir char f ORIGINAL_STRING --> tal awl wa7ed f STRING_COPY
        for (j=original_string.length()-i-1; j >= 0; j--) {

            if (original_string[j+i] == original_string[j]) {
                    local_number_of_matchs ++;
            }

        }
        
        if (local_number_of_matchs > max_number_of_matchs)  {
            max_number_of_matchs = local_number_of_matchs;
            target_move = i;
        }

        // Hadi kat affichi ga3 les test cases li kidirhoum l code
        // cout << "Matchs : " << local_number_of_matchs << " | Move : " << i << " | Original Str : " << original_string << " | Str Copy :" << string_copy << "\n";

    }

    cout << max_number_of_matchs << " " << target_move << endl;

    return 0;
}
