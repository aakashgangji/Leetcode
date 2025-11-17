"""
Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

Implement the StreamChecker class:

StreamChecker(String[] words) Initializes the object with the strings array words.
boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.
 

Example 1:

Input
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist
"""
from typing import List
class Trie:  
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
  
    def insert(self, word: str) -> None:
        current_node = self
        for char in word[::-1]:
            index = ord(char) - ord('a')
            if current_node.children[index] is None:
                current_node.children[index] = Trie()
            current_node = current_node.children[index]
        current_node.is_end = True
  
    def search(self, characters: List[str]) -> bool:
        current_node = self
        for char in characters[::-1]:      
            index = ord(char) - ord('a')
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]
            if current_node.is_end:
                return True
        return False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.character_stream = []
        self.max_length = 201
        for word in words:
            self.trie.insert(word)
  
    def query(self, letter: str) -> bool:
        self.character_stream.append(letter)
        return self.trie.search(self.character_stream[-self.max_length:])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)