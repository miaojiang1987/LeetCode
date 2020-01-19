package LowestCommonAncestorBST;

import javaUtil.TreeNode;

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || p == null || q == null)
            return null;
        TreeNode cur = root;
        while(cur != null) {
            if(cur.val < p.val && cur.val < q.val) {
                cur = cur.right;
            }
            else if(cur.val > p.val && cur.val > q.val) {
                cur = cur.left;
            }
            else
                break;
        }
        return cur;

    }
}
