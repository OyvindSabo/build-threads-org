from ..libs.frontLib.blockPost import blockPost
from ..libs.frontLib.styles import styles
from ..libs.frontLib.container import container

def renderHome():
  post = {
    'author': {
      'name': 'Øyvind',
      'profileLink': '/user/oyvindsabo'
    },
    'imageUrl': 'https://steemitimages.com/0x0/https://cdn.steemitimages.com/DQmXCfWZrZhW8oFqsFtWLLhHRCirP33TJugg2rVsGpWtm75/Steemit%20IMG_4572.jpg',
    'postUrl': '/forums/cars/oyvindsabo/',
    'title': 'This is a test post'
  }
  
  return f"""
    {styles()}
    {container(
      f'{blockPost(post)}{blockPost(post)}'
    )}
  """