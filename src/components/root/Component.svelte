<script lang="ts">
	import { toast } from "@zerodevx/svelte-toast";

	type PropertyType = {
		title?: string;
		icon?: string;
		iconPosition?: string;
		period?: string;
		modelValue?: string;
		modelName?: string;
	};

	export let keyFolder: string = "buttons";
	export let cols: number = 2;
	export let px: number = 2;
	export let keyName: string = "Button";
	export let name: string = "Button";
	export let componentPreview: any = null;
	export let patch: string = "";
	export let icon: any = null;
	export let properties: PropertyType = {
		title: "string",
		icon: "string",
		iconPosition: "string",
	};

	async function copyCode() {
		const contenidoHTML = await cargarContenidoHTML(keyFolder, keyName);
		if (contenidoHTML) {
			navigator.clipboard
				.writeText(contenidoHTML)
				.then(() => {
					toast.push("The code has been copied to the clipboard.");
				})
				.catch((error) => {
					console.error(
						`Error al copiar el código al portapapeles: ${error}`
					);
				});
		}
	}

	async function cargarContenidoHTML(carpeta: string, archivo: string) {
		const url = `../../${carpeta}/${archivo}.html`;
		try {
			const respuesta = await fetch(url);

			const contenidoHTML = await respuesta.text();
			return contenidoHTML;
		} catch (error) {
			console.error(`Error al cargar el contenido HTML: ${error}`);
			return null;
		}
	}
</script>

<div>
	<div class="flex flex-col p-7">
		<div class="w-full bg-slate-100 p-2 rounded-md flex justify-between">
			<h3 class="subtitle">{name}</h3>
			<div class="flex space-x-2 items-center">
				<span class="text-sm text-gray-400 pr-3">{patch}</span>
				<button
					on:click={() => copyCode()}
					class="bg-gray-200 text-gray-800 rounded-lg p-1"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-5 h-5 hover:scale-105 hover:rotate-90"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M16.5 8.25V6a2.25 2.25 0 00-2.25-2.25H6A2.25 2.25 0 003.75 6v8.25A2.25 2.25 0 006 16.5h2.25m8.25-8.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-7.5A2.25 2.25 0 018.25 18v-1.5m8.25-8.25h-6a2.25 2.25 0 00-2.25 2.25v6"
						/>
					</svg>
				</button>
			</div>
		</div>
		<div class={`grid grid-cols-${cols} bg-gray-50 p-3`}>
			<div class={`py-2 px-${px}`}>
				<svelte:component this={componentPreview} {icon} />
			</div>

			<div class="justify-start p-2 flex flex-col">
				<span class="subtitle">Properties</span>
				<hr class="my-2" />
				{#each Object.entries(properties) as [key, value]}
					<div>
						<span class="text-sm">
							{key}
						</span>
						<span class="text-sm text-gray-400">
							{value}
						</span>
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>
