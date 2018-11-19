from ..libs.frontLib.blockPost    import blockPost
from ..libs.frontLib.container    import container
from ..libs.frontLib.styles       import styles
from ..libs.frontLib.topNavigator import topNavigator

def renderHome():
  return """
    <script>
      const url = 'localhost:5000';

      window.onload = () => fetch(`http://${url}/api/threads/blockposts`).then(response => {
        let threads = response.json();
        threads.then(threads => {
          console.log('threads: ', threads);
          document.getElementById('container').innerHTML = threads.join('');
        });
      });
    </script>""" + f"""
    {styles()}
    {topNavigator()}
    {container()}
  """