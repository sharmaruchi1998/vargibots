/*! 
 *
 * @author     e-Yantra Team
 * @date       2023/04/22
 *
 * \subsection Aim
 *  Write a program for Buzzer which is already present and interfaced on Atmega2560 Development Board
 *  to turn ON and OFF at an interval of a second.
 *
 * \subsection Connections
 * Buzzer 				:  PH2 				<br>
 *
 */

#define F_CPU 16000000UL            // Crystal Frequency of Atmega2560 

#include <avr/io.h>                 // Standard AVR IO Library
#include <util/delay.h>             // Standard AVR Delay Library

int main(void)
{
    DDRH=0XFF;                       // Initialize buzzer pin PH2 as output
    while(1)
    {
        PORTH = 0x00;                // Turn ON the buzzer
        _delay_ms(1000);
        PORTH = 0xFF;                // Turn OFF the buzzer 
        _delay_ms(1000);

    }
}