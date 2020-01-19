package ZigzagIterator;

import java.util.List;
class ZigzagIterator {

    List<Integer> v1;
    List<Integer> v2;
    int i1, i2;
    boolean f;
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        this.v1 = v1;
        this.v2 = v2;
        i1 = 0;
        i2 = 0;
        f = true;
    }

    public int next() {
        if(i1 < v1.size() && i2 < v2.size()) {
            f = !f;
            return (!f) ? v1.get(i1++) : v2.get(i2++);
        }
        else if(i1 < v1.size())
            return v1.get(i1++);
        else
            return v2.get(i2++);
    }

    public boolean hasNext() {
        return i1 < v1.size() || i2 < v2.size();
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */