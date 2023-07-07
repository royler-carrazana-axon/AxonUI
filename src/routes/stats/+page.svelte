<script lang="ts">
	import HeaderPage from "../../components/root/HeaderPage.svelte";
	import Component from "../../components/root/Component.svelte";
	import Divider from "../../components/ui/dividers/Divider.svelte";
	import StatSimple from "../../components/ui/stats/StatSimple.svelte";
	import StatsCustom from "../../components/ui/stats/StatsCustom.svelte";

	const components = [
		{
			active : true,
			name: "Stats Simple",
			cols: 1,
			keyName: "StatSimple",
			keyFolder: "stats",
			componentPreview: StatSimple,
			patch: "/ui/dividers/Divider.svelte",
			properties: {
				period: "string",
				modelValue: "number",
				modelName: "string",
			},
		},
		{
			active : false,
			name: "Stats Simple",
			cols: 1,
			px: 32,
			keyName: "StatSimple",
			keyFolder: "stats",
			componentPreview: StatsCustom,
			patch: "/ui/dividers/Divider.svelte",
			properties: {
				period: "string",
				modelValue: "number",
				modelName: "string",
			},
		},
	];
</script>

<div>
	<HeaderPage title="Stats" />
 
	

	{#each components as component}
		<Component {...component} />
	{/each}
</div>
