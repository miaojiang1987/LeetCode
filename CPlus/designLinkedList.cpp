class MyLinkedList {

private:
    struct node{
        int val;
        node *next;
    }; 
    
    node *head;
    node *tail;
    int size;
    
    
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        head=nullptr;
        tail=nullptr;
        size=0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index>=size || index<0) return -1;
        node* cur=head;
        for (int i=0;i<index;i++){
            cur=cur->next;
        }
        
        return cur->val;
        
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        node *temp = new node();
        temp->val = val;
        temp->next = head;
        head = temp;
        if(size==0) tail = temp;
        ++size;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        node *temp=new Node();
        temp->val=val;
        if (size==0){
            tail = temp;
            head = temp;
        }
        tail->next=temp;
        tail=temp;
        size++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > size)
            return;
        
        if (index == 0) {
            addAtHead(val);
            return;
        }
        if (index == size) {
            addAtTail(val);
            return;
        }
        node *p = head;
        for (int i = 0; i < index-1; i++) {
            p = p->next;
        }
        node *q = new node();
        q->val=val;
        q->next = p->next;
        p->next = q;
        size++;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
                if (index >= size)
            return;
        
        node *p = head;
        if (index == 0) {
            head = head->next;
            delete p;
            size--;
            return;
        }

        for (int i = 0; i < index-1; i++) {
            p = p->next;
        }
        node *q = p->next;
        p->next = q->next;
        if (tail == q) tail = p;
        delete q;
        size--;
    }
};