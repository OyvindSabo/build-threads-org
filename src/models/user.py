class User:

  def __init__(self, key, profilePictureUrl, signatureHash, threadIds, username):
    self.key               = key
    self.profilePictureUrl = profilePictureUrl
    self.signatureHash     = signatureHash
    self.threadIds         = threadIds
    self.username          = username

  def editProfilePicture(newProfilePictureUrl):
    self.profilePictureUrl = newProfilePictureUrl

  def deleteByKey(key):
    pass

  def shouldDeleteSelf(key):
    return False