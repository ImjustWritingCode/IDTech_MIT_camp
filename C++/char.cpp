#include<iostream>
using namespace std;
int main(void)
{
	char ch;
	cout << "Please input a character: ";
	cin >> ch;
	cout << "The ASCII code of " << ch << " is " << (int)ch << endl;
	return 0;
}