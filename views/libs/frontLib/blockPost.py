def blockPost(post):
  return f"""
    <div class='blockPostContainer'>
      <img src='{post['imageUrl']}' class='blockPostImage'>
      <h2>
        <a href='{post['postUrl']}' class='postTitle'>{post['title']}</a>
      </h2>
      <a href='{post['author']['profileLink']}' class='userName'>{post['author']['name']}</a>
    </div>
  """