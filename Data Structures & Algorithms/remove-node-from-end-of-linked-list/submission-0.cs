/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
       // int valRemove = RemoveIndex(head, n);
        int length = 0;
        ListNode currHead = head;
        while (currHead != null){
            currHead = currHead.next;
            length += 1; 
        }
        int target = length - n; 
        if (target == 0) return head.next;
        ListNode copy = head;
        for (int i = 0; i < target - 1; i++) {
            copy = copy.next;
        }
        copy.next = copy.next.next;
        return head; 
             
    }
}
