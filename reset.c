#include <stdio.h>

int main(){
	FILE *fp;
	int values[6] = {0,0};
	fp = fopen("/dev/encoder-driver","w+");
	fwrite(values,1,1,fp);
	fclose(fp);
	return 0;
}





		
