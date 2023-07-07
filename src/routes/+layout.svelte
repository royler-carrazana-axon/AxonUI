<script>
	import { SvelteToast } from "@zerodevx/svelte-toast";
	import "../styles.css";
	import { browser } from "$app/environment";

	const components = [
		{
			name: "Introduction",
			path: "/",
		},
		{
			name: "Buttons",
			path: "/buttons",
		},
		{
			name: "Dividers",
			path: "/dividers",
		},
		{
			name: "Stats",
			path: "/stats",
		},
	];

	const oganisms = [
		{
			name: "Header",
			path: "/header",
		},
		{
			name: "Footer",
			path: "/fotter",
		},
	];

	const examples = [
		{
			name: "Dashboard 1",
			path: "/dashboard1",
		},
		{
			name: "Dashboard 2",
			path: "/dashboard2",
		},
		{
			name: "Dashboard 3",
			path: "/dashboard3",
		},
	];

	const options = {};

	let darkMode = true;

	function handleSwitchDarkMode() {
		darkMode = !darkMode;

		darkMode
			? document.documentElement.classList.add("dark")
			: document.documentElement.classList.remove("dark");
	}

	if (browser) {
		if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
			document.documentElement.classList.add("dark");
			darkMode = true;
		} else {
			document.documentElement.classList.remove("dark");
			darkMode = false;
		}
	}
</script>

<div>
	<div
		class="flex justify-between sticky top-0 from-gray-100 via-slate-200 to-slate-200 bg-gradient-to-bl px-32 shadow-gray-200 py-2 text-center"
	>
		<div class="">
			<a href="/" class="  text-gray-800 font-medium px-3 py-1"
				>Axon Web UI KIT</a
			>
		</div>
		<div class="  flex text-sm space-x-2 items-center p-2">
			<span>DarkMode</span>
			{#if !darkMode}
				<button on:click={handleSwitchDarkMode}>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-5 h-5 text-green-500"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M5.636 5.636a9 9 0 1012.728 0M12 3v9"
						/>
					</svg>
				</button>
			{/if}
			{#if darkMode}
				<button on:click={handleSwitchDarkMode}>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-5 h-5 text-red-500"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M5.636 5.636a9 9 0 1012.728 0M12 3v9"
						/>
					</svg>
				</button>
			{/if}
		</div>
	</div>
	<div class="flex justify-between px-20">
		<a href="https://github.com/royler-carrazana-axon/AxonUI">
			<div class="py-4 flex space-x-3 px-16 max-w-5xl mx-auto">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-6 h-6"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3"
					/>
				</svg>

				<span class="text-gray-500"
					>https://github.com/royler-carrazana-axon/AxonUI</span
				>
			</div></a
		>
	</div>
	<main class="py-3 flex flex-co px-14 max-w-5xl mx-auto">
		<aside
			class="flex-0 min-h-screen from-gray-50 via-slate-100 to-slate-100 bg-gradient-to-bl shadow-slate-100 p-2 w-1/4 shadow-lg rounded-xl p-4"
		>
			<div>
				<h2 class="subtitle">Atoms</h2>
				<hr class="py-3 my-1" />
				<div class="space-y-1 flex flex-col">
					{#each components as component}
						<a href={component.path}
							><button class="flex items-center space-x-2">
								<span
									class="text-sm hover:text-gray-800 hover:font-medium"
								>
									{component.name}
								</span>

								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-4 h-4 hover:translate-x-1"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
									/>
								</svg>
							</button></a
						>
					{/each}
				</div>
			</div>
			<div class="mt-7">
				<h2 class="subtitle">Organisms</h2>
				<hr class="py-3 my-1" />
				<div class="space-y-1 flex flex-col">
					{#each oganisms as organism}
						<a href={organism.path}
							><button class="flex items-center space-x-2">
								<span
									class="text-sm hover:text-gray-800 hover:font-medium"
								>
									{organism.name}
								</span>

								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-4 h-4 hover:translate-x-1"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
									/>
								</svg>
							</button></a
						>
					{/each}
				</div>
			</div>
			<div class="mt-7">
				<h2 class="subtitle">Examples</h2>
				<hr class="py-3 my-1" />
				<div class="space-y-1 min-h-screen flex flex-col">
					{#each examples as example}
						<a href={example.path}
							><button class="flex items-center space-x-2">
								<span
									class="text-sm hover:text-gray-800 hover:font-medium"
								>
									{example.name}
								</span>

								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-4 h-4 hover:translate-x-1"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
									/>
								</svg>
							</button></a
						>
					{/each}
				</div>
			</div>
		</aside>
		<div class="flex-1 border-gray-400">
			<slot />
		</div>
	</main>
	<SvelteToast {options} />
</div>
