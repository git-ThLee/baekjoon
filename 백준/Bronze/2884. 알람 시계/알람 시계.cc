#include <iostream>
#include <stdio.h>

int main()
{
	int H, M;
	scanf("%d %d", &H, &M);
	if (M < 45) {
		
		if (H == 0) {
			H = 23;
		}
		else {
			H -= 1;
		}
		M = 60 - (45 - M);
	}
	else {
		M -= 45;
	}
	printf("%d %d \n", H, M);

	return 0;
}

