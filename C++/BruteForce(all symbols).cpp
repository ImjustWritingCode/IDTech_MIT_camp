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
	for (i = -25; i < 26; i++)
	{
		for (j = 0; j < msg.length(); j++)
				cout << (char)(msg[j] + i);
		cout << endl;
	}
	cout << "Brute force finished, ";
	system("pause");
	return 0;
}