#include<stdio.h>
#include<json-c/json.h>
void main() {
	printf("Hello World!\n");
	FILE *fp;
	char s;
	fp = fopen("good_api.json", "r");
	while((s=fgetc(fp))!=EOF) {
		printf("%c",s);
	}
	fclose(fp);
}
