<script lang="ts">
	import { fly } from 'svelte/transition';
  export let name: string = "Button";
</script>

<button
transition:fly={{ x: -15, duration: 1000 }}
  class=" flex   px-7 hover:bg-black hover:border-gray-500 hover:scale-105 rounded-2xl border-gray-300 text-gray-300 py-2"
>
  <slot />
  <span class="ml-3">
    {name}
  </span>
</button>
