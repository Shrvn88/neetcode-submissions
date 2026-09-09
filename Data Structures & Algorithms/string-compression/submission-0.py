class Solution:
    def compress(self, chars: List[str]) -> int:
        
        read = write = 0

        while read < len(chars):
            ch = chars[read]
            cnt = 0


            while read < len(chars) and chars[read] == ch:
                cnt += 1
                read += 1
            
            
            chars[write] = ch
            write += 1

            if cnt > 1:
                for d in str(cnt):
                    chars[write] = d
                    write += 1

        return write