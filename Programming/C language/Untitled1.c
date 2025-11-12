#include<stdio.h>

float temp(float cel, float fah);
int main(){

	float cel, fah, concel, confah;
	float getCelsius()
	{
		printf("Enter temp in Celsius: ");
		scanf("%f", &cel);
		printf("%f degree Celsius = %f degress Fahrenheit", cel, concel);
	}
	float getFah()
	{
		printf("Enter temp in Fahrenheit: ");
		scanf("%f", &fah);
		printf("%f degree Fahrenheit = %f degress Celsius", fah, confah);
	}
	return 0;
}

float temp(float cel, float fah){
	
	float celToFah()
	{
		float concel;
		concel = (9/5 * cel) + 32;
	}
	float FahToCel()
	{
		float confah;
		confah = (5/9 * fah) - 32;
	}
	
	return ;
	
}