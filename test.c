#include <stdio.h>

int main(){
	FILE *fp;
	int values[6] = {0,0,0,0};
	fp = fopen("/dev/encoder-driver","r");
        fread(values,sizeof(int),4,fp);
	printf("vals:%d,%d,%d,%d\n",values[0],values[1],values[2],values[3]);
	return 0;
}





		
