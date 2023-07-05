<script>
  import "../styles.css";
</script>

<div>
  <div
    class="bg-gray-500 shadow-2xl shadow-slate-500 py-2 text-center text-white"
  >
    <a href="/" class="bg-gray-900 text-gray-200 px-3 py-1 rounded-lg">Home</a>
  </div>
  <main>
    <slot />
  </main>
</div>
