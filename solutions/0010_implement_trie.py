"""
LeetCode Problem 208: Implement Trie (Prefix Tree)
Difficulty: Medium
Focus: Trees/Prefixes

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and retrieve keys in a dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie 
  (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted 
  string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Time Complexity: 
- insert: O(L) where L is length of word
- search: O(L) where L is length of word
- startsWith: O(L) where L is length of prefix
Space Complexity: O(N * L) where N is number of words and L is average length
"""

class TrieNode:
    """Node in the Trie data structure."""
    def __init__(self):
        self.children = {}  # Map character to TrieNode
        self.is_end_of_word = False  # Marks end of a word

class Trie:
    """
    Trie (prefix tree) implementation.
    
    Each node represents a character and contains:
    - children: Dictionary mapping characters to child nodes
    - is_end_of_word: Boolean indicating if this node completes a word
    """
    
    def __init__(self):
        """Initialize empty trie with root node."""
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Args:
            word: String to insert
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """
        Search for a complete word in the trie.
        
        Args:
            word: String to search for
            
        Returns:
            True if word exists in trie, False otherwise
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """
        Check if any word in trie starts with given prefix.
        
        Args:
            prefix: Prefix to check
            
        Returns:
            True if any word starts with prefix, False otherwise
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Test cases
if __name__ == "__main__":
    # Test case from problem description
    trie = Trie()
    trie.insert("apple")
    print(f"search('apple'): {trie.search('apple')}")   # returns True
    print(f"search('app'): {trie.search('app')}")       # returns False
    print(f"startsWith('app'): {trie.startsWith('app')}") # returns True
    trie.insert("app")
    print(f"search('app'): {trie.search('app')}")       # returns True
    print()
    
    # Additional test cases
    trie2 = Trie()
    trie2.insert("hello")
    trie2.insert("world")
    trie2.insert("hell")
    
    print(f"search('hello'): {trie2.search('hello')}")  # True
    print(f"search('hell'): {trie2.search('hell')}")    # True
    print(f"search('hel'): {trie2.search('hel')}")      # False
    print(f"startsWith('hell'): {trie2.startsWith('hell')}")  # True
    print(f"startsWith('hea'): {trie2.startsWith('hea')}")  # False
    print(f"startsWith('wor'): {trie2.startsWith('wor')}")  # True