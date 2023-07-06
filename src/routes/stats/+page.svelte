<script lang="ts">
	import HeaderPage from "../../components/root/HeaderPage.svelte";
	import Component from "../../components/root/Component.svelte";
	import Divider from "../../components/ui/dividers/Divider.svelte";
	import StatSimple from "../../components/ui/stats/StatSimple.svelte";
	
    const components = [
		{
			name: "Stats Simple",
            cols: 1,
			keyName: "StatSimple",
			keyFolder: "stats",
			componentPreview: StatSimple,
			patch: "/ui/dividers/Divider.svelte",
			properties: {},
		},
	];
</script>

<div>
	<HeaderPage title="Stats" />
	<!-- Button Simple -->
	{#each components as component}
		<Component {...component}  />
	{/each}
</div>
