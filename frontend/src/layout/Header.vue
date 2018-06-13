<template>
  <div class="header">
    <!--
        TODO @kike
        Logo horizontal a la izquierda. Borde para limitar.
        A la izquierda del menu icono de notificaciones (Campanita) Muestra un dropdown con un listado. Ej: El atleta x ha publicado un post.
        - Home
        - Athletes
        - user email
          - Profile (Athlete profile)
          - Logout (Mostrar dialogo ¿Estás seguro de que quieres cerrar sesión?)
        -->
  </div>
</template>

<script>
export default {
  name: 'gb-header',
  data() {
    return {}
  },
  components: {}
}
</script>

<style lang="scss" scoped>
.header {
  padding: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  box-shadow: 0px 2px 10px 3px #ccc;
}
</style>
