package SerializeAndDeserializeBST;

import util.TreeNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class Solution {
    public class Codec {

        // Encodes a tree to a single string.
        public String serialize(TreeNode root) {
            StringBuilder sb = new StringBuilder();
            ArrayList<TreeNode> cur = new ArrayList<>();
            cur.add(root);
            while(!cur.isEmpty()) {
                ArrayList<TreeNode> next = new ArrayList<>();
                for(TreeNode n: cur) {
                    if(sb.length() > 0)
                        sb.append(' ');
                    sb.append(n==null ? '#' : Integer.toString(n.val));
                    if(n == null)
                        continue;
                    next.add(n.left!=null ? n.left : null);
                    next.add(n.right!=null ? n.right : null);
                }
                cur = next;
            }
            //System.out.println(sb.toString());
            return sb.toString();
        }


        // Decodes your encoded data to tree.
        public TreeNode deserialize(String data) {

            if(data.isEmpty())
                return null;
            String[] values = data.split(" ");
            //System.out.println(Arrays.asList(values));
            if(values[0].equals("#"))
                return null;
            Deque<String> q = new LinkedList<>(Arrays.asList(values));
            TreeNode root = new TreeNode(Integer.valueOf(q.pollFirst()));
            ArrayList<TreeNode> cur = new ArrayList<>();
            cur.add(root);
            while(!q.isEmpty()) {
                ArrayList<TreeNode> next = new ArrayList<>();
                for(TreeNode n: cur) {
                    String head = q.pollFirst();
                    n.left = head.equals("#") ? null : new TreeNode(Integer.valueOf(head));
                    head = q.pollFirst();
                    n.right = head.equals("#") ? null : new TreeNode(Integer.valueOf(head));
                    if(n.left != null)
                        next.add(n.left);
                    if(n.right != null)
                        next.add(n.right);

                }
                cur = next;
            }
            return root;
        }
    }



}
