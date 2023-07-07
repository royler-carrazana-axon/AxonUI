<script lang="ts">
	import HeaderPage from "../../components/root/HeaderPage.svelte";
	import Component from "../../components/root/Component.svelte";
	import Card1Image from "../../components/ui/cards/CardImage.svelte";
	import CardImage from "../../components/ui/cards/CardImage.svelte";
	import CardSimple from "../../components/ui/cards/CardSimple.svelte";

	const components = [
		{
			name: "Card Simple",
			cols: 2,
			keyName: "StatSimple",
			keyFolder: "stats",
			componentPreview: CardSimple,
			patch: "/ui/dividers/Divider.svelte",
			properties: {
				imageSrc: "string",
                link: "string",
			},
		},
		{
			name: "Card Simple with Image",
			cols: 1,
			keyName: "StatSimple",
			keyFolder: "stats",
			componentPreview: CardImage,
			patch: "/ui/dividers/Divider.svelte",
			properties: {
				imageSrc: "string",
				link: "string",
			},
		},
	];
</script>

<div>
	<HeaderPage title="Cards" />

	{#each components as component}
		<Component {...component} />
	{/each}
</div>
