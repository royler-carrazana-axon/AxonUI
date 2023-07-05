<script>
	import IconButton from "./../../components/ui/buttons/IconButton.svelte";
	import HeaderPage from "../../components/root/HeaderPage.svelte";
	import Button from "../../components/ui/buttons/Button.svelte";
	import Header1 from "../../components/ui/headers/Header1.svelte";

	const svg = `<svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-6 h-6 mx-auto"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6"
        />
      </svg> `;
</script>

<div>
	<HeaderPage title="Buttons" />
	<!-- Button Simple -->
	<div class="flex flex-col p-7">
		<div class="w-full bg-slate-100 p-2 rounded-md flex justify-between">
			<h3 class="subtitle">Button Simple</h3>
			<span class="text-sm text-gray-400 pr-3"
				>/ui/buttons/Button.svelte</span
			>
		</div>
		<div class="grid grid-cols-2 bg-gray-50">
			<div class="p-7">
				<Button />
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
			</div>
		</div>
	</div>
	<!-- Button with Icon -->
	<div class="flex flex-col p-7">
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
	</div>
</div>
