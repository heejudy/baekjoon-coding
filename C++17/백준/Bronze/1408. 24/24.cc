#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	string a, b;
	int rh, rm, rs;
	cin >> a;
	cin >> b;

	int s1 = stoi(a.substr(6,2));
	int s2 = stoi(b.substr(6, 2));
	int m1 = stoi(a.substr(3, 2));
	int m2 = stoi(b.substr(3, 2));
	int h1 = stoi(a.substr(0, 2));
	int h2 = stoi(b.substr(0, 2));
	if (s1 > s2) {
		m2 = m2 - 1;
		rs = s2 + 60 - s1;
	}
	else
		rs = s2 - s1;
	if (m1 > m2) {
		h2 = h2 - 1;
		rm = m2 + 60 - m1;
	}
	else
		rm = m2 - m1;
	if (h1 > h2) {
		rh = h2 + 24 - h1;
	}
	else
		rh = h2 - h1;
	
	cout.width(2); cout.fill('0');
	cout << to_string(rh) << ":";
	cout.width(2); cout.fill('0');
	cout << to_string(rm) << ":";
	cout.width(2); cout.fill('0');
	cout << to_string(rs);
}