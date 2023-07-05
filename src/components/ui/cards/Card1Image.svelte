<script>
  import { fade, fly } from "svelte/transition";
  import Button1 from "../buttons/Button.svelte";
</script>

<div
  in:fly={{ y: 77, duration: 1500 }}
  out:fade
  class="bg-[url('/b5.jpg')] h-80 bg-cover bg-center rounded-3xl p-3"
>
  <div class="flex justify-between p-5">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke-width="1.5"
      stroke="currentColor"
      class="w-14 h-14 text-gray-100"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"
      />
    </svg>
    <div class="flex flex-col h-full justify-between w-3/6">
      <div>
        <p class="text-gray-100 text-sm">Most viewed place today:</p>
        <h2 class="text-gray-50 text-2xl font-bold">
          The Tangua Curitiba Park
        </h2>
      </div>
      <div class="mt-[22%]">
        <Button1 />
      </div>
    </div>
  </div>
</div>
