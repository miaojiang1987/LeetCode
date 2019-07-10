public int depthSumInverse(List<NestedInteger> nestedList) {
    if(nestedList==null||nestedList.size()==0)
        return 0;
 
    HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
 
    //two stacks: one is for processing nested integer, the other is for tracking layers. 
    Stack<NestedInteger> stack = new Stack<NestedInteger>();
    Stack<Integer> layers = new Stack<Integer>();
 
    //put all NestedIntegers to Stack and record its layer to be 1
    for(NestedInteger ni: nestedList){
        stack.push(ni);
        layers.push(1);
    }
 
    int maxLayer=Integer.MIN_VALUE;
 
    while(!stack.isEmpty()){
        NestedInteger top = stack.pop();
        int topLayer = layers.pop();
 
        maxLayer=Math.max(maxLayer, topLayer);
 
        if(top.isInteger()){
            if(map.containsKey(topLayer)){
                map.get(topLayer).add(top.getInteger());
            }else{
                ArrayList<Integer> list = new ArrayList<Integer>();
                list.add(top.getInteger());
                map.put(topLayer, list);
            }        
        }else{
            for(NestedInteger ni: top.getList()){
                stack.push(ni);
                layers.push(topLayer+1);
            }
        }
    }
 
    // calcualte sum
    int result=0;
    for(int i=maxLayer; i>=1; i--){
        if(map.get(i)!=null){
            for(int v: map.get(i)){
                result += v*(maxLayer-i+1);
            }
        }
    }
 
    return result;
}