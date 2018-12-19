#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;
string encode(string str, string code)
{
	int i, j, num;
	int len = str.length();
	string cph="";
	for (i = 0; i < len; i++) {
		j = i % code.length();
		num = (int)code[j];
		if (num >= 'A'&&num <= 'Z')
			num -= 65;
		else
			num -= 97;
		if (str[i] <= 'Z'&&str[i] + num > 'Z')
			num -= 26;
		if (str[i] >= 'a'&&str[i] + num > 'z')
			num -= 26;
		cph += str[i] + num;
	}
	return cph;
}
string decode(string cph, string code)
{
	int i, j, num;
	int len = cph.length();
	string pln = "";
	for (i = 0; i < len; i++) {
		j = i % code.length();
		num = (int)code[j];
		if (num >= 'A'&&num <= 'Z')
			num -= 65;
		else
			num -= 97;
		if (cph[i] <= 'Z'&&cph[i] - num < 'A')
			num -= 26;
		if (cph[i] >= 'a'&&cph[i] - num < 'a')
			num -= 26;
		pln += cph[i] - num;
	}
	return pln;
}
int main(void)
{
	char ch;
	string str, code;
	cout << "Welcome to Vigenere cipher program" << endl << endl;
	while (1) {
		cout << "Please enter your text (type \"exit\" to exit) : ";
		cin >> str;
		if (str == "exit")
			exit(0);
		cout << "Encode (e) or decode (d) ? : ";
		cin >> ch;
		cout << "Please enter your code (shorter or equal plain text) : ";
		cin >> code;
		switch (ch) {
		case 'e':
		case 'E':
			str = encode(str, code);
			cout << "Below is the cipher text: " << endl;
			cout << str << endl << endl;
			break;
		case 'd':
		case 'D':
			str = decode(str, code);
			cout << "Below is the plain text: " << endl;
			cout << str << endl << endl;
			break;
		default:
			cout << "Error input" << endl;
		}
	}
	return 0;
}