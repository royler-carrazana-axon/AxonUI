<script lang="ts">
	import { fade } from "svelte/transition";
	import { fly } from "svelte/transition";

	//Props
	export let title: string = "Button";
	export let icon: any = null;
	export let iconPosition: string = "left";
</script>

<button
	in:fly={{ y: 50, duration: 2000 }}
	out:fade
	class={`bg-primary text-primary btn-primary flex items-center`}
>
	<span
		class={`flex px-2 ${iconPosition === "left" ? "order-2" : "order-1"} `}
	>
		{title}
	</span>

	<span class="w-5 h-6 mx-auto pt-0.5">
		<svelte:component this={icon}  />
	</span>
</button>
