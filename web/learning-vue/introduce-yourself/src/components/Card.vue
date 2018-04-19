<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">{{ text }}</p>
      <p class="card-text">
        <small class="text-muted">
          {{ footer }}
        </small>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'text', 'footer']
}
</script>
