#include <iostream>
#include <stdio.h>

int main()
{
	int N;
	int count = 0;
	int a[10] = { 0, };
	for (int i = 0; i < 10; i++) {
		scanf("%d", &N);
		a[i] = N % 42;
	}
	for (int i = 0; i < 10; i++) {
		for (int j = i+1; j < 10; j++) {
			if (a[i] == a[j]) {
				a[j] = 999;
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		if (a[i] != 999) {
			count++;
		}
	}
	printf("%d\n",count);

	return 0;
}