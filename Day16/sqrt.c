bool isPerfectSquare(int num) {
    int r=sqrt(num);
    if(r*r==num)
        return true;
    else
        return false;
}
