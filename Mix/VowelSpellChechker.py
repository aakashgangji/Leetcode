"""
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
For a given query word, the spell checker handles two categories of spelling mistakes:
Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:
When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
Example 1:
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
Example 2:
Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]
"""
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels=set("aeiou")
        def mask(w):
            return "".join('*' if ch in vowels else ch for ch in w)
        
        exact=set(wordlist)
        lower_map,vowel_map={},{}
        for w in wordlist:
            lw=w.lower()
            if lw not in lower_map:
                lower_map[lw]=w
            mw=mask(lw)
            if mw not in vowel_map:
                vowel_map[mw]=w
        ans=[]
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lq=q.lower()
            if lq in lower_map:
                ans.append(lower_map[lq])
                continue
            mq=mask(lq)
            ans.append(vowel_map.get(mq,""))
        return ans

sol=Solution()
print(sol.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
print(sol.spellchecker(["yellow"], ["YellOw"]))
# Output: ["yellow"]