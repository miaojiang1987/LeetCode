class TwoSum {
    private Map<Integer,Integer> map;
    /** Initialize your data structure here. */
    public TwoSum() {
         map=new HashMap<Integer,Integer>();
    }
    
    /** Add the number to an internal data structure.. */
    public void add(int number) {
        if (map.containsKey(number)){
            map.put(number,map.get(number)+1);
        }
        else{
            map.put(number,1);
        }
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    public boolean find(int value) {
        for (int key: map.keySet()){
            int complement=value-key;
            if (complement!=key){
                if(map.containsKey(complement)){
                    return true;
                }
            }
            else{
                if(map.get(key)>1) return true;
                
            }
        }
        return false;
    }
}
