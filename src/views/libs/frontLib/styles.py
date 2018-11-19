def styles():
  return """
    <style>
      body {
        background-color: #eeeeee;
        margin: 0px;
      }
      .container {
        width:100%;
        max-width:100vmin;
      }
      .blockPostContainer {
        background-color: #ffffff;
        text-align: left;
        max-width:100%;
        padding: 10px;
        margin:10px 0px;
      }
      .blockPostImage {
        width: 100%;
      }
      .formContainer {
        margin: 20vmin 0;
      }
      .form {
        font-family: Arial Black;
        font-size: 16px;
        color: #whi;
      }
      .formInput {
        font-family: Arial Black;
        background-color: White;
        border-radius: 5px;
        font-size: 16px;
        color: #444444;
        outline: none;
        padding: 10px;
        margin: 10px;
        border:none;
      }
      .postTitle {
        font-family: Arial Black;
        text-decoration: none;
        color: #444444;
      }
      .submitButton {
        background-color: DodgerBlue;
        font-family: Arial Black;
        border-radius: 5px;
        transition: 0.1s;
        font-size: 16px;
        cursor: pointer;
        padding: 10px;
        color: white;
        margin: 10px;
        border:none;
      }
      .submitButton:hover {
        background-color: LightSkyBlue;
        transition: 0.1s;
      }
      .userName {
        font-family: Arial Black;
        text-decoration: none;
        color: DodgerBlue;
      }
      .topNavigator {
        background-color: #ffffff;
        font-family: Arial Black;
        overflow: hidden;
      }
      .topNavigator a {
        text-decoration: none;
        padding: 14px 16px;
        text-align: center;
        font-size: 17px;
        color: #444444;
        float: left;
      }
      .topNavigator a:hover {
        background-color: #eee;
        color: black;
      }
      .topNavigator a.activeButton {
        background-color: DodgerBlue;
        color: white;
      }
      .topNavigatorRight {
        float: right;
      }
    </style>
  """