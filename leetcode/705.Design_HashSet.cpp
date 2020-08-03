class MyHashSet {
public:
    /** Initialize your data structure here. */
    int values[1000005];
    
    MyHashSet() {
        
        for (int i = 0; i < 1000005; ++i) values[i] = 0;
    }
    
    void add(int key) {
        values[key] = 1;
    }
    
    void remove(int key) {
        values[key] = 0;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return (values[key] == 1? true: false);
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
