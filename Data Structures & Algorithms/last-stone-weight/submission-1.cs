public class Solution {
    public int LastStoneWeight(int[] stones) {
        PriorityQueue<int, int> pq = new PriorityQueue<int, int>();
   
        foreach (int stone in stones)
        {
            pq.Enqueue(stone, -stone);
        }
        while (pq.Count > 1)
        {
            int val1 = pq.Dequeue();
            int val2 = pq.Dequeue();
            int newVal = val1 - val2;
            if (newVal > 0)
                pq.Enqueue(newVal, -newVal);        
        }
        return pq.Count > 0 ? pq.Dequeue() : 0;
    }
}
