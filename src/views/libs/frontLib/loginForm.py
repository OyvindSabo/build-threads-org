def loginForm():
  return f"""
    <div class='formContainer'>
      <form class='form'>
        <input type='text' name='username' placeholder='Username' class='formInput'>
        <br>
        <input type='password' name='privateKey' placeholder='Password' class='formInput'>
        <br>
        <input type='submit' value='Submit' class='submitButton'>
      </form>
    </div>
  """