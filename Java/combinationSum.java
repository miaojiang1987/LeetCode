class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if(candidates==null || candidates.length==0){
            return null;
        }
        
        List<List<Integer>> result=new ArrayList<>();
        List<Integer> temp=new ArrayList<Integer>();
        helper(candidates,temp,result,target,0,0);
        return result;
        
    }
    
    private void helper(int[] candidates,List<Integer> temp,List<List<Integer>> result,int target,int sum,int start){
        if (sum>target){
            return;
        }
        
        if (sum==target){
            result.add(new ArrayList<Integer>(temp));
        }
        
        else{
            for (int i=start;i<candidates.length;i++){
                temp.add(candidates[i]);
                helper(candidates,temp,result,target,sum+candidates[i],i);
                temp.remove(temp.size()-1);
            }
        }
    }
}