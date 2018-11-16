def blockPost(post):
  return f"""
    <center>
      <div class='blockPostContainer'>
        <a href='{post['author']['profileLink']}' class='userName'>{post['author']['name']}</a>
        <img src='{post['imageUrl']}' class='blockPostImage'>
        <h2>
          <a href='{post['postUrl']}' class='postTitle'>{post['title']}</a>
        </h2>
      </div>
    </center>
  """