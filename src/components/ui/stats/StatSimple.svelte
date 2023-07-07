<script lang="ts">
	import { fade, fly } from "svelte/transition";

	//Params
	export let period: String = "Today";
	export let modelValue: Number = 333;
	export let modelName: String = "Users";
</script>

<div>
	<div class="grid grid-cols-2 bg-white">
		<div>
			<div
				in:fly={{ y: 150, duration: 3000 }}
				out:fade
				class={`bg-primary texxt-primary  h-auto  object-center  px-3`}
			>
				<div class="flex py-6">
					<button
						class="bg-primary-dark text-primary rounded-full p-2 hover:rotate-12 text-center h-9 w-9"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.5"
							stroke="currentColor"
							class="w-6 h-5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"
							/>
						</svg>
					</button>

					<div class="flex flex-col w-full pr-7 space-y-1">
						<p
							class="text-primary ml-auto font-semibold text-right shadow-2xl text-sm"
						>
							{period}
						</p>
						<h2
							class="text-primary text-2xl font-bold self-end text-left"
						>
							+ {modelValue}
							{modelName}
						</h2>
					</div>
				</div>
			</div>
		</div>
		<div>
			<div
				in:fly={{ y: 150, duration: 3000 }}
				out:fade
				class={` bg-primary text-primary  h-auto  object-center  px-3`}
			>
				<div class="flex py-6">
					<button
						class="bg-primary-dark text-primary rounded-full p-2 hover:rotate-12 text-center h-9 w-9"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.5"
							stroke="currentColor"
							class="w-6 h-5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"
							/>
						</svg>
					</button>

					<div class="flex flex-col w-full pr-7 space-y-1">
						<p
							class=" text-primary ml-auto font-semibold text-right shadow-2xl text-sm"
						>
					    {period}
						</p>
						<h2
							class=" text-primary text-2xl font-bold self-end text-left"
						>
							+ {modelValue}
							{modelName}
						</h2>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
