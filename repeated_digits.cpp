#include <iostream>
using namespace std;

int main() {

	int N;
	cin >> N;
	
	int digit;
	int delta = 0;
  
	while (N > 0) {
	    cin >> digit;
	    delta ^= digit;
	    N--;
	}

	cout << delta;

  return 0;

}
