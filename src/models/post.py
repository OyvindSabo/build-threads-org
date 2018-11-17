class Post:
  def __init__(self, key, author, threadId, content):
    self.key       = key
    self.author    = author
    self.threadKey = threadKey
    self.content   = content

  def editContent(newContent):
    self.content = newContent

  def deleteByKey(key):
    pass

  def shouldDeleteSelf(key):
    return key == self.key or key == self.threadKey