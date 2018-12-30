class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int l = min(A, E), r = max(C, G);
        int d = min(B, F), u = max(D, H);
        
        long w1 = C - A, h1 = D - B;
        long w2 = G - E, h2 = H - F;
        
        long overlap = max(w1 + w2 - ((long)r - (long)l), 0L) * max(h1 + h2 - ((long)u - (long)d), 0L);
        cout << overlap << endl;
        return w1*h1 + w2*h2 - overlap;
    }
};
