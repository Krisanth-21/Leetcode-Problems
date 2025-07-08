/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode th1 = headA , th2 = headB;
        while (th1 != null){
            th2 = headB;
            while(th2 != null){
                if (th1 == th2){
                    return th1;
                }
                th2 = th2.next;
            }
            th1 = th1.next;
        }
        return null;
    }
}