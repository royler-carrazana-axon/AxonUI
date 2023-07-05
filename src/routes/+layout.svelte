<script>
	import "../styles.css";

	const components = [
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
</script>

<div>
	<div
		class="from-gray-100 via-slate-200 to-slate-200 bg-gradient-to-bl shadow-gray-200 py-2 text-center text-white"
	>
		<a href="/" class="  text-gray-400 px-3 py-1">Axon UI KIT</a>
	</div>
	<main class="py-14 flex px-14 max-w-5xl mx-auto">
		<aside
			class="flex-0 from-gray-50 via-slate-100 to-slate-100 bg-gradient-to-bl shadow-slate-100 p-2 w-1/4 shadow-lg rounded-xl p-4"
		>
			<div>
				<h2 class="text-gray-600">Atoms</h2>
				<hr class="py-3 my-1" />
				<div class="space-y-1 min-h-screen flex flex-col">
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
		</aside>
		<div class="flex-1 border-gray-400">
			<slot />
		</div>
	</main>
</div>
