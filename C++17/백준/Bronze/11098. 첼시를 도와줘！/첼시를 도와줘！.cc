#include <iostream>
#include <string>
#include <vector>
using namespace std; 

int main() {
	int n, p, a;
	string b;
	vector<string> total;
	cin >> n;
	for (int i = 0; i <n; i++)
	{
		vector<int> vec;
		vector<string> vec1;
		int count = 0;
		cin >> p;
		for (int j = 0; j < p; j++) {
			cin >> a;
			cin >> b;
			if (vec.empty()) {
				vec.push_back(a);
				vec1.push_back(b);
			}
			else {
				if (vec[0] < a) {
					vec.clear();
					vec1.clear();
					vec.push_back(a);
					vec1.push_back(b);
				}
			}
			count += 1;
		}
		total.push_back(vec1[0]);
	}
	for (int i = 0; i < total.size(); i++) {
		cout << total[i] << endl;
	}
}