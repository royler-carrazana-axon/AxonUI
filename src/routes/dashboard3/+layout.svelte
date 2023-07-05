<script>
	import Sidebar1 from "../../components/sidebar/Sidebar1.svelte";
	import Sidebar2 from "../../components/sidebar/Sidebar2.svelte";
	import Header2 from "../../components/ui/headers/Header2.svelte";
</script>

<div class="px-10 mt-14 absolute inset-0 bg-black z-50 m-0 -mt-10 pt-20">
	<div class="flex flex-col bg-gradient-to-br text-gray-800 bg-white">
		<div class=" grid grid-cols-5">
			<div class="col-span-1 border-gray-600 border-r-2 h-screen">
				<Sidebar2 />
			</div>
			<div class="col-span-4">
				<Header2 />
				<div>
					<slot />
				</div>
			</div>
		</div>
	</div>
</div>
