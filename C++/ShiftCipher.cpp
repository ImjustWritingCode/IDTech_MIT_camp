#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;
int main(void)
{
	string sen;
	int i, shf;
	while (1) {
		cout << "Please input a word: ";
		cin >> sen;
		if (sen == "exit")
			exit(0);
		cout << "Please input the shift value: ";
		cin >> shf;
		if (shf > 26)
			shf %= 26;
		for (i = 0; i < sen.length(); i++) {
			if (sen[i] > 'A'&&sen[i]<'Z') {
				if (sen[i] + shf > 'Z')
					sen[i] -= 26;
				if (sen[i] + shf < 'A')
					sen[i] += 26;
			}
			if (sen[i] > 'a'&&sen[i] < 'z') {
				if (sen[i] + shf > 'z')
					sen[i] -= 26;
				if (sen[i] + shf < 'a')
					sen[i] += 26;
			}
			sen[i] += shf;
		}
		cout << "The word shifted is:" << endl;
		cout << sen << endl;
	}
	return 0;
}