<script>
  import Sidebar1 from "../../components/sidebar/Sidebar1.svelte";
  import Header2 from "../../components/ui/headers/Header2.svelte";
</script>

<div
  class="flex flex-col bg-gradient-to-br from-gray-700 via-gray-700 to-gray-700 min-h-screen   text-white"
>
  <div class=" grid grid-cols-5">
    <div class="col-span-1 border-gray-600 border-r-2 h-screen">
      <Sidebar1 />
    </div>
    <div class="col-span-4">
      <Header2 />
      <div>
        <slot />
      </div>
    </div>
  </div>
</div>
