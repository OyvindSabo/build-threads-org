from ...views.libs.frontLib.blockPost import blockPost

def apiThreadsBlockPosts():
  posts = [
    {
      'author': {
        'name': 'Øyvind',
        'profileLink': '/user/oyvindsabo'
      },
      'imageUrl': 'https://steemitimages.com/0x0/https://cdn.steemitimages.com/DQmXCfWZrZhW8oFqsFtWLLhHRCirP33TJugg2rVsGpWtm75/Steemit%20IMG_4572.jpg',
      'postUrl': '/forums/cars/oyvindsabo/',
      'title': 'This is a test post'
    },
    {
      'author': {
        'name': 'Øyvind',
        'profileLink': '/user/oyvindsabo'
      },
      'imageUrl': 'https://steemitimages.com/0x0/https://cdn.steemitimages.com/DQmXCfWZrZhW8oFqsFtWLLhHRCirP33TJugg2rVsGpWtm75/Steemit%20IMG_4572.jpg',
      'postUrl': '/forums/cars/oyvindsabo/',
      'title': 'This is a test post'
    }
  ]
  return list(map(lambda x: blockPost(x), posts))