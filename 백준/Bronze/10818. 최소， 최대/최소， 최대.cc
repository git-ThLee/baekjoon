#include <iostream>
#include <stdio.h>

int main()
{
	int T;
	int max = -1000001, min= 1000001;
	int a;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d", &a);
		if (max < a) {
			max = a;
		}
		if (min > a) {
			min = a;
		}
	}
	printf("%d %d\n", min, max);

	return 0;
}