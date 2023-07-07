<script>
	import { fade } from "svelte/transition";
	import { fly } from "svelte/transition";

	//Props
	export let title = "Button";
</script>

<button
	in:fly={{ y: 50, duration: 2000 }}
	out:fade
	class={`bg-primary text-primary btn-primary `}
>
	{title}
</button>
