class Solution {
public:
    int n;
    int dp[101];
    int solve(vector<int>&nums , int idx)
    {
        if(idx>=n) return 0;

        if(dp[idx] != -1) return dp[idx];

        int take=nums[idx]+solve(nums,idx+2);
        int skip=solve(nums,idx+1);

        return dp[idx]=max(take,skip);
    }
    int rob(vector<int>& nums) {
        
        n=nums.size();
        
        if(n==1) return nums[0];
        
        memset(dp,-1,sizeof(dp));

        return solve(nums,0);
        
        // return max(dp[n-1] ,dp[n-2]);
    }
};