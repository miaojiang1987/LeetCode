class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int distance=words.length;
        int index_1=-1;
        int index_2=-1;
        
        for (int i=0;i<words.length;i++){
            if (word1.equals(words[i])) index_1=i;
            if (word2.equals(words[i])) index_2=i;
            if (index_1!=-1 && index_2!=-1){
              distance=Math.min(distance,Math.abs(index_1-index_2));
              //if (dist<distance) distance=dist;
            }
            
        }
        
        return distance;
    }
}