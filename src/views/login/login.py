from ..libs.frontLib.container import container
from ..libs.frontLib.loginForm import loginForm
from ..libs.frontLib.styles import styles

def renderLogin():
  return f"""
    {styles()}
    {container(loginForm())}
  """