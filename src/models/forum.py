class Forum:
  def __init__(self, key, forumName, threadKeys):
    self.key        = key
    self.forumName  = forumName
    self.threadKeys = threadKeys

  def addThread(threadKey):
    if threadKey not in self.threadKeys:
      self.threadKeys.append(threadKey)

  def deleteByKey(key):
    if key in self.threadKeys:
      self.threadKeys.remove(key)

  def shouldDeleteSelf(key):
    return False
