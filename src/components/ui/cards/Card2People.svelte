<script lang="ts">
	import { fly } from 'svelte/transition';

</script>
<div
transition:fly={{ x: -150, duration: 1000 }}
class="flex items-center mt-7 flex-col space-y-3">
  <img src="/profile1.jpg" class="w-16 h-16 rounded-full" alt="" />
  <h2 class="text-gray-100 text-base font-bold">Royler Marichal</h2>
</div>
