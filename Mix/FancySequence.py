"""Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
 

Example 1:

Input
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

Explanation
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20
"""
class Fancy:
  def __init__(self):
    self.MOD = 1_000_000_007
    # For each `val` in `vals`, it actually represents a * val + b.
    self.vals = []
    self.a = 1
    self.b = 0

  # To undo a * val + b and get the original value, we append (val - b) // a.
  # By Fermat's little theorem:
  #   a^(p - 1) ≡ 1 (mod p)
  #   a^(p - 2) ≡ a^(-1) (mod p)
  # So, (val - b) / a ≡ (val - b) * a^(p - 2) (mod p)
  def append(self, val: int) -> None:
    x = (val - self.b + self.MOD) % self.MOD
    self.vals.append(x * pow(self.a, self.MOD - 2, self.MOD))

  # If the value is a * val + b, then the value after adding by `inc` will be
  # a * val + b + inc. So, we adjust b to b + inc.
  def addAll(self, inc: int) -> None:
    self.b = (self.b + inc) % self.MOD

  # If the value is a * val + b, then the value after multiplying by `m` will
  # be a * m * val + b * m. So, we adjust a to a * m and b to b * m.
  def multAll(self, m: int) -> None:
    self.a = (self.a * m) % self.MOD
    self.b = (self.b * m) % self.MOD

  def getIndex(self, idx: int) -> int:
    return (-1 if idx >= len(self.vals)
            else (self.a * self.vals[idx] + self.b) % self.MOD)

S=Solution()
fancy = Fancy()
fancy.append(2)   # fancy sequence: [2]
fancy.addAll(3)   # fancy sequence: [2+3] -> [5]
fancy.append(7)   # fancy sequence: [5, 7]
fancy.multAll(2)  # fancy sequence: [5*2, 7*2] -> [10, 14]
print(fancy.getIndex(0)) # return 10
fancy.addAll(3)   # fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10)  # fancy sequence: [13, 17, 10]
fancy.multAll(2)  # fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
print(fancy.getIndex(0)) # return 26
print(fancy.getIndex(1)) # return 34
print(fancy.getIndex(2)) # return 20