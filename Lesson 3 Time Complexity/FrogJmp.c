#include <math.h>
int solution(int X, int Y, int D) {
    return ceil((double) (Y-X) / D);
}