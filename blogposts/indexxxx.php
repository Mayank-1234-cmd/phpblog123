
  <style>@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
  * {
    font-weight:100px;
    font-family: 'Roboto', sans-serif;
  }
  img {
    width:100%;
  }
  hr {
    width:100%;
  }
  .p {
    font-size:10px;
    display: inline-block;
    display: inline;
  }
  span {
    display:inline;
  }</style>
  <h3><i>a site<span class="p">hello world <a href="update.php">update</a></span></h3></i>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
  <?php
  require '../dev/pd.php';
  $Parsedown = new Parsedown();
  echo $Parsedown->text('hgisd'); 
  