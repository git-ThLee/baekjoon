#include <iostream>
#include <stdio.h>

int main()
{
	
	int a=0;
	int b=0;
	int max= -101;
	for (int i = 1; i <= 9; i++) {
		scanf("%d", &a);
		if (max < a) {
			max = a;
			b = i;
		}
	}
	printf("%d\n%d\n", max, b);
	return 0;
}