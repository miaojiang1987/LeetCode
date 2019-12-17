import util.TreeNode

object `Kth Smallest Element in a BST` {
    import scala.collection.mutable.ArrayBuffer

    object Solution {
        def kthSmallest(root: TreeNode, k: Int): Int = {
            val inorder = new ArrayBuffer[TreeNode]()
            traverse(root, inorder, k)
            return inorder(k-1).value
        }
        def traverse(root: TreeNode, inorder: ArrayBuffer[TreeNode], k: Int): Unit = {
            if(root == null || inorder.size >= k)
                return
            traverse(root.left, inorder, k)
            inorder.append(root)
            traverse(root.right, inorder, k)
        }
    }
}
