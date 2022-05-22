#include <iostream>
#include <stdio.h>

int main()
{
	float M=-1; //최댓값
	int N; //과목 수
	float a[10000] = { 0, };
	float b;
	float c[10000] = { 0, };
	float sum = 0;
	

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%f", &b);
		if (M < b) {
			M = b;
		}
		c[i] = b;
	}
	for (int i = 0; i < N; i++) {
		a[i] = (c[i] / M) * 100;
		sum += (c[i] / M) * 100;
	}
	printf("%f\n", sum/N);
	return 0;
}