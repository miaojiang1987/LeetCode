class Solution {
    public int depthSum(List<NestedInteger> nestedList) {
        int sum=0;
        LinkedList<NestedInteger> queue=new LinkedList<NestedInteger>();
        LinkedList<Integer> depth=new LinkedList<Integer>();
        
        for(NestedInteger ni: nestedList){
            queue.offer(ni);
            depth.offer(1);
        }
        
        while (!queue.isEmpty()){
            NestedInteger top=queue.poll();
            int dep=depth.poll();
            if (top.isInteger()){
                sum+=dep*top.getInteger();
            }
            else{
                for(NestedInteger ni: top.getList()){
                    queue.offer(ni);
                    depth.offer(dep+1);
                }
            }
            
        }
        
        return sum;
    }
}