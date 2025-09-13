#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main() {
	int a, b;
	int total = 0;
	vector<int> mini;
	cin >> a;
	cin >> b;
	
	for (a; a <= b; a++) {
		if (sqrt(a) == int(sqrt(a))) {
			mini.push_back(a);
			total += a;
		}
	}
	if (mini.empty() == true) {
		cout << -1;
	}
	else {
		cout << total << endl;
		cout << mini[0];
	}	
}