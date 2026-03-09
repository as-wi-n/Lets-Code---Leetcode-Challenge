bool checkPerfectNumber(int num) {
    int limit=sqrt(num);
    int s=0,q=0;
    if(num==1)
        return false;
    for(int i=1;i<=limit;i++)
    {
        if((num%i)==0)
        {
            s+=i;
            if(num/i!=num)
                q=num/i;
            s+=q;
        }
    }
    if(s==num)
    {
        return true;
    }
    else
    {
        return false;
    }
}
