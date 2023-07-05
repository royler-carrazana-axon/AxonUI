<script lang="ts">
	 
	import HeaderPage from "../../components/root/HeaderPage.svelte";
	import Component from "../../components/root/Component.svelte";
	import Button from "../../components/ui/buttons/Button.svelte";

	const components = [
		{
			name: "Button Simple",
			componentPreview: Button,
			patch: "/ui/buttons/Button.svelte",
			properties: {
				color: "string",
				title: "string",
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
	<!-- Button with Icon -->
	<!-- <div class="flex flex-col p-7">
		<div class="w-full bg-slate-100 p-2 rounded-md flex justify-between">
			<h3 class="subtitle">Button Simple with Icon</h3>
			<span class="text-sm text-gray-400 pr-3"
				>/ui/buttons/IconButton.svelte</span
			>
		</div>
		<div class="grid grid-cols-2 bg-gray-50">
			<div class="p-7">
				<IconButton icon="data" title="Data" iconPosition="right" />
			</div>

			<div class="justify-start p-2 flex flex-col">
				<span class="subtitle">Properties</span>
				<hr class="my-2" />
				<div>
					<span class="text-sm">color</span>
					<span class="text-sm text-gray-400">string</span>
				</div>
				<div>
					<span class="text-sm">title</span>
					<span class="text-sm text-gray-400">string</span>
				</div>
				<div>
					<span class="text-sm">icon</span>
					<span class="text-sm text-gray-400">string</span>
				</div>
				<div>
					<span class="text-sm">iconPosition</span>
					<span class="text-sm text-gray-400">left</span>
				</div>
			</div>
		</div>
	</div> -->
</div>
