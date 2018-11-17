from flask import current_app

from ..models.forum  import Forum
from ..models.post   import Post
from ..models.thread import Thread
from ..models.user   import User

def deleteObjectByKey(key)
  for obj in current_app:
    obj.deleteByKey(key)
    if obj.shouldDeleteSelf:
      current_app.remove(obj)