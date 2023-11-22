<template>
  <header>
    <div class="navMenu">
      <ul>
        <li><router-link to="/">Go to homepage</router-link></li>
        <li><router-link to="/createAd">Create new Ad</router-link></li>
        <li><router-link to="/adList">Show all Ads</router-link></li>
      </ul>
    </div>
  </header>

  <router-view />
</template>

<script>


</script>
<style lang="scss">
.navMenu {
  text-align: end;
  background-image: linear-gradient(to right, black 10%, gray 60%, aqua 90%, white);
}

ul {
  display: inline-block;
}

li {
  display: inline-block;
  background-color: bisque;
  border: 1px solid black;
  text-align: center;
  margin-left: 20px;
  border-radius: 20px;
  padding: 5px;
  box-shadow: 5px 5px 10px 0 black;
}
</style>
