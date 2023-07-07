<script>
	import { fly } from "svelte/transition";
</script>

<div>
	<hr
		in:fly={{ y: 500, duration: 3000 }}
		class="px-3 h-0.5 bg-gray-800/50 mx-7 dark:invert"
	/>
</div>
