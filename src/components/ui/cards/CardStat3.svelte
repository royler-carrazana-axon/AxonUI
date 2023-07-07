<script lang="ts">
	import { fly, fade } from "svelte/transition";
	import { onMount } from "svelte";
	import type { ChartType, ChartConfiguration } from "chart.js/auto";

	import Chart from "chart.js/auto";

	export let color: string = "bg-sky-100";
	let portfolio: any;
	const data = {
		labels: ["Expenses", "Savings", "Investments"],
		datasets: [
			{
				label: "My First Dataset",
				data: [300, 50, 100],
				backgroundColor: ["#7000e1", "#fc8800", "#00b0e8"],
				// hoverOffset: 4,
				borderWidth: 0,
			},
		],
	};
	const config: ChartConfiguration<ChartType, number[], string> = {
		type: "doughnut",
		data: data,
		options: {
			responsive: true,
			plugins: {
				legend: {
					position: "bottom",
					display: true,
					labels: {
						usePointStyle: true,
						padding: 20,
						font: {
							size: 14,
						},
					},
				},
				title: {
					display: true,
					text: "My Personal Portfolio",
				},
			},
		},
	};
	onMount(() => {
		const ctx = portfolio.getContext("2d");
		// Initialize chart using default config set
		var myChart = new Chart(ctx, config);
	});
</script>

<canvas
	in:fly={{ y: 150, duration: 3000 }}
	out:fade
	class={` ${color}  h-auto  object-center rounded-3xl px-3`}
	bind:this={portfolio}
/>

<style>
	canvas {
		width: 100% !important;
		height: 100% !important;
	}
</style>
