import util._

import scala.annotation.tailrec

object `Count Complete Tree Nodes` {
    object Solution {
        val height = (root: TreeNode) => {
            var h = 0
            var cur = root
            while(cur != null) {
                h += 1
                cur = cur.left
            }
            h
        }

        def countNodes(root: TreeNode): Int = {
            // 2^n - 1 for an n-level tree
            if(root == null)
                return 0
            val l = height(root.left)
            val r = height(root.right)
            if(l == r) {
                (1 << l) + countNodes(root.right)
            }
            else {
                (1 << r) + countNodes(root.left)
            }
        }
    }
}
