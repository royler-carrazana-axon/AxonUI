<script lang="ts">
	import { fade } from "svelte/transition";
	import { fly } from "svelte/transition";

	//Props
	export let color: string = "bg-black";
	export let title: string = "Button";
	export let icon: any = null;
	export let iconPosition: string = "left";
</script>

<button
	in:fly={{ y: 50, duration: 2000 }}
	out:fade
	class={` ${color}  rounded-3xl px-7  h-10 flex hover:${color}-900   text-white text-basew  justify-center  items-center`}
>
	<span
		class={`flex px-2 ${iconPosition === "left" ? "order-2" : "order-1"} `}
	>
		{title}
	</span>

	<span class="w-5 h-6 mx-auto pt-0.5">
		<svelte:component this={icon} />
	</span>
</button>
