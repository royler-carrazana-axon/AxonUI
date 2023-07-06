<script lang="ts">
	 
	import HeaderPage from "../../components/root/HeaderPage.svelte";
	import Component from "../../components/root/Component.svelte";
	import Button from "../../components/ui/buttons/Button.svelte";
	import IconButton from "../../components/ui/buttons/IconButton.svelte";
	import ChevronCircleUp from 'svelte-icons/fa/FaChevronCircleUp.svelte';
	const components = [
		{
			name: "Button Simple",
			keyName: "Button", 
			keyFolder: "buttons", 
			componentPreview: Button,
			patch: "/ui/buttons/Button.svelte",
			properties: {
				color: "string",
				title: "string",
			}
		},
		{
			name: "Button Simple with Image",
			keyName: "IconButton", 
			keyFolder: "buttons", 
			icon: ChevronCircleUp,
			componentPreview: IconButton,
			patch: "/ui/buttons/IconButton.svelte",
			properties: {
				color: "string",
				title: "string",
				icon: "SvelteIcon",
			}
		},
	];
</script>

<div>
	<HeaderPage title="Buttons" />
	<!-- Button Simple -->
	{#each components as component}
		<Component {...component} />
	{/each}
</div>
