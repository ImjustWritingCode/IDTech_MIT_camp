#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;
int main(void)
{
	string msg;
	int i, j;
	cout << "Please input message you want to crack: ";
	cin >> msg;
	cout << "Brute forcing..." << endl;
	for (i = 1; i < 26; i++)
	{
		for (j = 0; j < msg.length(); j++)
		{
			if (msg[j] >= 'A'&&msg[j] <= 'Z'&&msg[j] + i > 'Z')
				cout << (char)(msg[j] - 26 + i);
			else if (msg[j] >= 'a'&&msg[j] <= 'z'&&msg[j] + i > 'z')
				cout << (char)(msg[j] - 26 + i);
			else
				cout << (char)(msg[j] + i);
		}
		cout << endl;
	}
	cout << "Brute force finished, ";
	system("pause");
	return 0;
}