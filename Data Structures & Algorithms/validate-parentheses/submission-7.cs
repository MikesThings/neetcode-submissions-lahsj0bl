public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();
        Dictionary<char, char> bookends = new Dictionary<char, char> {
            {'{', '}'}, {'(', ')'}, {'[', ']'}
        };
        foreach (char e in s) {
            if (e == '(' || e == '{' || e == '[') {
                stack.Push(e);
            }
            else if (e == ')' || e == '}' || e == ']') {       
                if (stack.Count() <= 0) {
                    return false;
                }         
                char x = stack.Pop();
                if (bookends[x] != e) {
                    return false;
                }
            }
        }
        return stack.Count() <= 0;   
    }
}
