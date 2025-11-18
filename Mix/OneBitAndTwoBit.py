"""
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1
    


"""This code defines a class Solution with a method isOneBitCharacter that determines if the last character in
a binary array can be decoded as a one-bit character. The method iterates through the array, checking each bit.
 If it encounters a 1, it skips the next bit (since 1 indicates a two-bit character). If it encounters a 0, it moves to the next bit (indicating a one-bit character). 
 The loop continues until it reaches the second-to-last bit. Finally, it checks if the index is at the last bit, returning True if so (indicating the last character is a one-bit character) and False otherwise.
"""

