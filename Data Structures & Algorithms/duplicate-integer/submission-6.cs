public class Solution {
    public bool hasDuplicate(int[] nums) {
        List<int> numDict = new List<int>(); 
        foreach (int x in nums)
        {            
            if (numDict.Contains(x))
                return true;
            numDict.Add(x);
        }
        return false;
    }
}