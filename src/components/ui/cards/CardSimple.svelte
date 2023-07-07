<script lang="ts">
	import { fade, fly } from "svelte/transition";
	export let imageSrc: string = "/b5.jpg";
  export let link: string = "/b5.jpg";
  export let subtitle: string = "New Place:";
  export let title: string = "Time to unleassh the Explorer of new";
</script>

<div
	in:fly={{ y: 150, duration: 3000 }}
	out:fade
	class={`bg-[url('${imageSrc}')] h-56 bg-cover bg-center rounded-3xl p-3`}
>
	<div class="flex justify-between p-6">
		<div class="flex flex-col h-full justify-between">
			<div>
				<a href={link}>
					<button
						class="bg-primary rounded-full p-2 hover:rotate-12 text-center h-9 w-9"
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
					</button></a
				>

				<p class="text-primary font-semibold shadow-2xl mt-7 text-sm">
					{subtitle}
				</p>
				<h2 class="text-primary text-2xl font-bold">
					{title}
				</h2>
			</div>
		</div>
	</div>
</div>
