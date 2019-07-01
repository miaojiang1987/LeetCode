class hashmap {
    class ListNode {
        int key;
        int value;
        ListNode next;
        public ListNode(int key, int value) {
            this.key = key;
            this.value = value;
        }
    } 
    List<ListNode> bucket;
    /** Initialize your data structure here. */
    public MyHashMap() {
        bucket = new ArrayList<ListNode>();
        for (int i = 0; i < 1000; i++) {
            bucket.add(new ListNode(0, 0));
        }
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        ListNode head = bucket.get(key % 1000);
        ListNode cur = head.next;
        ListNode prev = head;
        while (cur != null) {
            if (cur.key == key) {
                cur.value = value;
                return;
            }
            prev = cur;
            cur = cur.next;
        }
        prev.next = new ListNode(key, value);
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        ListNode head = bucket.get(key % 1000);
        ListNode cur = head.next;
        while (cur != null) {
            if (cur.key == key) {
                return cur.value;
            }
            cur = cur.next;
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        ListNode head = bucket.get(key % 1000);
        ListNode cur = head.next;
        ListNode prev = head;
        while (cur != null) {
            if (cur.key == key) {
                prev.next = cur.next;
                return;
            }
            prev = cur;
            cur = cur.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */