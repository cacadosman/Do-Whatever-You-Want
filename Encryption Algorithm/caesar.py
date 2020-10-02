class Caesar:

  def __init__(self, key = 0):
    if not isinstance(key, int):
      raise Exception("Invalid key")
    self.key = key
    self.dictup = {}
    self.dictdown = {}
    self.pre()
  
  def pre(self):
    for i in range(26):
      self.dictup[chr(ord('a')+i)] = chr(ord('a')+(i+self.key)%26)
      self.dictup[chr(ord('A')+i)] = chr(ord('A')+(i+self.key)%26)
    for i in range(26):
      self.dictdown[chr(ord('a')+i)] = chr(ord('a')+(i-self.key)%26)
      self.dictdown[chr(ord('A')+i)] = chr(ord('A')+(i-self.key)%26)

  def encrypt(self, plain):
    cypher = "".join([self.dictup[p] if p in self.dictup else p for p in plain])
    return cypher 

  def decrypt(self, cypher):
    plain = "".join([self.dictdown[c] if c in self.dictdown else c for c in cypher])
    return plain
