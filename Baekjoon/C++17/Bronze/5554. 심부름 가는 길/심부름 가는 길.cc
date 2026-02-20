#include <stdio.h>	

int main(void)
{
	int a, b, c, d;
	int res;
	scanf("%d %d %d %d", &a, &b, &c, &d);

	res = a + b + c + d;
	printf("%d\n", res / 60);
	printf("%d", res % 60);

	return 0;
}