<script lang="ts">
	import HeaderPage from "../../components/root/HeaderPage.svelte";
	import Component from "../../components/root/Component.svelte";
	import Divider from "../../components/ui/dividers/Divider.svelte";
	const components = [
		{
			name: "Divider Simple",
			cols: 1,
			keyName: "Divider",
			keyFolder: "dividers",
			componentPreview: Divider,
			patch: "/ui/dividers/Divider.svelte",
			properties: {},
		},
	];
</script>

<div>
	<HeaderPage title="Dividers" />
	<!-- Button Simple -->
	{#each components as component}
		<Component {...component} />
	{/each}
</div>
