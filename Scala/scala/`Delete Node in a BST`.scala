import util.TreeNode

object `Delete Node in a BST` {
    object Solution {
        def deleteNode(root: TreeNode, key: Int): TreeNode = {
            //println("root=", root._value, "key=", key)
            if(root == null)
                return null
            if(key < root._value) {
                root.left = deleteNode(root.left, key)
                return root
            }
            if(key > root._value) {
                root.right = deleteNode(root.right, key)
                return root
            }
            if(root.right == null)
                return root.left
            var cur = root.right
            while(cur.left != null) {
                cur = cur.left
            }
            val nextVal = cur._value
            //println("next", nextVal)
            root.value = nextVal
            root.right = deleteNode(root.right, nextVal)
            root
        }
    }

}
