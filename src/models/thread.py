class Thread:
  def __init__(self, key, author, forumName, postKeys, threadName):
    self.key        = key
    self.author     = author
    self.forumName  = forumName
    self.postKeys   = postKeys
    self.threadName = threadName

  def addPost(postKey):
    if postKey not in self.postKeys:
      self.postKeys.append(postKey)

  def deleteByKey(key):
    if key in self.postKeys:
      self.postKeys.remove(key)

  def shouldDeleteSelf(key):
    return key == self.key