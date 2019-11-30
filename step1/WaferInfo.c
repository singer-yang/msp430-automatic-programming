#include <stdio.h>
#include <msp430.h> 
#include "Debug/MSP430FR5xx_6xx/tlv.h"
#include "Debug/MSP430FR5xx_6xx/tlv.c"
#include <assert.h>

/**
 * hello.c
 */
int main(void)
{
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer
	PM5CTL0 &= ~LOCKLPM5;
	
	struct s_TLV_Die_Record * pDIEREC;
	unsigned char bDieRecord_bytes;
	TLV_getInfo(TLV_TAG_DIERECORD, 0, &bDieRecord_bytes, (unsigned int **)&pDIEREC);

	uint16_t typeinfo=TLV_getDeviceType();

	printf("Hello World!\n");
	printf("pDIEREC wafer id is %ld\n",pDIEREC->wafer_id);
	printf("pDIEREC die_x_position is %d\n",pDIEREC->die_x_position);
	printf("pDIEREC die_y_position is %d\n",pDIEREC->die_y_position);
	printf("pDIEREC test_results is %d\n",pDIEREC->test_results);
	
	return 0;
}
