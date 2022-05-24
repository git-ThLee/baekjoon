#include <iostream>
#include <stdio.h>

int main()
{
	
	int a, b, c;
	int d;
	int f;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	d = a * b * c;
	int arr[10] = { 0, };
	for (int i = 0; d > 0 ; i++) {
		f = d % 10;
		arr[f]++;
		d = d / 10;
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}
	

	return 0;
}