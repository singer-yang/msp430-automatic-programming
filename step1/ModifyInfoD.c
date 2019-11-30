#include <stdio.h>
#include <msp430.h> 


/**
 * hello.c
 * after testing, this program is successful
 */

#pragma RETAIN(jtag_lock)
#pragma location=0x1800
const unsigned long int jtag_lock = 0x1234;

int main(void)
{
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer
	PM5CTL0 &= ~LOCKLPM5;
	
	printf("Hello World!\n");
	
	void *ptr;
	ptr = (unsigned long int *) &jtag_lock;
	printf("address of ptr is 0x%p\n", ptr);
	printf("value of ptr address is %ld",*((unsigned long int *)ptr));

	return 0;
}
