<script>
	import { fade } from 'svelte/transition';
	import { fly } from 'svelte/transition';

</script>

<button
in:fly={{ y: 50, duration: 2000 }} out:fade
  class=" rounded-3xl px-7 h-14 hover:bg-gray-900 bg-black text-white text-lg"
>
  Explore Destination
</button>
