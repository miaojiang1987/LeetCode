class Solution {
    public int minCost(int[][] costs) {
        if (costs==null || costs.length==0){
            return 0;
        }
        
        int[] tmp=new int[3];
        for (int i=0;i<3;i++) tmp[i]=costs[0][i];
        
        for (int i=1;i<costs.length;i++){
            int tmp_0=Math.min(tmp[1],tmp[2])+costs[i][0];
            int tmp_1=Math.min(tmp[0],tmp[2])+costs[i][1];
            int tmp_2=Math.min(tmp[0],tmp[1])+costs[i][2];
            tmp[0]=tmp_0;
            tmp[1]=tmp_1;
            tmp[2]=tmp_2;
            
        }
        
        return Math.min(Math.min(tmp[0],tmp[1]),tmp[2]);
        
        
    }
}