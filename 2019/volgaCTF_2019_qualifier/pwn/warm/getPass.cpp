#include <iostream>

int main(int argc, char *argv[])
{
    char pass[16];

    *pass = 'v';
    pass[1] = 0x4e ^ pass[0];
    pass[2] = 0x1e ^ pass[1];
    pass[3] = 0x15 ^ pass[2];
    pass[4] = 0x5e ^ pass[3];
    pass[5] = 0x1c ^ pass[4];
    pass[6] = 0x21 ^ pass[5];
    pass[7] = 1 ^ pass[6];
    pass[8] = 0x34 ^ pass[7];
    pass[9] = 7 ^ pass[8];
    pass[10] = 0x35 ^ pass[9];
    pass[0xb] = 0x11 ^ pass[10];
    pass[0xc] = 0x37 ^ pass[0xb];
    pass[0xd] = 0x3c ^ pass[0xc];
    pass[0xe] = 0x72 ^ pass[0xd];
    pass[0xf] = 0x47 ^ pass[0xe];
    
    for(int i = 0; i < 16; i++)
        putchar(pass[i]);
    
    return 0;
}