<script>
	import { fade, fly } from "svelte/transition";
	import Card1Stat from "../../components/ui/cards/Card1Stat.svelte";
	import CardStat3 from "../../components/ui/cards/CardStat3.svelte";
	import CardStat4 from "../../components/ui/cards/CardStat4.svelte";
	import Card1People from "../../components/ui/cards/Card1People.svelte";
	import Divider from "../../components/ui/dividers/Divider.svelte";
</script>

<div class="px-10 mt-14 absolute inset-0 bg-black z-50 m-0 -mt-10 pt-20">
	<div class="grid p-7 grid-cols-3 gap-4">
		<CardStat3 color="bg-yellow-100/100" />
		<div class="flex flex-col space-y-3">
			<Card1Stat
				color="bg-gray-800/50"
				modelName="Users"
				modelValue={350}
				period="03/2023"
			/>
			<Card1Stat
				color="bg-gray-800/50"
				modelName="Projects"
				modelValue={350}
				period="03/2023"
			/>
			<Card1Stat
				color="bg-gray-800/50"
				modelName="Orders"
				modelValue={350}
				period="03/2023"
			/>
		</div>
		<CardStat4 />
	</div>

	<Divider />
  
	<div>
		<h2
			in:fly={{ y: 500, duration: 2000 }}
			class="text-2xl font-medium pt-2 px-7"
		>
			Staff conected
		</h2>
	</div>
	<div class="flex space-x-3 mt-7 px-7">
		<Card1People />
		<Card1People />
		<Card1People />
	</div>
</div>
