<script>
	import { fade, fly } from "svelte/transition";
</script>

<div>
	<div
		in:fly={{ y: 50, duration: 3000 }}
		out:fade
		class="bg-primary-clean bg-opacity-80 rounded-2xl p-4"
	>
		<div class="flex justify-between">
			<h2 class="text-primary-in-clean text-xl font-medium">
				Bounce Rate
			</h2>
			<button
				class="bg-primary-dark rounded-full p-2 hover:rotate-12 hover-center h-9 w-9"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-6 h-5 text-primary"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"
					/>
				</svg>
			</button>
		</div>
		<div class="justify-around px-7 mt-3 flex hover-center">
			<button
				class="border-2 border-gray-500 p-4 rounded-2xl flex flex-col text-primary-in-clean text-center hover-primary"
			>
				<span>Mon</span>
				<span class="font-bold text-lg">3</span>
			</button>
			<button
				class="bg-primary-dark text-primary border-2 border-gray-500 p-4 rounded-2xl flex flex-col"
			>
				<span>Mon</span>
				<span class="font-bold text-lg">2</span>
			</button>
			<button
				class="border-2 border-gray-500 p-4 rounded-2xl flex flex-col text-primary-in-clean text-center hover-primary"
			>
				<span>Mon</span>
				<span class="font-bold text-lg">3</span>
			</button>
		</div>
		<div
			class="flex self-end pt-24 px-3 bottom-1 divide-x-2 divide-gray-400 space-x-3"
		>
			<span class="text-primary-in-clean text-6xl font-medium">23%</span>
			<div class="flex pl-3 text-primary-in-clean font-semibold flex-col">
				<span> -10% </span>
				<span> Since last Rate </span>
			</div>
		</div>
	</div>
</div>
