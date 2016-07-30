class Solution {
public:
string longestPalindrome(string s) {
       
        size_t n = s.length();
        int startPos = 0;
        int max = 1;
        for (int i = 0; i < n; ++i)
        {
            int oddLen = 0, evenLen = 0, curLen;
            oddLen = Palindromic(s,i,i);
            
            if (i + 1 < n)
               evenLen = Palindromic(s,i,i+1);
            
            curLen = oddLen > evenLen? oddLen : evenLen;
            
            if (curLen > max)
            {
                max = curLen;
                if (max & 0x1)
                  startPos = i - max / 2;
                else 
                  startPos = i - (max - 1) / 2;
            }
        }
        
        return s.substr(startPos,max);
    }
    
    int Palindromic(const string &str, int i, int j)
    {
        size_t n = str.length();
        int curLen = 0;

        while (i >= 0 && j < n && str[i] == str[j])
        {
			--i;
            ++j;
        }
        curLen = (j-1) - (i+1) + 1;

        return curLen;
    }

};
