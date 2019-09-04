class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
          map<int,int> hashmap;
          for (auto interval:intervals){
              hashmap[interval[0]]++;
              hashmap[interval[1]]--;
          }
          int room=0; 
          int max_rooms=0;
          for (auto value:hashmap){
              room+=value.second;
              max_rooms=max(room,max_rooms);
          }
        
          return max_rooms;
       }          
    
};