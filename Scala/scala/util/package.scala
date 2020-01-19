package object util {
    class TreeNode(var _value: Int) {
        var value: Int = _value
        var left: TreeNode = null
        var right: TreeNode = null
    }

    class ListNode(var _x: Int = 0) {
        var next: ListNode = null
        var x: Int = _x
    }
}
