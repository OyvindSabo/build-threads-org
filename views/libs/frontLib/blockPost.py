def blockPost(author, post):
  return f"""
    <div style='margin=5px'>
      <a href='{author.profileLink}>{author.name}</a>
      <img src='{post.imageUrl}'>
      <h2>
        <a href='{post.threadLink}'>{post.title}</a>
      </h2>
    </div>
  """