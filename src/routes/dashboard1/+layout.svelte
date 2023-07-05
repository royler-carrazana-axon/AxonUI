<script>
  import Header1 from "../../components/ui/headers/Header1.svelte";
</script>

<div class="flex flex-col bg-gradient-to-t from-gray-700 via-black to-black  min-h-screen pb-20 text-white">
  <div class=" max-w-6xl mx-auto">
    <Header1 />
    <slot />
  </div>
</div>
