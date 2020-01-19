package FirstBadVersion;

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1, end = n;
        while(start <= end) {
            if(end == start) {
                if(isBadVersion(end))
                    return end;
                else
                    return end + 1;
            }
            if(end == start + 1) {
                if(isBadVersion(start))
                    return start;
                if(isBadVersion(end))
                    return end;
                return end + 1;
            }
            int mid = start + (end-start) / 2;
            if(isBadVersion(mid))
                end = mid;
            else
                start = mid;
        }
        return -1;
    }
}

