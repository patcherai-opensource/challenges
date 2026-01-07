#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char *flag = getenv("FLAG");
    if (flag != NULL) {
        puts(flag);
    } else {
        puts("actf{default_flag_placeholder}");
    }
    return 0;
}
