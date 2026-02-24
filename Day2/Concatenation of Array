int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int *ans=(int*)malloc((numsSize*2)*sizeof(int));
    for(int i=0;i<numsSize*2;i++)
    {
        ans[i]=nums[i%numsSize];
    }
    *returnSize=numsSize*2;
    return ans;
}
